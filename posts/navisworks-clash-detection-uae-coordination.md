---
title: "Navisworks Manage Clash Detection: UAE Coordination Workflow"
slug: navisworks-clash-detection-uae-coordination
date: 2026-10-26
category: drafting
category_title: Drafting
description: "Run Navisworks Manage clash tests for UAE projects—federate models, set tolerances, report and close clashes."
canonical: https://shoaibsite.blogspot.com/2026/10/navisworks-clash-detection-uae-coordination.html
---
**Navisworks clash detection** is how many UAE main contractors and BIM leads catch duct-vs-beam and pipe-vs-ceiling conflicts before fit-out starts. Navisworks Manage federates architectural, structural and MEP models, runs Clash Detective, and produces reports the design team can close against a shared issue list.

This tutorial walks through a practical UAE coordination workflow: append models, set hard vs soft tests, assign owners, and push status through Autodesk Docs or BIM collaboration without drowning the team in duplicate clashes.

**Key takeaways**

- Agree hard/soft tolerances in the BEP before the first run.
- Clash by discipline pairs, not one giant ‘everything vs everything’ test.
- Group duplicates; assign one owner and a due date per clash group.
- Link reports to shop-drawing and permit milestones.

## Tools and official references

Product overview: [Autodesk Navisworks](https://www.autodesk.com/products/navisworks/overview). Command-level help: [Navisworks 2026 help](https://help.autodesk.com/view/NAV/2026/ENU/). For cloud markup and model exchange use [Autodesk BIM 360 / Docs family pages](https://www.autodesk.com/bim-360). Authority context for Dubai permits sits on [Dubai Municipality](https://www.dm.gov.ae/).

## Hard vs soft vs duplicate clashes

| Type | Meaning | Typical UAE example |
| --- | --- | --- |
| Hard | Geometry intersects | Chilled-water pipe through beam |
| Soft | Clearance / buffer violated | Cable tray inside maintenance zone above ceiling |
| Duplicate | Same element appears twice | Two copies of a duct after a bad append |

## Federation workflow (step by step)

1. Collect current IFC or native NWC/NWD exports from each discipline—aligned to shared coordinates.
2. Append into a coordination NWF; never explode consultant geometry into CAD for clash.
3. Create search sets: Architecture walls/ceilings, Structure beams/slabs, MEP by system.
4. Run Clash Detective for Arch×Struct, MEP×Struct, MEP×Arch with agreed tolerances.
5. Group results by grid zone; assign status Open → Reviewed → Resolved → Approved.
6. Export HTML/XML report; link clash IDs to the issue tracker in Docs.
7. Re-run only changed search sets after each model drop—not the entire history blindly.

Site and civil context often comes from Civil 3D—see [Civil 3D basics for site work](https://shoaibsite.blogspot.com/2026/10/civil-3d-basics-for-site-and.html). Building models usually come from Revit or Archicad: [Revit BIM workflow for small design firms](https://shoaibsite.blogspot.com/2026/10/revit-bim-workflow-for-small-design.html) and [Archicad vs Revit](https://shoaibsite.blogspot.com/2026/10/archicad-vs-revit-which-bim-tool-fits.html).

## Sample clash matrix (cite-worthy)

| Test | Tolerance | Owner | Gate |
| --- | --- | --- | --- |
| MEP wet × Structure | 0–15 mm hard | MEP coordinator | Before ceiling shop drawings |
| Duct × Ceiling zone | Soft 100–150 mm | Fit-out architect | Before RCP approval |
| Façade bracket × Slab edge | Hard 0 mm | Façade engineer | Before stone cladding SD |
| Fire services × Escape path | Per code soft | Fire consultant | Before authority package |

Close coordination loops against the same milestones you use for [shop drawing approval in Dubai](https://shoaibsite.blogspot.com/2026/10/shop-drawing-approval-process-dubai.html) and [Dubai fit-out approval drawings](https://shoaibsite.blogspot.com/2026/10/dubai-fit-out-approval-drawings.html). For IFC-first Dubai submissions, pair this with our [IFC OpenBIM workflow for Dubai BIM submissions](/blog/ifc-openbim-workflow-dubai-bim-submissions/).

## Issue writing that gets clashes closed

A clash ID alone does not move a duct. Each issue should carry:

- Grid location and level.
- Disciplines involved and proposed owner.
- Screenshot from the federated model.
- Suggested resolution (reroute, resize, open structure request).
- Due date tied to the next model drop.

Ban vague titles like “Clash 1284.” Prefer “L12 Grid C-4 CHW vs beam B12 — MEP to offset 150 mm south.”

## Cadence for UAE main-contractor meetings

| Meeting | Input | Output |
| --- | --- | --- |
| Weekly coordination | Fresh NWC/IFC drops | Updated clash groups + owners |
| Bi-weekly design | Open hard clashes only | Signed decisions in minutes |
| Pre-ceiling close | Soft clearance report | RCP shop-drawing release gate |
| Pre-stone install | Façade/slab edge clashes | Cladding SD release gate |

Publish the clash dashboard PDF to the CDE the same day—do not leave status only inside one planner’s NWF.

## Search set library (starter)

- ARCH_Walls · ARCH_Ceilings · ARCH_Doors
- STR_Beams · STR_Columns · STR_Slabs
- MEP_Duct_Supply · MEP_Duct_Return · MEP_Pipe_CHW · MEP_Pipe_Domestic · MEP_CableTray
- FF_Joinery · FF_Stone (when modelled)

Save search sets in the coordination NWF template so every new tower does not reinvent filters. Review membership whenever a discipline changes element naming.

For shop-drawing packages that follow clash close-out, keep the same grid references on RCP and ceiling SD sheets so installers can find the resolved route without opening Navisworks.

## Export and archive rules

At each coordination milestone, publish an NWD snapshot plus the HTML clash report to the CDE. Lock write access on that revision. When disputes arise months later about who owned a duct clash, the archived report is the evidence—not a rebuilt NWF on someone’s laptop.

Also archive the search-set definitions and tolerance values used for that run. Changing tolerance from 15 mm to 50 mm silently between weeks makes trend charts meaningless.

## FAQ

### What is Navisworks clash detection?

Navisworks clash detection compares geometry from federated models to find hard intersections, soft clearance violations and duplicate elements so the team can resolve them before site installation.

### What tolerance should UAE projects use?

There is no single number. Agree tolerances per discipline in the BEP—often tighter for wet services and looser for soft clearance zones. Document them before the first Clash Detective run.

### Do I need Navisworks Manage or Freedom?

Clash Detective and full coordination tools require Navisworks Manage (or the appropriate Autodesk collection). Freedom is for viewing published NWD/NWC files, not for running clash tests.

Need coordinated shop drawings after clash close-out? Contact [D3DDD](/) at [info@d3ddd.com](mailto:info@d3ddd.com).

Originally published on [ShoaibSite](https://shoaibsite.blogspot.com/2026/10/navisworks-clash-detection-uae-coordination.html).
