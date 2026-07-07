# Route to MSc @ Oxford — Living Strategy Document

> **Single source of truth** for the goal: securing an **Oxford research degree** (MSc by Research, upgradeable to DPhil) with a **core in ML-based control for compliant / embodied robotic systems**, the **tendon-driven humanoid bioreactor as the flagship testbed**, and a parallel **startup track** (the safety layer for "physical AI").
>
> This is a *living* document. Add ideas, meeting notes, and decisions as they arise during the Oxford internship. It builds toward a **bulletproof plan for how and when to approach supervisors** with a research proposal, and **which department / funding / founding route** to take.
>
> ⚠️ It does **not** yet contain a dedicated research proposal — that is built separately over time (§7 scaffold), fed by the lab needs-finding in §6 and the thesis-seed directions in §7.

**Last updated:** 2026-06-30 · **Owner:** Marcel · **Status:** Active — internship phase

### How to use / update this doc
- Treat §2 (North Star), §3 (Principles) and §4 (Why me) as **stable**; revise rarely.
- Drop new ideas into §5 (directions), §6 (needs-finding), §12 (open questions), or §13 (action items).
- Run any "completely different" idea through the **two-question filter** in §8b before acting on it.
- Log every meaningful change in §16 (Changelog) with a date.
- Placeholders for your input are marked `>> [ ... ]`.

---

## 1. Snapshot (update freely)

- **Where I am now:** Research internship at NDORMS / Mouthuy lab, Oxford — building the soft hollow-fibre bioreactor chamber (Marie Kruth's DPhil). Mouthuy has transferred to **Materials**; his lab is increasingly working with humanlike / tendon-driven robotics.
- **Research core (recentred):** **safe/stable learning-based control for compliant / embodied robotic systems** — my passion *and* sharpest edge, and Furieri's exact methods. The **humanoid bioreactor is the flagship testbed** (Mouthuy co — advantage, internship value, novel compliant-control platform all retained), **not the point**.
- **Furieri fit — methods confirmed on paper.** His theme *"Learning-Based Control with Closed-Loop Guarantees"* (NN controllers for nonlinear systems; RL policy parametrizations; guarantees *by construction*) maps almost word-for-word onto the tendon-driven problem, with a specific **port-Hamiltonian / energy-based bridge** (§10f).
- **Supervisor model:** **Furieri (ES primary) + Mouthuy (co)**; degree = **apply to the funded DPhil in Engineering Science**, decide MSc-vs-DPhil at transfer. **PhD-vs-MSc is resolved** — the self-funded MSc(R) as a *destination* is dominated (§9f).
- **Startup (crystallised):** the **safety / stability layer for learned control of compliant ("physical AI") robots** — a hardware-agnostic control-software layer, portable off the bioreactor (§11). **Founding path: root in the UK (Oxford spinout + strong PhD-founder visas), expand into the US.**
- **Two things NOT yet settled (research):** (1) confirm Furieri wants to aim these methods at a **robot** (his testbeds are infrastructure); (2) **name the novel thesis contribution** — methods-fit ≠ thesis (§7).
- **Key hurdle:** funding (international fees + average grades) — target supervisor-grant + German funding, not merit scholarships (§9c).
- **Hard deadline:** **December 2026 / January 2027** scholarship round for **2027-28 entry**.
- `>> [ current top-of-mind note: ... ]`

---

## 2. North Star

Get admitted to an **Oxford research degree** on a project whose core is **ML-based control for compliant / embodied robotic systems**, that:
1. Sits genuinely at **robotics + embodied AI + learning-based control with guarantees**.
2. Uses the **tendon-driven humanoid bioreactor as its flagship testbed** (retaining my unfair advantage).
3. **Maximises admission odds** via my advantages + warm supervisors (Furieri + Mouthuy).
4. **Keeps the DPhil option open** — apply to the DPhil, decide MSc-vs-DPhil at transfer (§9).
5. **Keeps a startup path open** on the control-software layer — **UK-rooted, US-expansion** (§11).

Robotics/control anchor + credential home: **Prof. Furieri** (Engineering Science). Platform/domain anchor: **Prof. Mouthuy** (Materials). Department leaning **ES**, formally decided at application.

Secondary / backstop: US/EU PhD programmes (MIT Raman Lab, UIUC, Northwestern, EPFL, TU Delft) as later-stage alternatives.

---

## 3. Guiding principles (hard-won, keep visible)

- **The core is the control; the biology is the application.** My passion *and* edge is ML control for compliant/embodied systems. The humanoid is the **flagship testbed, not the point** (more convergent on my edge, not less).
- **The Devanthro connection is my single strongest differentiator** — attached to the **project and the people**, not the department; it survives an ES registration intact (§10a).
- **Safe-by-construction, not post-hoc.** On a compliant robot driving a tissue chamber, a learned controller cannot occasionally wander unstable — it would damage the tendons or the culture. Guarantees-*by-construction* are **operationally necessary** here — and, not coincidentally, the **core of the startup** (§11a).
- **Methods-fit ≠ thesis.** Finding the paragraph on Furieri's site that matches my system is easy; the **novel contribution is what I *add*** (§7).
- **Converge, don't diffuse.** Depth that compounds beats breadth that diffuses. Pick and go deep on the robotics-control core.
- **The friendship strengthens the bet — it does not replace it.** Furieri's methods map *onto* my platform's control problem; knowing him argues for going *deeper* on the robot.
- **Protect the Furieri friendship — don't instrumentalise it.** Let it be real; read his work; let the supervision conversation *emerge* via a peer-level technical exchange (§10f).
- **Startup = founder–market fit, not topic heat.** The startup rides the **control-software layer** (my edge), not bio (slow/regulated/capital-heavy) and not Furieri's energy/industrial domains (not my edge).
- **Stay Pierre-anchored via the testbed** — keeps Mouthuy as co, the admission advantage, and the internship's compounding value.
- **Let the platform's shared pain define the application problem** (§6). My unique value is *translation*.
- **The internship is maximised when it *compounds into* the degree** — show Pierre my robotics/control thinking, not just bench diligence.
- **The credential label is second-order; the work is first-order.** Thesis + publications + the system I built define me. (And publications double as **immigration + fundraising assets** — §11c.)
- **27 is not late — and a funded PhD is not "lost time."** The average high-growth-startup founder is ~45, and success rates rise with age well into the 40s; finishing a deep-tech PhD at ~31 with a technical moat, network, IP, and O-1/DeepMind credibility is *young*, not behind. The PhD **builds the company's foundation while I'm paid**, and can *incubate* the startup rather than merely precede it (§9f).
- **Optionality:** prefer moves that keep multiple futures open (academic + entrepreneurial; MSc + DPhil; UK + US).

---

## 4. Why me — unfair advantages (candidacy spine)

- **I helped build the exact robot.** At **Devanthro**, I worked on the humanoid (tendon-driven, series-elastic) platform.
- **My BSc thesis is the empirical seed of the PhD.** An **RL/ANN-based control algorithm for this exact tendon-elastic hardware**, tackling nonlinear control under tendon elasticity. The arc: **BSc = make it work empirically; PhD = make it *provably* work** (stable by construction — §10f).
- **The lab's humanoid bioreactor *is* a modified Devanthro shoulder joint.** Mouthuy et al. (2022, *Communications Engineering*) has **Rafael Hostettler / Devanthro as a co-author** → industrial continuity.
- **My current internship work is the physical interface** between the eHF muscle tissue and that robot.
- **This advantage survives an ES registration** (§10a) and is what makes me competitive for an ES place despite average grades — I arrive with a de-risked, ready-to-run, methodologically-matched **testbed**.

---

## 5. Candidate research directions (core recentred; selection driven by §6 + §7)

**Research core = safe/stable learning control for compliant/embodied robotic systems.** The humanoid bioreactor is the flagship testbed; direction **A** is the lead. Any *new* "completely different" idea must pass the §8b two-question filter.

| ID | Direction (short) | One-line description |
|----|-------------------|----------------------|
| **A** *(lead)* | Closed-loop, guaranteed-stable RL control of the humanoid bioreactor | NN/RL controller for the tendon-elastic system with **closed-loop guarantees by construction**; precise programmable strain + tissue-responsive feedback. The methods core; the bioreactor is the testbed. |
| **B** | Robotic automation of fibre potting & chamber assembly | Deformable-object handling + vision QC; direct extension of the internship. |
| **C** | Vision-based contractile readout + autonomous drug/geroprotector screening loop | Longevity bridge: muscle as a sarcopenia model. |
| **D** | Smart point-of-care cell-therapy manufacturing bioreactor | Closed-system, AI process control + vision QC. |
| **E** | Biohybrid actuators / muscle-powered robots | "Robotics + tissue engineering," most literal sense. |

- **Defensibility:** **A › B › C › D › E**
- **Startup potential (of the *application*):** **D › C › A › B › E** — but the startup thesis rides the **domain-general control-software layer**, not any single bio application (§8a, §11).
- **Bottom line:** lead with **A** as the flagship testbed for the control core. **B is the fallback** if the lab's shared pain is assembly/reproducibility. §6 sharpens the application; §7 names the novel contribution.

`>> [ new direction ideas — run through §8b filter first: ... ]`

---

## 6. Lab needs-finding (sharpens the application problem)

**Goal:** interview everyone, understand each project's interaction with the robot, and surface the **highest-value problem in the shared control / stimulation / feedback layer** — my lane. A well-defined, control-flavoured shared problem is the **natural bridge project to bring to both Furieri and Mouthuy**, and the lab are my **first "users"** → shared pain = early market validation for the control-software layer (§11).

### Interview template (ask everyone the same core set)
1. **What mechanical regime does your tissue need, and why that one?** *(principled vs guessed)*
2. **Walk me through running a stimulation session today, start to finish.** *(workflow friction)*
3. **Where does the platform limit you — what do you babysit, redo, or work around?** *(pain / automation openings)*
4. **How do you know the stimulation did what you intended — what do you measure, and when?** *(the feedback gap)*
5. **If the robot could do one thing it can't today, what would it be?** *(latent demand)*

> Q1 & Q4 most likely surface the control-shaped problem: fixed/guessed regimes with no tissue feedback = the open-loop gap my (guaranteed) closed-loop control closes.

### Guardrails
- **Stated wishes ≠ real needs** — capture the raw complaint *and* my translation into a control problem.
- **Don't pre-decide** — log pains pointing *away* from embodied control (→ direction B).
- **Stay in the shared control/feedback layer**, not anyone's specific biology.
- **Loop Pierre in early** — reads as platform-mapping, not stealth.

### Synthesis table (running — add a row per conversation)

| Person | Project / tissue | How they use the platform | Pains & workarounds | Stated wishes | My translation → candidate problem | Generalises to other labs? |
|--------|------------------|---------------------------|---------------------|---------------|-----------------------------------|----------------------------|
| `>> [ ]` | | | | | | |
| `>> [ ]` | | | | | | |

### Emerging patterns
- `>> [ shared problem #1: ... ]`
- **Working hypothesis of the highest-value problem:** `>> [ ... ]`

---

## 7. Research proposal — TO BE BUILT (scaffold + thesis-seed directions)

*No proposal drafted yet. The application problem comes from §6; the **novel contribution** is named below (methods-fit ≠ thesis).*

**Thesis-seed directions (the "what's genuinely new"):**
- **Extend guaranteed-stable learning-control to the specific structure of tendon-elastic actuation** — the nonlinearities and *coupling* of a multi-tendon, series-elastic system. Elastic energy storage makes **energy-based / passivity / port-Hamiltonian** formulations a natural fit (aligns with Furieri's port-Hamiltonian work — §10f).
- **Guarantees under a *changing* plant.** As tissue develops and mechanically feeds back, the plant changes; making closed-loop guarantees hold under this drift is novel, hard, and platform-motivated.
- `>> [ refine / add candidate contributions: ... ]`

**Checklist a strong proposal must satisfy:**
- [ ] **Original research question** — a novel *contribution* (above), not just "his controller class fits my system."
- [ ] Clear **unsolved problem** (open-loop, imprecise, feedback-free stimulation on compliant hardware; no safe-by-construction learned controller).
- [ ] **Robotics/control novelty pitched to Furieri** — safe/stable learning control of a nonlinear compliant system; my platform as a novel testbed; the port-Hamiltonian angle.
- [ ] **Why me** (§4), framed around the science.
- [ ] **Feasible scope** + milestones (§9).
- [ ] A **demonstrable result** ≥ MSc-R bar with a path to the DPhil bar.
- [ ] **Supervisors + fit** (Furieri primary + Mouthuy co).
- [ ] Honest **risk/contingency** note.

`>> [ proposal drafts / fragments here when ready ]`

---

## 8. Strategic framing notes (reference)

### 8a. Discovery instrument vs product / where the startup lives
The **humanoid = the "wind tunnel"** where control intelligence is discovered/validated; it never scales as a product. The **commercial asset = the learned, guaranteed-stable control-software / policy layer** — hardware-agnostic and portable across compliant/contact-rich robots. The DPhil generates the IP + credibility; the startup commercialises the software layer (full thesis in **§11**).

### 8b. The two-question filter (run any "completely different" idea through this)
- (a) Does it excite me **more**, *sustainably* — not just today?
- (b) Do I have a **defensible edge**, or am I starting from zero?
- **Both yes → stress-test it.** Either no → shiny-object syndrome in a lab coat.

### 8c. Startup reframe
Startup success tracks **unfair founder–market fit**, not topic trendiness. The startup rides my edge (robotic control software), not bio (slow/regulated/capital-heavy) and not Furieri's energy/industrial domains (not my edge).

### 8d. "Directly helps people" split (reference)
- **Therapeutic device** (bioartificial liver/kidney, hollow-fibre based — my expertise): most literal help but a 10–15-yr regulatory path, startup graveyard. Long-horizon ambition, not an MSc-to-startup play.
- **Smart manufacturing** (direction D): better fit than a device, still slower than a control-software play.
- Reference facts: manual CAR-T ~$400k/patient, labour ~40%, 2–5% contamination, automation → ~$100k; CGT manufacturing market ~$26.6B by 2035.

### 8e. Converge, don't diffuse — three concentric options (ranked)
1. **Robotics-control core, humanoid bioreactor as flagship testbed — Furieri (primary) + Mouthuy (co).** Passion + edge + advantage + clean ES credential. **Strongest.**
2. **Furieri-anchored control project, application broadened, no Mouthuy.** Keeps Luca + control skill; drops the platform advantage.
3. **A completely different topic (e.g., Furieri's grid/industrial domain), neither advantage nor passion.** No moat. **Weakest.**

### 8f. Recentring — three "optimise-for-X" disentangled
1. **My passion + edge → robotics / embodied control.**
2. **Furieri's hottest markets → grid / transport / industrial reliability.** Fundable, and where his entrepreneurial energy is — but a domain I have *no edge in* (the founder–market-fit trap).
3. **My admission advantage → the bio/Mouthuy platform.**
**Resolution:** center on **(1)**; keep the humanoid as the flagship **testbed** to retain **(3)**; point the startup at the control-software layer.

### 8g. The startup rarely falls straight out of the PhD topic
It comes from skills, network, an entrepreneurial supervisor, a hot fundable area, and a problem found along the way. Furieri gives me world-class ML-control training, an entrepreneurial mentor, and a network *regardless* of the exact topic. **Don't over-engineer the "perfect startup topic" now** — optimise for capability + fit + mentor; let the venture crystallise during the PhD (§11e).

---

## 9. The Oxford research-degree path: structure, duration & funding

### 9a. PRS → transfer → confirmation
Every research student starts as a **Probationer Research Student (PRS)**. **~End of year 1 (by the 4th term, max 6th)**, **Transfer of Status** decides **MSc by Research** ("worthwhile contribution") vs **DPhil** ("significant and substantial contribution"), assessed by two non-supervisor faculty + oral. DPhil then requires **Confirmation of Status** (~9 terms).

### 9b. The three degree shapes (clearing up the "1-year MSc" myth)
- **Taught MSc — ~1 year.** *This* is the 1-year master's students mean — no research project, no platform, no supervisor relationship, no DPhil path. ES barely offers taught MScs. **Not the target.**
- **MSc by Research — normally 2 years** in ES and Materials (thesis within 2, at most 3). A "1-year MSc by Research" is **not** an admission route here.
- **DPhil — 3–4 years** realistically (3 is the floor). *Not* "only 3."

### 9c. Funding reality (flips the naive logic)
- **The MSc by Research is rarely funded** — most studentships/scholarships target *doctoral* study. A 2-year MSc(R) usually means **self-funding at ~£33,370/year international fees + ~£17–25k/year living = well north of £100k over two years.**
- **The DPhil is where the funding is.** So the *longer* degree is the more financially accessible one.
- **Grades caveat:** supervisor backing carries *admission*; competitive scholarships (Clarendon, DTPs) weight grades — my weak spot. **Don't bank on those.** Target instead:
  - **Supervisor/grant-attached studentships** (the PI selects; fit + backing outweigh grades). Plays to Furieri/Mouthuy.
  - **External German funding** — DAAD, Studienstiftung, etc.
- **Caveat:** a DPhil studentship + early MSc exit can have funding-contract implications — known, non-catastrophic, but a bridge to be aware of.

### 9d. The resolution — apply to the DPhil, decide at transfer
Both routes start as PRS. So **apply to the DPhil**: (a) unlocks funding the MSc(R) can't access, and (b) still contains the **MSc by Research as a genuine early exit** if the startup pull wins. The **transfer point (~1 year in) is the real fork.**

### 9e. Timing & deadlines
- Both departments **closed for 2026-27, open for 2027-28** — fits the timeline (internship wraps ~Sept 2026).
- Because funding is the real hurdle, the **hard deadline is the December 2026 / January 2027 scholarship round.**
- Furieri recruits via the **DPhil in Engineering Science**, ~early-December deadline for October entry.

### 9f. PhD vs MSc — RESOLVED (stop re-litigating)
**Decision: apply to the funded DPhil. The self-funded MSc by Research as a *destination* is off the table.** Why the dilemma dissolves:
- **The MSc(R) is the *dominated* option.** It costs **~£100k out of pocket** (rarely funded), gives a **thinner foundation** (2 years, less depth, fewer publications, less IP), *and* saves only **~1.5 years**. Paying six figures for a weaker result, slightly faster, is a bad trade when optimising time *and* money toward a company.
- **Two corrections to common (lab) advice:** budget the DPhil at **3.5–4 years**, not "only 3" (3 is the floor); and the "1-year" option is a **taught MSc** — a different degree with no research, no platform, no supervisor relationship. The *research* MSc is 2 years. The 1-year idea is a mirage.
- **So the real choice is only: funded DPhil vs. skip a degree entirely** and go straight at a frontier company / founding.
- **You don't even decide that upfront.** Apply to the funded DPhil; at **transfer of status (~end of year 1)** either continue (if it's compounding) or **exit with an MSc by Research — earned *while paid*, not for £100k.** Applying to the DPhil buys the option value of both, with a real decision gate one year in (when I'll know if the research is working, Furieri is great, the venture is crystallising, DeepMind is calling). Applying ≠ locking into four years.
- **The one condition that actually decides it (self-assessment — Q12):** all of this assumes I genuinely want to *do the research*. If yes → the funded DPhil is clearly best. If I'm honestly lukewarm and just want to build fast → **don't do any degree**; a PhD I don't want is a miserable multi-year slog, funded or not. The deciding question isn't money or time — it's internal.

### Indicative 2-year shape (works as terminal MSc *or* DPhil years 1–2)
- **Year 1 (to transfer):** implement a **guaranteed-stable learning controller** for the shoulder bioreactor; validate **precise, programmable strain**; integrate a **real-time tissue readout**; close the loop. → clears MSc-R.
- **Year 2:** show **adaptive closed-loop control beats fixed scripts**; demonstrate guarantees under the developing plant / a learned new regime. → DPhil-scale if continuing; strong terminal MSc-R + startup IP if exiting.
- **Headline result:** *a provably-stable, RL-driven humanoid bioreactor that autonomously improves muscle function over scripted stimulation.*

---

## 10. Department & supervision strategy

### 10a. The advantage is attached to the project + people, NOT the department — three layers
- **Department** = where I'm registered / the parchment → credential-legibility lever (reason to prefer ES).
- **Project** = the humanoid bioreactor (my edge: built the robot; thesis = its control seed) — doesn't change with the department.
- **Supervision** = Furieri (ES primary) + Mouthuy (co). My Pierre-lab experience is an edge relative to *Mouthuy* — who stays on the team.
→ **In the ES route I keep the advantage *and* gain the label.** Change the container, keep the contents.

### 10b. The two routes

| Route | Home dept | Supervisor model | Credential | Admission odds | Notes |
|-------|-----------|------------------|------------|----------------|-------|
| **ES-home** *(current lean)* | Engineering Science | **Furieri = primary**, Mouthuy = co | **Research degree in Engineering Science** — clean robotics label | Strong; Furieri decides, won via the *project + methods fit* | De-risked by the relationship + confirmed methods fit. Advantage preserved via Mouthuy co + platform-as-testbed. |
| **Materials-home** *(fallback)* | Materials | **Mouthuy = primary**, Furieri/ORI = co | Research degree in Materials | **Highest** — Mouthuy alone can wave me in | Label weaker for robotics but recoverable via thesis + publications. |

### 10c. Settled strategy
**Robotics-control core; humanoid as flagship testbed; Furieri (ES primary) + Mouthuy (co); apply to the DPhil in Engineering Science; decide MSc-vs-DPhil at transfer.** ES is the current lean; Materials the fallback if Furieri's robotics appetite doesn't firm up.

### 10d. The honest tradeoff
The advantage is **most potent for admission in the Materials route** (Mouthuy alone suffices). In ES it's marginally less of a slam-dunk on *admission* — but the **credential is better**. A good, conscious trade.

### 10e. Don't shop — bring your own project
With a warm supervisor I **bring and co-develop my own project**, not pick from a menu. The department follows from the project + supervisors; it is not a substitute for choosing them.

### 10f. Luca Furieri — profile, methods fit & relational guidance
- **Who:** Associate Professor, **Engineering Science** (joined 2025); Tutorial Fellow, **St Hugh's**; ex-EPFL PI (Ambizione), PhD ETH Zurich. In **Oxford's Control Group** (with Antonis Papachristodoulou) — **not** ORI. Entrepreneurially engaged (EPFL startup ecosystem).
- **Methods (his):** learning-based control with **formal stability/safety guarantees** — stability-constrained RL ("MAD"), neural system-level synthesis, distributed control, learning-to-optimize, **port-Hamiltonian NN control with dependability guarantees**.
- **Application domains (his):** safety-critical infrastructure — **electricity grid, automated transportation, networked systems, industrial reliability.** *(Seam: his testbeds are infrastructure, not robots or bio.)*

**Methods fit — confirmed on paper (the strong axis):**
- His theme *"Learning-Based Control with Closed-Loop Guarantees"* — **NN controllers for nonlinear systems, RL policy parametrizations, guarantees built into the controller class *by construction*** — maps almost word-for-word onto the tendon-driven problem.
- **The arc:** BSc tackled the tendon-elastic nonlinearity *empirically* and hit the stability wall; his framing is the *rigorous* version — stable **by construction**.
- **Specific bridge — port-Hamiltonian / energy-based.** Tendon elasticity is *stored energy* → passivity / port-Hamiltonian formulations are a natural fit, and he's worked on exactly that. The fit is *specific*, not just thematic.
- **Operationally:** a learned controller on a compliant robot **cannot** occasionally go unstable → safe-by-construction is *necessary* (and the startup's core — §11a).

**Still NOT settled:**
1. **Does he want to aim these methods at a *robot*?** His testbeds are infrastructure. A matching paragraph ≠ appetite — only a real conversation settles it.
2. **Methods-fit ≠ thesis.** The novel contribution is what *I add* (§7).

**Relational guidance:** keep it a **real friendship**; don't rush; read his work. The unlock now is a **peer-level technical opening**, e.g.: *"I spent my BSc doing RL control of a tendon-driven system and kept hitting the stability wall empirically; your closed-loop-guarantees framing is the rigorous version of what I was fumbling toward — and I suspect the elastic-energy structure is a natural fit for the port-Hamiltonian angle."* Probes his robotics appetite (open Q) in the same move.

### 10g. Supervisor / co-supervisor candidates

| Candidate | Role in plan | Group | Why | Status |
|-----------|--------------|-------|-----|--------|
| **Prof. Luca Furieri** | **ES primary** *(lead)* | Control Group, Eng Sci | Learning control w/ closed-loop guarantees — confirmed methods fit; warm relationship; startup-savvy | Friendship forming (tennis) |
| **Prof. Pierre-Alexis Mouthuy** | **Co** (+ Materials-home primary) | Materials / NDORMS | The platform/testbed, the domain, the Devanthro advantage | Internship supervisor |
| **Prof. Perla Maiolino** | Optional ORI co | Soft Robotics Lab (ORI) | Soft/compliant systems + force sensing (if sensing/soft-robotics becomes central) | Not contacted |
| **Prof. Ingmar Posner** | Optional (RL) | Applied AI Lab (ORI) | Robot learning / RL; startup founder (Oxa) | Not contacted |
| **Prof. Hua (Cathy) Ye** | Biomedical bridge co | Eng Sci / IBME *(verify)* | Already Marie's co-supervisor; tissue eng + bioreactors | Known via lab |

Furieri makes Maiolino/Posner **optional**. **Skip the CDTs** (AIMS, RAINZ): cohort-based, committee-admitted, DPhil-locked, thematically off.

`>> [ notes from conversations with Furieri / Pierre: ... ]`

---

## 11. Startup & founding path

### 11a. The venture thesis (crystallised)
One line: **a software layer that makes *learned* controllers *provably safe and stable* on *compliant, contact-rich* robots — the safety / certification layer for "physical AI."**
Why now: the humanoid / manipulation / cobot wave has a well-known bottleneck — learned policies are powerful but brittle and unsafe on real hardware; on compliant/contact-rich systems, instability = damaged hardware or an injured person. Furieri's *"guarantees by construction"* is exactly that missing layer. The commercial asset is the **hardware-agnostic control-software / policy layer**, lifted off the bioreactor onto any compliant robot (§8a).

### 11b. Two wedges (decide during the PhD — §11e)
- **Horizontal — "guardrails for physical AI":** an SDK / middleware robotics companies license to deploy learned policies on compliant hardware with stability guarantees. Biggest TAM, rides the current funding frenzy, software margins.
- **Vertical (my sharpest edge) — human-interactive / medical-adjacent compliant robotics:** exoskeletons, prosthetics, surgical/assistive robots, human-safe cobots — where safe-by-construction is non-negotiable and worth paying for, and where my unusual combination (humanoid musculoskeletal robotics + tissue/bio + guaranteed control) is a differentiated founder story almost no one else can tell. Vertical = clearer first customer + regulatory moat.

### 11c. How the PhD manufactures the company
- **Moat / IP:** the portable guaranteed-control layer (patented via **Oxford University Innovation**).
- **Demonstrator:** the humanoid bioreactor proves it on a real compliant system — a fundable proof point.
- **Credential + network:** Oxford + **Furieri** (entrepreneurial supervisor / door-opener) + Oxford's spinout & deep-tech-VC ecosystem + **Mouthuy's medical network** (for the vertical).
- **Bonus — the two paths reinforce each other:** the **publications + Oxford doctorate are themselves the evidence base for the founder visas** (§11d). Research output = immigration + fundraising assets.

### 11d. UK or US — root in the UK, expand into the US
**The UK is the natural, lowest-friction base** (IP is Oxford-rooted, network is here, founder-immigration favourable for an Oxford PhD grad):
- **Graduate visa** — PhD grads get **3 years, no sponsor**, to start a business (a runway to test the model).
- **Global Talent visa** — no sponsor, no business plan, full company ownership, **settlement in 3 years**; natural fit for an Oxford doctorate + publications.
- **Innovator Founder visa** — **no minimum investment**, ILR in 3 years; since Nov 2025 you can switch in from the Graduate route without leaving.
→ Can start the company *during or right after* the PhD without leaving.

**The US is the bigger market / deeper capital — expand into it, don't found in it:**
- **O-1A (extraordinary ability)** — preferred founder route (no cap, no lottery, high approval); since Jan 2025 a **founder-owned company can petition for its owner**. A strong Oxford PhD + publications is exactly this profile.
- **E-2 (treaty investor)** — open to me as a **German** national (Germany is an E-2 treaty country).
- **L-1 (new office)** — if founded in the UK first, transfer myself in to open a US arm: the clean **"expand, don't relocate"** route.
- **International Entrepreneur Parole** — labelled for founders but a **fragile backup**: discretionary parole (not a visa), high funding thresholds, only a couple dozen approvals ever. Don't build the plan around it.
→ Founding *directly* in the US as a German with Oxford IP is higher-friction on every axis. UK-root / US-expand is also how most European-R&D deep-tech scales.

### 11e. What to set up now (years out — this is about optionality)
- **Keep the IP position clean** and **understand Oxford's spinout terms early** (they've become more founder-friendly recently). Furieri has navigated this — get his read on **spin-out vs licence**.
- **Treat every publication / award as an immigration *and* fundraising asset** — build the O-1A / Global Talent evidence base deliberately.
- **Let the wedge (horizontal vs medical vertical) crystallise** from the research + lab needs-finding (§6) — don't fix it prematurely (§8g).
- Don't force the company early; it can begin *during* the PhD, but the ingredients (moat, demonstrator, network) come first.

`>> [ startup notes / customer conversations / investor contacts: ... ]`

---

## 12. Open questions / decisions to resolve

| # | Question | Notes | Status |
|---|----------|-------|--------|
| 1 | Application problem to anchor A? | From §6 needs-finding. | In progress (§6) |
| 2 | ES-home vs Materials-home? | **Lean ES** (Furieri). Fallback Materials. Formalised at application. | Leaning ES |
| 3 | Apply to DPhil or MSc(R)? | **RESOLVED — apply to the funded DPhil.** MSc(R) as a *destination* is dominated (~£100k, thinner, saves only ~1.5 yrs); decide MSc-vs-DPhil at **transfer** (§9f). | Resolved |
| 4 | Funding source? | Target **supervisor-grant + German funding**, not merit scholarships. **Critical.** | Open — high priority |
| 5 | **Does Furieri want a *robotics* application?** | His testbeds are infrastructure. Probe via the peer-level conversation (§10f). | Open — key |
| 6 | **What is the novel thesis contribution?** | Methods-fit ≠ thesis. Seeds in §7. | Open — key |
| 7 | **Startup wedge — horizontal safety-middleware vs medical/human-interactive vertical?** | Crystallise from research + needs-finding (§11b, §11e). | Open — later |
| 8 | **IP — Oxford spinout vs retain/license?** | Understand Oxford's terms early; get Furieri's read (§11e). | Open — later |
| 9 | Founding geography? | **UK-root, US-expand** (§11d). | Resolved (lean) |
| 10 | Demonstrable internship result I'll point to? | Must show robotics/control thinking. | Open |
| 11 | Degree class clears the ES bar (strong 2:1 equiv)? | Verify German-grade mapping. | Open — verify |
| 12 | **Do I genuinely want to *do the research* — or just hold the credential?** | The gate that decides degree-vs-skip-degree. If lukewarm → skip the degree, go straight at a frontier company / founding (§9f). | Open — self-assessment; **decisive** |

---

## 13. Action items (near-term)

- [ ] **Read Furieri's work** — the *closed-loop guarantees* theme, the stability-constrained RL ("MAD") paper, the **port-Hamiltonian NN control** paper — enough to engage as a peer.
- [ ] **Open a peer-level technical conversation with Furieri** using the BSc-stability-wall → closed-loop-guarantees opener (§10f): deepens the friendship *and* probes his robotics appetite (Q5).
- [ ] **Name the novel thesis contribution** (Q6) — develop the §7 seeds.
- [ ] **Run the lab needs-finding (§6)**; loop Pierre in.
- [ ] **Showcase robotics/control thinking to Pierre** via a concrete demo linking my RL/tendon-control background to the platform.
- [ ] Confirm **KPI specifics** with Marie; build the **quantitative test rig** before iterating designs.
- [ ] **Map funding:** DAAD / Studienstiftung timelines + eligibility; supervisor-grant/studentship options with Furieri/Mouthuy.
- [ ] **Understand Oxford's spinout terms** + spin-out-vs-license, with Furieri's input (§11e).
- [ ] **Build the immigration/fundraising evidence base deliberately** — treat publications/awards as O-1A / Global Talent assets (§11c–d).
- [ ] **Verify** ES + Materials research-degree deadlines for 2027-28 and the **Dec 2026 / Jan 2027** scholarship deadline.
- [ ] **Verify** my degree class maps to a strong 2:1 equivalent.
- [ ] Run any **"completely different"** idea through the **§8b two-question filter** first.

---

## 14. The approach plan (how & when to approach Pierre + Furieri)

**Phase 1 — Now → mid-internship (earn the right + gather evidence):**
- Deliver technical work that **shows robotics/control thinking**, not only bench diligence.
- **Run the needs-finding (§6)**, Pierre looped in.
- **Let the Furieri friendship develop**; read his work; open the **peer-level technical conversation** (§10f) — listen for his robotics appetite (Q5).

**Phase 2 — Mid → late internship (open the conversations):**
- Informal chat with Pierre: interest in continuing into an Oxford research degree, framed around the **robotics-control core + §6-validated application** + my background. Ask him to **co-supervise** and his ES-vs-Materials preference.
- With Furieri, let the supervision question **emerge** from the technical exchange once mutual interest is clear.

**Phase 3 — Late internship (firm up):**
- **Connect Furieri + Mouthuy** around a project both find compelling.
- Lock **application problem, novel contribution, department (lean ES), route (DPhil), funding plan**.
- Begin drafting the **proposal** (§7).

**Phase 4 — Application (2027-28 cycle):**
- Apply to the **DPhil in Engineering Science** (Furieri primary + Mouthuy co), **by the December 2026 / January 2027 scholarship deadline**.
- Submit funding applications (supervisor-grant + German bodies).
- Keep the **MSc-at-transfer** option explicit.

**Principles:** supervisor-led admission ⇒ warm supervisors are the lever; a peer-level/organic intro >> a cold one; lead with **science + platform**; **bring my own project** (§10e).

`>> [ running notes on conversations / commitments: ... ]`

---

## 15. Sources & reference links (for verification)

**Oxford structure / degrees / funding**
- Research courses & transfer — ox.ac.uk/admissions/graduate/courses/research-courses
- Getting started (taught vs research; DPhil 3–4 yrs; scholarship deadlines) — ox.ac.uk/admissions/graduate/courses/getting-started
- MSc by Research in Engineering Science (2-yr; ES primary supervisor rule; ~£33,370 intl fee; open 2027-28) — ox.ac.uk/admissions/graduate/courses/msc-research-engineering-science
- MSc by Research in Materials (normally 2 yrs; open 2027-28) — ox.ac.uk/admissions/graduate/courses/msc-research-materials
- DPhil in Engineering Science — ox.ac.uk/admissions/graduate/courses/dphil-engineering-science
- Oxford IP policy & **Oxford University Innovation** (spin-outs) — innovation.ox.ac.uk
- German funding: DAAD (daad.de), Studienstiftung (studienstiftung.de)

**Furieri / supervisors**
- Luca Furieri — Oxford Engineering Science profile — eng.ox.ac.uk/people/luca-furieri/
- Furieri research page (**"Closed-Loop Guarantees"** theme) — lucafurieri.it/research.html
- Furieri domains (grid + automated transport) — actu.epfl.ch (SNSF Ambizione)
- Port-Hamiltonian angle — "Distributed Neural Network Control with Dependability Guarantees: a Compositional Port-Hamiltonian Approach" (nccr-automation.ch / arXiv)

**Startup / founder immigration & spin-outs**
- UK Graduate visa (3 yrs for PhD), Global Talent, Innovator Founder — gov.uk/browse/visas-immigration/work-visas ; davidsonmorris.com (Innovator Founder / Start-up 2026 guides)
- US founder options (O-1A, E-2, L-1 new office, IEP) — uscis.gov (International Entrepreneur Rule) ; tryalma.com (founder-visa guides 2026)
- Oxford spin-out terms / UK university spin-out reform — innovation.ox.ac.uk ; (TenU USIT guide) — *verify current terms*

**Domain / market**
- CAR-T cost & automation — vocal.media (2026); Frontiers Bioeng. Biotechnol. (2026)
- CGT manufacturing market (~$26.6B by 2035) — biospace.com

**Lab / project**
- Mouthuy et al. (2022), *Communications Engineering* 1:2 — doi:10.1038/s44172-022-00004-9 (Hostettler/Devanthro co-author)
- Marie Kruth, DPhil Transfer Report (project file)

---

## 16. Changelog

- **2026-06-30 — Document created.** North Star, principles, "why me", five-direction menu, strategic framing, Oxford pathway + 2-year shape, co-supervisor shortlist, open questions, action items, approach plan. Proposal left as an empty scaffold.
- **2026-06-30 — Update 2.** Settled Pierre-anchored / ORI-via-Pierre / home deferred; added §6 Lab needs-finding; added §10 Department & supervision (ES vs Materials; ES MSc(R) needs an ES primary; ORI applications via Eng Sci).
- **2026-06-30 — Update 3.** Added **Furieri** as ES-primary candidate; config **Furieri primary + Mouthuy co**. Added **§9 degree structure & funding** (1-year-MSc myth; DPhil 3–4 yrs & competitively funded; funding flips the logic — MSc(R) usually self-funded; **apply-DPhil-decide-at-transfer**; supervisor-grant + German funding; **Dec 2026/Jan 2027** deadline, **2027-28** entry). Added **§10a** (advantage attaches to project+people) and **§10e** ("don't shop"). Added **§8** converge framing + two-question filter + founder–market-fit reframe.
- **2026-06-30 — Update 4.** **Recentred the research core** on **safe/stable learning control for compliant/embodied robotic systems**; **humanoid demoted to flagship testbed** (Mouthuy co, advantage retained); startup rides the control-software layer. Added the **three-optimise-for-X disentanglement** (§8f) and **startup-doesn't-fall-from-the-topic** (§8g). Added the **Furieri methods-fit evidence** (§10f: *"Closed-Loop Guarantees"* theme maps word-for-word; **BSc→PhD arc**; **port-Hamiltonian bridge**; safe-by-construction necessity). Added key open questions (Q5 robotics appetite; Q6 methods-fit ≠ thesis) + **thesis-seed directions** (§7). Added the **peer-level conversation opener**.
- **2026-06-30 — Update 5 (this).** Added **§11 Startup & founding path**: the **venture thesis** (safety/stability layer for learned control of compliant "physical AI" robots); the **two wedges** (horizontal safety-middleware SDK; medical/human-interactive vertical where the bio background compounds); the **PhD-produces-the-ingredients** logic (moat/IP via Oxford University Innovation, demonstrator, credential+network, publications-as-immigration-assets); and the **UK-root / US-expand** pathway with concrete visa routes (UK: Graduate → Global Talent / Innovator Founder; US: O-1A, E-2 as a German, L-1 new-office, IEP as a fragile backup). Renumbered subsequent sections. Added open questions (Q7 wedge, Q8 IP spinout-vs-license, Q9 geography), action items (spinout terms; build the immigration/fundraising evidence base), and a founder-immigration/spin-out sources block.
- **2026-06-30 — Update 6.** Added **§9f "PhD vs MSc — RESOLVED"**: apply to the **funded DPhil**; the self-funded MSc(R) as a *destination* is **dominated** (~£100k, thinner foundation, saves only ~1.5 yrs); decide at **transfer of status** (exit with an MSc earned *while paid* if the startup pull wins). Corrected the "only 3 years" (→ 3.5–4) and "1-year MSc" (→ that's a *taught* MSc) points. Added the **age/deep-tech reframe** (27 isn't late; ~45 avg high-growth founder; PhD builds the foundation while paid and can incubate the venture) as a principle (§3), and the **decisive self-assessment** — *do I actually want to do the research?* — as open question Q12 (if lukewarm → skip the degree, go straight at a frontier company / founding).
- `>> [ next entry: date — what changed ]`
