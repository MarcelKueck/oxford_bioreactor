# Soft Hollow-Fibre Bioreactor Chamber — Project Working Document

*Personal reference and working log. Created 26 June 2026.*
*This is a living document — update the checklists, logs, and KPIs as the project moves and as numbers get locked down.*

---

## 0. How to use this

This is my single source of truth for the internship: what I'm building, why, what's been tried already, what the targets are, and what I still need to find out. Sections 1–2 are context I can re-read or lift when explaining the project. Sections 3–9 are the working core. Sections 10–12 are checklists and logs I tick off and add to as I go.

The one structural idea to keep in mind: **everything is organised around two feedback loops** (chamber design, then fibre potting), and a feedback loop is only real if the test half produces a repeatable *number*. So my first job isn't a chamber redesign — it's building the test rig that makes redesigns comparable.

---

## 1. Project at a glance

**What the project is.** I'm contributing to Marie Kruth's DPhil (NDORMS, supervised by Prof. Pierre-Alexis Mouthuy, with Profs. Philippa Hulley and Hua Ye). The DPhil is building a human *in vitro* skeletal-muscle model to reduce reliance on animal models — most drugs that work in animals fail in human trials, so there's a real need for human-relevant muscle tissue for drug testing and disease study.

**The three-part DPhil plan, and where I fit:**

1. *Electrospun hollow-fibre (eHF) scaffold* — mostly done (dissolvable collector, electrospinning, stretch-alignment). This is Marie's completed work.
2. **Soft flexible bioreactor chamber** — **this is my piece.** The chamber houses the fibre bundle, perfuses it (artificial vasculature, beating the ~100–200 µm diffusion limit), and transmits mechanical stretch to the growing tissue.
3. *Muscle culture + drug response* — downstream, depends on a working chamber.

**Why "soft."** Muscle needs cyclic mechanical loading to mature. So the chamber can't be a rigid cartridge — it has to flex to pass stretch from an external mechanical platform to the fibres, while still perfusing them.

**People & roles**
- *Marie Kruth* — supervisor, owns the DPhil, my main point of contact and the source of most of the numbers I still need.
- *Prof. Mouthuy* — PI; his group also built the humanoid bioreactor platform (Mouthuy et al., 2022, *Comms Eng*) that's a candidate mechanical-loading system.
- *Profs. Hulley & Ye* — co-supervisors.

**Timeline note.** The project proposal labels the build as Aug–Sept 2026, but I'm starting now (late June). That's actually ideal: **June–July is the natural window to build the test rigs and lock down the missing numbers**, so that when the core build phase hits I'm iterating against real, quantitative targets instead of figuring out how to measure things.

**Toolchain:** Fusion 360 (CAD) → SLA 3D printing (clear medical-grade resin) → soft membrane bonded on (Permali Tuftane TPU film, Stormsure polyurethane glue).

---

## 2. What I'm building

### The inherited starting point (one option, not a requirement)
The design I'm inheriting: two rigid SLA-printed end-pieces ("top and bottom") connected by a flexible TPU membrane sleeve in the middle. Medium perfuses through; the membrane flexes to transmit stretch; the fibre bundle runs down the axis, potted into the printed pieces at each end. **This is a valid starting point, not a constraint** — see "Architecture: what's fixed vs what's mine to decide" below.

### Current design state (from my Fusion file)
The model shows the two printed pieces. Each has:
- A main **axial bore** with a **threaded ("screwed") collar** at the connecting end.
- A **side luer-lock port**.
- **Grooves** for the membrane and elastic-ring fixation.

The threaded collars and the membrane are how the two halves join; the membrane bridges them in the assembled chamber.

### The fibres the chamber must accommodate
Post-stretch eHF specs (PVA-based, from Marie's transfer report) — these constrain the bore geometry and potting volume:
- Overall diameter ≈ **198 µm**, wall ≈ **41 µm**, lumen ≈ **89 µm**
- Working length used in potting trials: **8 cm**
- This phase: tens of fibres (potting trials ran ~10–18). **Eventual target: several hundred fibres**, potted with intact dissolvable cores then flushed simultaneously.

### The two flow circuits — RESOLVED: 2 pairs, 4 ports total
**Confirmed:** the chamber has **two independent flow circuits**, each with its own inlet and outlet → **2 inlets + 2 outlets = 4 ports.**
- **Intracapillary (ICS)** — flow *through the fibre lumens*. Natural route is **axial** (in one end, out the other), so the fibre ends must stay open to the ICS header.
- **Extracapillary (ECS)** — flow through the **shell space around the fibres**, between the end seals. Natural route is the **side ports** (in one end, out the other).

So one valid layout is: ICS inlet + outlet = the two **axial** openings (one per end); ECS inlet + outlet = the two **side** ports (one per end). That's the topology the current Fusion model already has (axial bore + one side port per piece) — so resolving to 4 ports **doesn't necessarily mean adding ports**, it confirms what each existing port is *for*.

**The consequence that matters:** the **potting is what separates ICS from ECS.** Each end's pot must seal the shell space off from the lumen header so the two circuits can't cross-leak. That makes the ICS–ECS seal (and lumen patency) central to potting, not a nice-to-have — see §6 and the patency test in §7.

### Architecture: what's fixed vs what's mine to decide
The *requirements* are fixed. The *architecture* — how I actually realise them — is my call.

**Fixed (must be met, however I build it):**
- Leakproof under the pump / pressure conditions
- Correct dimensions (accommodates the fibre bundle; specs above)
- 2 inlets + 2 outlets (independent ICS and ECS circuits)
- Fibres can be integrated (potted, patent, surviving stretch)
- Flexible enough to transmit mechanical signals + mount to a loading platform
- Easy to assemble; looks finished, not prototype-y

**Open (my design decision) — the form factor and how flex is achieved.** Candidate directions, *not* a recommendation:
- *Inherited multi-part:* rigid SLA end-pieces + bonded flexible TPU membrane (current model).
- *Monolithic single-print:* the whole chamber printed in one go, possibly in a flexible resin so flex is intrinsic — no membrane bond, no threaded joint.
- *Fully flexible:* entirely soft body.
- Hybrids of the above.

**The one fact linking this choice to the inherited problems:** in the sealing history (§5), *every* persistent leak is at a **joint** — the threaded ends, the side ports, the membrane bond. Leakproof is a hard requirement. So the architecture choice is largely a decision about **how many joints I'm willing to have, and how each one seals.** A monolithic flexible print could eliminate the threaded joint and the membrane bond entirely — potentially dissolving most of §5 — at the cost of needing a suitable flexible printable resin and rethinking potting access and sterilisation. (The potting seal and the port connections remain regardless of architecture.) That tradeoff is the thing to weigh first.

---

## 3. Requirements, must-haves & KPIs (from kickoff)

### Requirements
- **Functional** — it works.
- **Easy to assemble** — reproducible, not fiddly.
- **Looks good — not like a prototype.** A finished-looking device, not grease-and-tape.

### Must-haves
- **Two inlets + two outlets (4 ports)** — independent ICS and ECS circuits (resolved; see §2).
- **Fibres can be integrated** (potting works and survives).
- **Flexible system to transmit mechanical signals** — must integrate into a mechanical loading platform.

### KPIs (as stated — these need real numbers)
- 10,000 cycles of cyclic loading
- A certain pressure held for a certain time
- Structural integrity after a certain time in the pump system

### What each KPI actually means, and the numbers I have to get

The KPIs are the right *instincts* but under-specified, and most of the missing numbers aren't mine to invent — they come from the pump, the platform, and the culture protocol. They resolve into **three distinct tests**:

| Test | What it measures | Why "a certain X" is incomplete | Number I need |
|---|---|---|---|
| **Burst / leak pressure** | Quasi-static: pressure at which it leaks or fails | A pressure target is meaningless without the pump's working pressure to set a margin above | Pump **operating pressure** (+ flow rate) |
| **Cyclic fatigue** | Survival over 10k cycles | Cycles are meaningless without **strain amplitude + frequency**. At ~1 Hz, 10k cycles ≈ 3 h — almost certainly a **first milestone**, not the endurance bar | Strain %, frequency, and the *real* target cycle count / duration |
| **Combined endurance** | Perfusion **+** cyclic loading running together over time; catches delamination & slow leaks the other two miss | "A certain time" must be tied to how long a culture actually runs (muscle differentiation is often 1–2+ weeks) | Intended **culture duration** |

> Typical muscle stimulation lands somewhere around ~10% strain at ~0.5–1 Hz, but this varies a lot — **do not hard-code it; get the actual protocol from Marie.**

---

## 4. My operating structure: the two feedback loops

The kickoff defined two prioritised feedback loops. The dependency order is correct and worth internalising.

```
PRIORITY 1 — CHAMBER DESIGN LOOP
   design (Fusion) → SLA print → ASSEMBLE → quantitative test → iterate
                                              │
                          (leak / pressure / cyclic / endurance + mechanical attachment)

PRIORITY 2 — FIBRE POTTING LOOP
   potting protocol → pot bundle → quantitative readout → iterate
                                        │
                       (lumen patency % / alignment / ICS–ECS seal)
```

**Why P1 leads:** a chamber that won't seal or survive the pump is useless however cleanly the fibres are potted. I *can* pot into a rough chamber to test potting in isolation, but I *can't* meaningfully test sealing without a chamber design first. So P1 first, and the two loops can later run partly in parallel.

**The real first task (hiding inside P1):** a feedback loop needs a repeatable number. The lab's current leak test is qualitative — run water, watch for drops. That tells me *leaks / doesn't leak today*, not whether v3 is 20% better than v2. **So before any chamber iteration, build the test rig** (see §7). Treat "build the rig" as task 0 and the first redesign as its first input.

---

## 5. Inherited problem 1 — Sealing (the heart of Priority 1)

### The situation in one paragraph
The **membrane-to-printed-piece bond** can be made to work well. The persistent leak points are the **threaded ("screwed") end joints** and the **side luer ports**. The *only* thing that has ever fully sealed them is **vacuum grease + multiple parafilm layers** — which is impractical, fails "looks good," fails "easy to assemble," *and still leaks if pressure is pushed*. Replacing this grease-and-tape approach with a designed/glued solution is **the** central unsolved problem for P1.

### What's been tried (timeline)

| Date | Key change tested | Outcome at threaded ends & luer ports | Verdict |
|---|---|---|---|
| 26 Mar | First full assembly; PU glue + **cable ties**; luer stops on ends | Side ports wouldn't close (support-structure residue, temp-fixed with blue tac); leak at screwed ends; tape failed; parafilm reduced but dripped; **grease + parafilm → sealed** | Grease+parafilm only working seal |
| 8 Apr | Membrane → 1.8 cm; **elastic rings** instead of cable ties; side luers drilled out | Rings *block the area under the membrane* → glue can't distribute → worse bond; leaks at ends and drilled luers; grease + 2× parafilm sealed; **raised pressure → membrane–piece bond leaked** | Elastic-rings-during-cure is the wrong call |
| 23 Apr | **Cable ties during cure, removed after drying**; PTFE film on joints | PTFE alone didn't seal; grease + parafilm sealed; **raised pressure → no leak at ends or attachment** | Cable-tie-then-remove bond works under pressure ✅ |
| 8 May | **PTFE on the inside** of joints (vs outside) | PTFE only → leaks; PTFE + 1–2 parafilm → leaks; **PTFE + 3 parafilm → fully sealed under pressure** | Works but clearly impractical |

### Settled vs open
- ✅ **Settled:** Bond the membrane with **PU glue + cable-tie compression during cure, then remove the cable ties.** Use cable ties, *not* elastic rings, so glue fully wets under the membrane. This survives raised pressure.
- ❌ **Open (my design target):** the threaded joints and luer ports. Everything that seals them is grease/tape. **Direction: redesign these as integrated/glued/captured geometry** so they seal by design, not by manual sealant.

### Highest-leverage insight
The **threaded ends are also the load path** to the mechanical platform. They are simultaneously (a) the worst leak point, (b) the worst offender against "looks good" and "easy to assemble," and (c) the force-transmission interface. **Fixing the end-piece design addresses sealing, aesthetics, assembly, and mechanical attachment in one move.** This is where to spend design effort first.

---

## 6. Inherited problem 2 — Fibre potting (Priority 2)

### Goal
A fibre bundle potted into the printed piece such that: lumens stay **open** (perfusable), fibres stay **straight/aligned**, the pot **seals ICS from ECS**, the **support piece can be removed**, and the pot **survives post-potting stretching**.

### What's been tried (timeline)

| Date | Setup | Key findings |
|---|---|---|
| 24 Mar | 3 cores-removed fibres in a cut 3 mL syringe | Potting works; easy at n=3, flagged as harder at scale → *"may need a removable lid."* Viscosity is the knob: too thick won't wick between fibres; too thin → capillary flow *into* lumens |
| 8 Apr | 18 fibres, flexible sleeve + syringe injection | 8 cm length chosen; screw pieces still fit after cutting (no PU/membrane interference ✅); cross-sections ~15/18 and ~14/18 lumens open — majority patent, **but only 2 sections sampled** |
| 28 Apr | 15 fibres, membrane → 2.3 cm for alignment, cure upside-down to fight bubbles | Injection **pushes fibres sideways → curving**; **new air bubbles form during injection**; upside-down cure **failed — membrane bent under resin weight and tipped**; some resin influx into lumens |
| 28 May | 10 fibres, support structure, fibres tied both ends, 3 rings vs sagging, upside-down cure rigged straight | **Curving solved** (fixing both ends ✅); **even distribution** (no tilt ✅); **support piece still won't come out** ❌; **resin sagging persists** ❌; migration unclear |

### Open problems (what still needs solving)
- **Support-piece removal** — still impossible. Next ideas: grease the screwed part before potting; or **redesign to avoid the support entirely** (cf. the "removable lid" idea from 24 Mar).
- **Resin sagging** — persists. Next: shorten the support structure; revisit geometry/orientation.
- **Air bubbles during injection** — degassing + injection method.
- **Resin infiltration into lumens** — partly mitigated by squeezing/closing fibre ends; tune resin viscosity.
- **Resin migration along fibres** — still unclear; needs cleaner cross-section sampling to even measure.
- **Scale-up** — from ~10–18 fibres to 50–60, eventually hundreds.
- **Quantification** — currently 2 hand-counted cross-sections. Not statistically meaningful, and a prime automation target (see §7).

---

## 7. The test rigs — my engineering edge

This is the highest-value thing I bring to a lab that's been doing this **by hand**. Each loop's "test" half should output a number, logged automatically.

### Priority 1 rigs (build these first)
- **Pressure-decay / leak rig (the key one).** Seal the chamber, pressurise to a set point, close the valve, **log pressure vs time** with a pressure transducer + microcontroller (e.g. Arduino). A pressure drop = a quantified leak rate → directly comparable across designs. Cheap, fast, and turns the qualitative drip-test into a real metric.
- **Burst test.** Ramp pressure to failure, record the max. Pairs with the pump operating pressure to set a safety margin.
- **Cyclic loading rig.** Mount the chamber on a linear actuator (or the lab's uniaxial stage), cycle at the agreed strain/frequency, **count cycles automatically**, and run a pressure-decay check at intervals (e.g. every N cycles) to track degradation.
- **Combined endurance.** Chamber in the pump loop *and* on the cyclic rig, run for the target duration with continuous pressure logging; watch for membrane-bond delamination and slow leaks.

### Priority 2 readouts
- **Automated lumen counting.** Replace manual cross-section counting with image analysis (Fiji/ImageJ like Marie, or a Python/OpenCV script) to count open vs blocked lumens and measure alignment across *many* sections → a real patency %.
- **Fluid-passage / patency test.** Perfuse through the potted bundle, measure flow/pressure, confirm lumens are patent **and** the pot seals ICS from ECS.

> Building these rigs is also the most defensible "concrete, demonstrable result" to point to at the end of the summer — a measurement system the lab keeps using.

---

## 8. External inputs I must lock down (ask Marie / Mouthuy early)

These constrain the design more than anything in the requirements list. Get them before committing to geometry.

- [ ] **Pump operating pressure + flow rate** → sets pressure/burst test targets.
- [ ] **Mechanical platform interface** — mounting geometry, **stroke/displacement range**, frequency capability (uniaxial stage and/or the humanoid platform, Mouthuy 2022). This dictates the end-piece design.
- [ ] **Stimulation protocol** — strain %, frequency, target duration → sets the cyclic-fatigue KPI.
- [ ] **Culture duration** → sets the combined-endurance test duration.
- [ ] **Sterilisation method** (autoclave vs other) → affects resin and membrane material choice; confirm the current materials survive it.
- [x] **Inlet/outlet count — RESOLVED:** 2 pairs = 4 ports (independent ICS + ECS). See §2 and decision log.
- [ ] **Fibre-count target for this phase** (tens now → hundreds later) → bore size and potting volume.

---

## 9. Parked for later — but design so I don't foreclose them

From the "later with Marie" discussion. Don't build these now; just don't make them impossible.

- **Electrical stimulation.** Connects to the conductive PEDOT:PSS already in the fibre pipeline. **Leaving room for electrode ports costs nothing now** — keep it in mind when laying out the end-pieces.
- **Functional readout via pillars sensing displacement.** The classic muscle-on-flexible-posts force measurement: pillars deflect, you track displacement → contractile force. Displacement tracking is a **vision/sensing problem — squarely my territory**, and the most interesting potential demonstrable result. But it depends on a working, sealed chamber first.

> Keep both firmly in "later." Do **not** let them pull focus from Priority 1.

---

## 10. Formal design-criteria checklist

From `Design_criteria.docx`. Tick as each is met and verified by a test.

**Casing**
- [ ] Improved architecture via CAD + prototyping
- [ ] Integrates into an external mechanical loading system
- [ ] Transmits force from the loading system
- [ ] Easy chamber assembly
- [ ] Independent inlet/outlet pathways per compartment (intracapillary + extracapillary)
- [ ] Structural integrity during mechanical loading
- [ ] Leak-free operation + uniform flow during perfusion
- [ ] Sufficient space/geometry for potting and sealing

**Fibre potting**
- [ ] Reproducible potting workflow
- [ ] Easy incorporation of fibres into the casing
- [ ] Clean, consistent results
- [ ] Limited fibre curving + even resin distribution
- [ ] No resin infiltration into / migration along fibres
- [ ] Compatible with post-potting stretching
- [ ] Structural integrity during perfusion

---

## 11. Open questions & decisions log

**Open questions** (move to the decision log once resolved):
- Real cyclic target (strain / frequency / cycle count)?
- Sterilisation method and material compatibility?
- Architecture: multi-part + membrane vs monolithic flexible print vs fully flexible?
- Is the support structure kept (and made removable) or designed out entirely?

**Decision log**

| Date | Decision | Rationale |
|---|---|---|
| 26 Jun 2026 | Chamber uses **2 flow circuits = 4 ports** (2 in, 2 out): ICS through the fibre lumens (axial), ECS through the shell space (side). | Standard dual-circuit HF-bioreactor design; matches the design-criteria requirement for independent pathways per compartment. Implementation / form factor deliberately left open. |
| | | |

---

## 12. Progress log

| Week / date | Focus | Done | Blockers | Next |
|---|---|---|---|---|
| Jun–Jul (ramp-up) | Build P1 test rig(s); lock down §8 numbers | | | |
| | | | | |
