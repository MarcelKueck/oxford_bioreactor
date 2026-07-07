# -*- coding: utf-8 -*-
#
# Soft hollow-fibre bioreactor chamber — ONE rigid END PIECE + its TIGHTENING RING.
# Fusion 360 script.  Paste into Scripts & Add-Ins -> "+" -> create a Python script,
# replace the generated file with this one, and Run.  Builds in the ACTIVE document.
#
# Architecture (one end piece, outboard -> inboard along +Z):
#   0  outboard face
#   1  AXIAL ICS port  (female Luer-lock 6% sealing taper)  ->
#   2  lumen-header cavity (dia = shell_bore)               ->
#   3  potting zone: plain through-bore (dia = shell_bore); fibres + PU form the plug later ->
#   4  90-degree ECS port (female Luer on a radial stub) tapping the bore ecs_inboard_offset
#      INBOARD of the potting zone (feeds the shell, never the lumen header)             ->
#   5  inboard SPIGOT (reduced OD, bore continues = shell_bore):
#        base->tip:  external THREADED BOSS | O-RING GROOVE | sealing BARB | CAPTURE GROOVE
#
# The two chamber ends are geometrically identical (one plumbed inlets, one outlets),
# so this single part serves both -> print two end pieces and two rings.
#
# Tightening ring: separate printed cap-nut. Internal thread on the boss, hard-stop
# shoulder, skirt over the cuff, internal capture lip, through-hole for cuff+membrane,
# and 6 external grip flats. Sits OUTSIDE the wetted path.
#
# NOTES / DECISIONS
#   * Doc check: Marie's transfer report gives post-stretch eHF ~198um OD / 89um lumen,
#     8 cm working length -> shell_bore=8 mm is ample. The assembly notes give the
#     silicone cuff sleeve as ~3.8 cm circumference (~12 mm ID) -> matches spigot_OD=12.
#     No document value contradicts the supplied defaults.
#   * Fusion's internal length unit is CENTIMETRES. Every length here is either a named
#     user parameter (mm) or built with ValueInput.createByString(...) -> no bare mm floats.
#   * The primary solids (body / boss / spigot / bores / stub / ring) are driven by
#     dimensions and offset planes bound to user parameters, so they update live when you
#     edit a parameter. The small revolved detail features (Luer tapers, grooves, barb) are
#     generated from the parameter values at build time; the script is idempotent (it
#     deletes and rebuilds the two components), so after changing a parameter just Run again.
#   * Threads use Fusion's modelled Thread feature where possible; if that proves
#     unreliable the boss/ring fall back to a smooth surface at the nominal major dia
#     (see "# TODO thread") and a warning is reported -- threads never block the build.

import adsk.core
import adsk.fusion
import math
import traceback

# ------------------------------------------------------------------ build switch
# use_luer=True  -> female Luer-lock ports (ISO 80369-7, 6% taper) on both circuits.
# use_luer=False -> hose barbs for silicone tubing of ID = tubing_id instead.
# (Boolean, so it is a Python switch, not a Fusion user parameter which must be numeric.)
USE_LUER = True


def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface

        design = adsk.fusion.Design.cast(app.activeProduct)
        if not design:
            ui.messageBox('No active Fusion design. Open a Design and run again.')
            return
        # Keep it parametric.
        design.designType = adsk.fusion.DesignTypes.ParametricDesignType

        root = design.rootComponent
        up = design.userParameters
        VI = adsk.core.ValueInput
        FO = adsk.fusion.FeatureOperations

        warnings = []
        created_params = []

        # -------------------------------------------------------------- parameters
        def add_param(name, expr, unit='mm', comment=''):
            """Create (or, on re-run, update) a user parameter. Everything tunable here."""
            p = up.itemByName(name)
            if p:
                p.expression = expr
            else:
                p = up.add(name, VI.createByString(expr), unit, comment)
            if name not in created_params:
                created_params.append(name)
            return p

        # --- BRIEF DEFAULTS (base) ------------------------------------------------
        add_param('shell_bore',        '8',    'mm', 'main bore; fibre bundle + potting')
        add_param('body_wall',         '3',    'mm', 'rigid body wall thickness')
        add_param('spigot_wall',       '2',    'mm', 'spigot tube wall thickness')
        add_param('lumen_header_depth', '4',   'mm', 'ICS header counterbore depth')
        add_param('potting_length',    '6',    'mm', 'axial length of the potting plug zone')
        add_param('ecs_inboard_offset', '5',   'mm', 'ECS tap sits this far INBOARD of potting')
        add_param('spigot_engagement', '12',   'mm', 'reduced-OD spigot length the cuff sits on')
        add_param('boss_thread_major', '20',   'mm', 'external boss thread major dia')
        add_param('thread_pitch',      '2',    'mm', 'boss/ring thread pitch')
        add_param('boss_length',       '8',    'mm', 'threaded boss axial length')
        add_param('ring_wall',         '3',    'mm', 'tightening-ring wall thickness')
        add_param('oring_cs',          '2',    'mm', 'O-ring cross-section dia')
        add_param('barb_height',       '0.5',  'mm', 'sealing barb radial height')
        add_param('capture_groove',    '1.5',  'mm', 'capture groove (square) side')
        add_param('ecs_stub_length',   '10',   'mm', 'radial ECS stub length beyond body OD')
        add_param('fillet_r',          '1',    'mm', 'fillet radius on step transitions')
        add_param('thread_clearance',  '0.35', 'mm', 'radial thread clearance (ring vs boss)')
        add_param('slip_clearance',    '0.2',  'mm', 'radial slip fit clearance')
        add_param('luer_mouth_ID',     '4.0',  'mm', 'female Luer mouth ID (ISO 80369-7)')
        add_param('luer_taper_length', '7.5',  'mm', 'female Luer taper engagement length')
        add_param('tubing_id',         '1.6',  'mm', 'barb fallback: silicone tubing ID')

        # --- ASSUMPTIONS (not fixed by the brief/docs; tune to your cuff & fittings) ---
        add_param('cuff_wall',      '1.5', 'mm', 'ASSUMED silicone cuff wall thickness')
        add_param('cuff_flange',    '1.5', 'mm', 'ASSUMED cuff mouth-flange radial height')
        add_param('ecs_stub_od',    '8.0', 'mm', 'ASSUMED ECS stub OD (houses female Luer)')
        add_param('ecs_channel_dia', '2.0', 'mm', 'ASSUMED ECS connecting channel bore')
        add_param('barb_width',     '1.2', 'mm', 'ASSUMED sealing-barb axial width')
        add_param('ring_lip_length', '2.0', 'mm', 'ASSUMED ring capture-lip length')
        add_param('ring_grip_depth', '0.6', 'mm', 'ASSUMED grip flat depth')
        add_param('barb_boss_len',  '6.0', 'mm', 'ASSUMED hose-barb nipple length (use_luer=False)')

        # --- DERIVED (expressions -> stay parametric) -----------------------------
        add_param('body_OD',           'shell_bore + 2 * body_wall',   'mm', 'rigid body OD')
        add_param('spigot_OD',         'shell_bore + 2 * spigot_wall', 'mm', 'spigot OD')
        add_param('ring_OD',           'boss_thread_major + 2 * ring_wall', 'mm', 'ring OD')
        add_param('oring_groove_depth', '0.75 * oring_cs', 'mm', 'O-ring groove depth')
        add_param('oring_groove_width', '1.3 * oring_cs',  'mm', 'O-ring groove width')
        add_param('luer_small_dia',    'luer_mouth_ID - 0.06 * luer_taper_length', 'mm',
                  'female Luer taper small dia (6% per 10 mm)')
        # axial stations (z, outboard face = 0, +Z inboard)
        add_param('z_luer_end',   'luer_taper_length', 'mm', 'end of axial Luer taper')
        add_param('z_pot_start',  'luer_taper_length + lumen_header_depth', 'mm', 'potting start')
        add_param('z_pot_end',    'z_pot_start + potting_length', 'mm', 'potting end')
        add_param('z_ecs',        'z_pot_end + ecs_inboard_offset', 'mm', 'ECS tap centreline')
        add_param('ecs_body_margin', 'ecs_stub_od / 2 + 2', 'mm', 'body length past ECS tap')
        add_param('body_length',  'z_ecs + ecs_body_margin', 'mm', 'rigid body axial length')
        add_param('z_boss_end',   'body_length + boss_length', 'mm', 'boss tip station')
        add_param('z_spigot_tip', 'z_boss_end + spigot_engagement', 'mm', 'spigot tip station')
        add_param('ecs_tip_x',    'body_OD / 2 + ecs_stub_length', 'mm', 'radial x of ECS stub tip')
        add_param('ecs_stub_reach', 'body_wall + ecs_stub_length', 'mm', 'stub extrude length from bore wall')
        add_param('z_oring',   'z_boss_end + 3', 'mm', 'O-ring groove centre')
        add_param('z_barb',    'z_boss_end + spigot_engagement / 2', 'mm', 'sealing barb centre')
        add_param('z_capture', 'z_spigot_tip - 3', 'mm', 'capture groove centre')
        # ring internals
        add_param('cuff_tube_od',    'spigot_OD + 2 * cuff_wall', 'mm', 'cuff OD on the spigot')
        add_param('ring_lip_id',     'cuff_tube_od + 2 * slip_clearance', 'mm', 'ring through-hole / lip ID')
        add_param('ring_skirt_bore', 'ring_lip_id + 2 * cuff_flange', 'mm', 'ring skirt bore over cuff flange')
        add_param('ring_thread_bore', 'boss_thread_major + 2 * thread_clearance', 'mm', 'ring internal thread bore')
        add_param('ring_length',     'boss_length + spigot_engagement', 'mm', 'ring axial length')
        add_param('ring_skirt_len',  'ring_length - boss_length - ring_lip_length', 'mm', 'ring skirt bore length')

        def cm(name):
            """Current value of a user parameter, in Fusion internal units (cm)."""
            return up.itemByName(name).value

        # -------------------------------------------------- idempotent rebuild
        m = adsk.core.Matrix3D.create()

        # Remove previously built components (Assembly Design doc) ...
        for i in range(root.occurrences.count - 1, -1, -1):
            oc = root.occurrences.item(i)
            if oc.component.name in ('EndPiece', 'TighteningRing'):
                oc.deleteMe()
        # ... or previously built bodies (single-component / Part Design doc)
        for nm in ('end_piece', 'tightening_ring'):
            b = root.bRepBodies.itemByName(nm)
            if b:
                b.deleteMe()

        # Separate components need an Assembly Design document. A "Part Design"
        # document allows only ONE component, so fall back to building both parts
        # as separate BODIES in the root component instead of hard-failing.
        single_component = False

        def make_container(name):
            nonlocal single_component
            try:
                c = root.occurrences.addNewComponent(m).component
                c.name = name
                return c
            except Exception:
                single_component = True
                return root

        endComp = make_container('EndPiece')
        ringComp = make_container('TighteningRing')
        if single_component:
            warnings.append(
                'This document allows only ONE component (Part Design doc) -> built the '
                'end piece and ring as two BODIES ("end_piece", "tightening_ring") in the '
                'root component. For separate, individually printable components, run this in '
                'an ASSEMBLY document (File > New > Assembly Design), then re-run.')

        # -------------------------------------------------- small helpers
        def offset_plane(comp, base, expr):
            pi = comp.constructionPlanes.createInput()
            pi.setByOffset(base, VI.createByString(expr))
            return comp.constructionPlanes.add(pi)

        def add_circle(sk, world_xyz, radius_cm):
            c = sk.modelToSketchSpace(adsk.core.Point3D.create(*world_xyz))
            return sk.sketchCurves.sketchCircles.addByCenterRadius(c, radius_cm)

        def bind_dia(sk, circ, expr):
            """Bind a circle to a diameter parameter (geometry already correct if this fails)."""
            try:
                cp = circ.centerSketchPoint.geometry
                tp = adsk.core.Point3D.create(cp.x + circ.radius, cp.y, 0)
                dim = sk.sketchDimensions.addDiameterDimension(circ, tp, True)
                dim.parameter.expression = expr
            except Exception:
                warnings.append('could not bind dia dimension to "%s"' % expr)

        def extrude(comp, sk, dist_expr, operation, body=None, positive=True, prof_index=0):
            prof = sk.profiles.item(prof_index)
            ei = comp.features.extrudeFeatures.createInput(prof, operation)
            d = VI.createByString(dist_expr if positive else '-(%s)' % dist_expr)
            ei.setDistanceExtent(False, d)
            if body is not None and operation != FO.NewBodyFeatureOperation:
                ei.participantBodies = [body]
            return comp.features.extrudeFeatures.add(ei)

        def extrude_all(comp, sk, body, positive=True, prof_index=0):
            prof = sk.profiles.item(prof_index)
            ei = comp.features.extrudeFeatures.createInput(prof, FO.CutFeatureOperation)
            dirn = (adsk.fusion.ExtentDirections.PositiveExtentDirection if positive
                    else adsk.fusion.ExtentDirections.NegativeExtentDirection)
            ei.setAllExtent(dirn)
            ei.participantBodies = [body]
            return comp.features.extrudeFeatures.add(ei)

        def revolve_profile(comp, pts_xz):
            """Closed polyline in the XZ plane from world (x,0,z) points; returns the sketch."""
            sk = comp.sketches.add(comp.xZConstructionPlane)
            sk.isComputeDeferred = True
            lines = sk.sketchCurves.sketchLines
            sp = [sk.modelToSketchSpace(adsk.core.Point3D.create(p[0], 0.0, p[1])) for p in pts_xz]
            first = lines.addByTwoPoints(sp[0], sp[1])
            prev = first
            for i in range(2, len(sp)):
                prev = lines.addByTwoPoints(prev.endSketchPoint, sp[i])
            lines.addByTwoPoints(prev.endSketchPoint, first.startSketchPoint)
            sk.isComputeDeferred = False
            return sk

        def revolve(comp, sk, axis, operation, body=None):
            prof = sk.profiles.item(0)
            ri = comp.features.revolveFeatures.createInput(prof, axis, operation)
            ri.setAngleExtent(False, VI.createByString('360 deg'))
            if body is not None and operation != FO.NewBodyFeatureOperation:
                ri.participantBodies = [body]
            return comp.features.revolveFeatures.add(ri)

        def find_circ_edge(body, z_cm, r_cm, tol=0.03):
            for e in body.edges:
                g = e.geometry
                if g and g.objectType == adsk.core.Circle3D.classType():
                    if abs(g.center.z - z_cm) < tol and abs(g.radius - r_cm) < tol:
                        return e
            return None

        def fillet_edge(comp, body, z_cm, r_cm, tag):
            try:
                e = find_circ_edge(body, z_cm, r_cm)
                if not e:
                    warnings.append('fillet edge not found: %s' % tag)
                    return
                col = adsk.core.ObjectCollection.create()
                col.add(e)
                fi = comp.features.filletFeatures.createInput()
                fi.addConstantRadiusEdgeSet(col, VI.createByString('fillet_r'), True)
                comp.features.filletFeatures.add(fi)
            except Exception:
                warnings.append('fillet failed: %s' % tag)

        def find_cyl_face(body, r_cm, zmin, zmax, tol=0.05):
            for f in body.faces:
                s = f.geometry
                if s and s.objectType == adsk.core.Cylinder.classType() and abs(s.radius - r_cm) < tol:
                    bb = f.boundingBox
                    if bb.minPoint.z >= zmin - 0.1 and bb.maxPoint.z <= zmax + 0.1:
                        return f
            return None

        def add_thread(comp, face, is_internal, dia_cm, tag):
            """Modelled thread; returns True on success, else records a fallback warning."""
            try:
                threads = comp.features.threadFeatures
                q = threads.threadDataQuery
                res = q.recommendThreadData(dia_cm, is_internal, False)
                # res -> (Boolean, threadType, threadDesignation, threadClass)
                if not res[0]:
                    warnings.append('%s: no matching thread size -> smooth (# TODO thread)' % tag)
                    return False
                tinfo = threads.createThreadInfo(is_internal, res[1], res[2], res[3])
                faces = adsk.core.ObjectCollection.create()
                faces.add(face)
                tin = threads.createInput(faces, tinfo)
                tin.isModeled = True
                threads.add(tin)
                warnings.append('%s: modelled thread "%s" (verify pitch vs thread_pitch)' % (tag, res[2]))
                return True
            except Exception:
                warnings.append('%s: thread feature failed -> smooth boss (# TODO thread)' % tag)
                return False

        # ================================================================ END PIECE
        bl = cm('body_length')
        zbe = cm('z_boss_end')
        zst = cm('z_spigot_tip')
        zle = cm('z_luer_end')
        zecs = cm('z_ecs')
        etx = cm('ecs_tip_x')
        bod = cm('body_OD')
        sod = cm('spigot_OD')
        btm = cm('boss_thread_major')
        sb = cm('shell_bore')
        mouth_r = cm('luer_mouth_ID') / 2.0
        small_r = cm('luer_small_dia') / 2.0
        tl = cm('luer_taper_length')

        # E1 -- body cylinder (dia = body_OD, 0 -> body_length)
        sk = endComp.sketches.add(endComp.xYConstructionPlane)
        c = add_circle(sk, (0, 0, 0), bod / 2.0)
        bind_dia(sk, c, 'body_OD')
        endBody = extrude(endComp, sk, 'body_length', FO.NewBodyFeatureOperation).bodies.item(0)
        endBody.name = 'end_piece'

        # E2 -- threaded boss (dia = boss_thread_major)
        pl_be = offset_plane(endComp, endComp.xYConstructionPlane, 'body_length')
        sk = endComp.sketches.add(pl_be)
        c = add_circle(sk, (0, 0, bl), btm / 2.0)
        bind_dia(sk, c, 'boss_thread_major')
        extrude(endComp, sk, 'boss_length', FO.JoinFeatureOperation, endBody)

        # E3 -- reduced-OD spigot tube (dia = spigot_OD)
        pl_bo = offset_plane(endComp, endComp.xYConstructionPlane, 'z_boss_end')
        sk = endComp.sketches.add(pl_bo)
        c = add_circle(sk, (0, 0, zbe), sod / 2.0)
        bind_dia(sk, c, 'spigot_OD')
        extrude(endComp, sk, 'spigot_engagement', FO.JoinFeatureOperation, endBody)

        # E4 -- main through-bore (dia = shell_bore) from header floor to spigot tip
        pl_le = offset_plane(endComp, endComp.xYConstructionPlane, 'z_luer_end')
        sk = endComp.sketches.add(pl_le)
        c = add_circle(sk, (0, 0, zle), sb / 2.0)
        bind_dia(sk, c, 'shell_bore')
        extrude_all(endComp, sk, endBody, positive=True)

        # E6 -- ECS radial stub (join), from bore wall outward along +X
        pl_stub = offset_plane(endComp, endComp.yZConstructionPlane, 'shell_bore/2')
        sk = endComp.sketches.add(pl_stub)
        c = add_circle(sk, (sb / 2.0, 0, zecs), cm('ecs_stub_od') / 2.0)
        bind_dia(sk, c, 'ecs_stub_od')
        extrude(endComp, sk, 'ecs_stub_reach', FO.JoinFeatureOperation, endBody, positive=True)

        if USE_LUER:
            # E5 -- axial female Luer socket (6% taper), revolve-cut about Z
            sk = revolve_profile(endComp, [(0, 0), (mouth_r, 0), (small_r, tl), (0, tl)])
            revolve(endComp, sk, endComp.zConstructionAxis, FO.CutFeatureOperation, endBody)

            # E7 -- ECS female Luer socket, revolve-cut about the stub's X axis
            axInput = endComp.constructionAxes.createInput()
            axInput.setByLine(adsk.core.InfiniteLine3D.create(
                adsk.core.Point3D.create(0, 0, zecs), adsk.core.Vector3D.create(1, 0, 0)))
            ecsAxis = endComp.constructionAxes.add(axInput)
            sk = revolve_profile(endComp, [(etx, zecs), (etx, zecs + mouth_r),
                                           (etx - tl, zecs + small_r), (etx - tl, zecs)])
            revolve(endComp, sk, ecsAxis, FO.CutFeatureOperation, endBody)

            # E7b -- ECS connecting channel from socket apex inward to the main bore
            pl_tip = offset_plane(endComp, endComp.yZConstructionPlane, 'ecs_tip_x')
            sk = endComp.sketches.add(pl_tip)
            c = add_circle(sk, (etx, 0, zecs), cm('ecs_channel_dia') / 2.0)
            bind_dia(sk, c, 'ecs_channel_dia')
            extrude(endComp, sk, 'ecs_tip_x', FO.CutFeatureOperation, endBody, positive=False)
        else:
            # ---- hose-barb fallback (silicone tubing ID = tubing_id) ----
            tid = cm('tubing_id')
            bbl = cm('barb_boss_len')
            tube_r = (tid + 0.06) / 2.0   # nipple wall a touch over tubing ID
            ridge_r = (tid + 0.14) / 2.0  # retaining ridge slightly larger

            # axial barb nipple protruding outboard (-Z) + bore to header
            sk = endComp.sketches.add(endComp.xYConstructionPlane)
            add_circle(sk, (0, 0, 0), tube_r)
            extrude(endComp, sk, 'barb_boss_len', FO.JoinFeatureOperation, endBody, positive=False)
            pl_tip = offset_plane(endComp, endComp.xYConstructionPlane, '-(barb_boss_len)')
            sk = endComp.sketches.add(pl_tip)
            add_circle(sk, (0, 0, -bbl), ridge_r)
            extrude(endComp, sk, 'barb_width', FO.JoinFeatureOperation, endBody, positive=True)
            sk = endComp.sketches.add(endComp.xYConstructionPlane)
            c = add_circle(sk, (0, 0, 0), tid / 2.0)
            bind_dia(sk, c, 'tubing_id')
            extrude(endComp, sk, 'z_luer_end', FO.CutFeatureOperation, endBody, positive=True)
            sk = endComp.sketches.add(endComp.xYConstructionPlane)
            add_circle(sk, (0, 0, 0), tid / 2.0)
            extrude(endComp, sk, 'barb_boss_len', FO.CutFeatureOperation, endBody, positive=False)

            # ECS barb nipple on the stub tip (+X) + channel bore
            pl_tip = offset_plane(endComp, endComp.yZConstructionPlane, 'ecs_tip_x')
            sk = endComp.sketches.add(pl_tip)
            add_circle(sk, (etx, 0, zecs), tube_r)
            extrude(endComp, sk, 'barb_boss_len', FO.JoinFeatureOperation, endBody, positive=True)
            pl_r = offset_plane(endComp, endComp.yZConstructionPlane, 'ecs_tip_x + barb_boss_len')
            sk = endComp.sketches.add(pl_r)
            add_circle(sk, (etx + bbl, 0, zecs), ridge_r)
            extrude(endComp, sk, 'barb_width', FO.JoinFeatureOperation, endBody, positive=True)
            sk = endComp.sketches.add(pl_tip)
            c = add_circle(sk, (etx, 0, zecs), tid / 2.0)
            bind_dia(sk, c, 'tubing_id')
            extrude(endComp, sk, 'ecs_tip_x', FO.CutFeatureOperation, endBody, positive=False)
            sk = endComp.sketches.add(pl_tip)
            add_circle(sk, (etx, 0, zecs), tid / 2.0)
            extrude(endComp, sk, 'barb_boss_len', FO.CutFeatureOperation, endBody, positive=True)
            warnings.append('USE_LUER=False: simplified hose barbs built (nipple+ridge), not ISO Luer.')

        # E8 -- O-ring groove on the spigot (revolve cut)
        ogd = cm('oring_groove_depth')
        ogw = cm('oring_groove_width')
        zor = cm('z_oring')
        sk = revolve_profile(endComp, [
            (sod / 2.0 - ogd, zor - ogw / 2.0), (sod / 2.0, zor - ogw / 2.0),
            (sod / 2.0, zor + ogw / 2.0), (sod / 2.0 - ogd, zor + ogw / 2.0)])
        revolve(endComp, sk, endComp.zConstructionAxis, FO.CutFeatureOperation, endBody)

        # E9 -- capture groove near the spigot tip (square, revolve cut)
        cg = cm('capture_groove')
        zcap = cm('z_capture')
        sk = revolve_profile(endComp, [
            (sod / 2.0 - cg, zcap - cg / 2.0), (sod / 2.0, zcap - cg / 2.0),
            (sod / 2.0, zcap + cg / 2.0), (sod / 2.0 - cg, zcap + cg / 2.0)])
        revolve(endComp, sk, endComp.zConstructionAxis, FO.CutFeatureOperation, endBody)

        # E10 -- sealing barb ridge on the spigot (revolve join)
        bh = cm('barb_height')
        bw = cm('barb_width')
        zb = cm('z_barb')
        sk = revolve_profile(endComp, [
            (sod / 2.0, zb - bw / 2.0), (sod / 2.0 + bh, zb), (sod / 2.0, zb + bw / 2.0)])
        revolve(endComp, sk, endComp.zConstructionAxis, FO.JoinFeatureOperation, endBody)

        # E11 -- fillets on the step / thick-thin transitions (each is best-effort)
        fillet_edge(endComp, endBody, bl, bod / 2.0, 'body->boss step')
        fillet_edge(endComp, endBody, zbe, sod / 2.0, 'boss->spigot step')
        fillet_edge(endComp, endBody, zle, sb / 2.0, 'header counterbore floor')

        # E12 -- boss external thread (modelled, else smooth # TODO thread)
        boss_face = find_cyl_face(endBody, btm / 2.0, bl, zbe)
        if boss_face:
            add_thread(endComp, boss_face, False, btm / 2.0, 'boss')
        else:
            warnings.append('boss thread face not found -> smooth boss (# TODO thread)')

        # ================================================================ TIGHTENING RING
        rod = cm('ring_OD')
        rtb = cm('ring_thread_bore')

        # R1 -- outer cylinder (assembled position: over the boss + spigot)
        pl_r0 = offset_plane(ringComp, ringComp.xYConstructionPlane, 'body_length')
        sk = ringComp.sketches.add(pl_r0)
        c = add_circle(sk, (0, 0, bl), rod / 2.0)
        bind_dia(sk, c, 'ring_OD')
        ringBody = extrude(ringComp, sk, 'ring_length', FO.NewBodyFeatureOperation).bodies.item(0)
        ringBody.name = 'tightening_ring'

        # R2 -- through-hole / capture-lip ID (full length)
        sk = ringComp.sketches.add(pl_r0)
        c = add_circle(sk, (0, 0, bl), cm('ring_lip_id') / 2.0)
        bind_dia(sk, c, 'ring_lip_id')
        extrude_all(ringComp, sk, ringBody, positive=True)

        # R3 -- thread bore over the boss (leaves a hard-stop shoulder at the boss tip)
        sk = ringComp.sketches.add(pl_r0)
        c = add_circle(sk, (0, 0, bl), rtb / 2.0)
        bind_dia(sk, c, 'ring_thread_bore')
        extrude(ringComp, sk, 'boss_length', FO.CutFeatureOperation, ringBody, positive=True)

        # R4 -- skirt bore over the cuff flange (stops short -> internal capture lip)
        pl_r1 = offset_plane(ringComp, ringComp.xYConstructionPlane, 'z_boss_end')
        sk = ringComp.sketches.add(pl_r1)
        c = add_circle(sk, (0, 0, zbe), cm('ring_skirt_bore') / 2.0)
        bind_dia(sk, c, 'ring_skirt_bore')
        extrude(ringComp, sk, 'ring_skirt_len', FO.CutFeatureOperation, ringBody, positive=True)

        # R5 -- 6 external grip flats: intersect the ring with a rounded-corner hex prism
        try:
            grip_depth = cm('ring_grip_depth')
            R = (rod - 2.0 * grip_depth) / math.sqrt(3.0)   # hex circumradius
            sk = ringComp.sketches.add(pl_r0)
            sk.isComputeDeferred = True
            lines = sk.sketchCurves.sketchLines
            hp = []
            for k in range(6):
                a = math.radians(30 + 60 * k)
                hp.append(sk.modelToSketchSpace(
                    adsk.core.Point3D.create(R * math.cos(a), R * math.sin(a), bl)))
            first = lines.addByTwoPoints(hp[0], hp[1])
            prev = first
            for k in range(2, 6):
                prev = lines.addByTwoPoints(prev.endSketchPoint, hp[k])
            lines.addByTwoPoints(prev.endSketchPoint, first.startSketchPoint)
            sk.isComputeDeferred = False
            hexBody = extrude(ringComp, sk, 'ring_length', FO.NewBodyFeatureOperation).bodies.item(0)
            tools = adsk.core.ObjectCollection.create()
            tools.add(hexBody)
            ci = ringComp.features.combineFeatures.createInput(ringBody, tools)
            ci.operation = FO.IntersectFeatureOperation
            ci.isKeepToolBodies = False
            ringComp.features.combineFeatures.add(ci)
        except Exception:
            warnings.append('grip flats failed -> ring left round')

        # R6 -- ring internal thread (modelled, else smooth # TODO thread)
        thread_face = find_cyl_face(ringBody, rtb / 2.0, bl, zbe)
        if thread_face:
            add_thread(ringComp, thread_face, True, rtb / 2.0, 'ring')
        else:
            warnings.append('ring thread face not found -> smooth bore (# TODO thread)')

        # ================================================================ SUMMARY
        def val_mm(n):
            return up.itemByName(n).value * 10.0

        lines_out = []
        lines_out.append('=== Bioreactor end piece + tightening ring ===')
        lines_out.append('Built as %s: bodies "%s" + "%s"'
                         % ('two BODIES in the root component' if single_component
                            else 'two separate components (EndPiece, TighteningRing)',
                            endBody.name, ringBody.name))
        lines_out.append('Luer ports: %s' % ('female Luer-lock 6%% taper (mouth %.2f, small %.2f mm)'
                         % (val_mm('luer_mouth_ID'), val_mm('luer_small_dia')) if USE_LUER
                         else 'hose barbs for tubing ID %.2f mm' % val_mm('tubing_id')))
        lines_out.append('Key dims (mm): shell_bore %.1f, body_OD %.1f, spigot_OD %.1f, '
                         'boss_major %.1f, ring_OD %.1f, body_len %.1f, spigot_tip %.1f'
                         % (val_mm('shell_bore'), val_mm('body_OD'), val_mm('spigot_OD'),
                            val_mm('boss_thread_major'), val_mm('ring_OD'),
                            val_mm('body_length'), val_mm('z_spigot_tip')))
        lines_out.append('User parameters created/updated: %d' % len(created_params))
        lines_out.append('  ' + ', '.join(created_params))
        if warnings:
            lines_out.append('Notes / fallbacks (%d):' % len(warnings))
            for w in warnings:
                lines_out.append('  - ' + w)
        else:
            lines_out.append('No warnings.')

        summary = '\n'.join(lines_out)
        try:
            app.log(summary)          # -> Text Commands console
        except Exception:
            print(summary)

        ui.messageBox(summary + '\n\nDone', 'End piece + ring built')

    except Exception:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
