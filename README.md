# oxford_bioreactor

Parametric CAD for the soft hollow-fibre bioreactor chamber.

## `fusion360/end_piece_and_ring.py`

Builds one rigid **end piece** + its **tightening ring** (both Formlabs SLA, biocompatible
resin). The two chamber ends are geometrically identical, so this single part serves both —
print two end pieces and two rings.

**How to run**
1. In Fusion 360 open a new/empty **Design**, then **Utilities → Scripts and Add-Ins → Scripts → Create** a Python script and replace its `*.py` with `end_piece_and_ring.py` (or point the script folder at `fusion360/`).
2. Select it and click **Run**. It builds two components (`EndPiece`, `TighteningRing`) in the active document and pops a summary; nothing is saved or exported. Re-running is safe — it deletes and rebuilds the two components.
3. **Tweak first:** `shell_bore` (bore for the fibre bundle + potting) and `spigot_OD` (must match your silicone cuff ID); edit them under **Modify → Change Parameters** or at the top of the script, then Run again. Set `USE_LUER = False` near the top for hose barbs (`tubing_id`) instead of female Luer ports.
