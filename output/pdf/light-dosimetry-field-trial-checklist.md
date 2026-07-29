# Checklist: Wearable light measurement in field studies

**Planning, collection, analysis, and reporting | Version 1.2, 29 July 2026**

**Source guide: [doi:10.17617/6xca-cg59](https://doi.org/10.17617/6xca-cg59)**

**Scope.** Wearable measurement of personal visible light or optical radiation in free-living studies. Mark an item **N/A** only with a reason. An outlined square is an action; a pale-gold **Context** box provides supporting information. Use terms consistently: **measured at the sensor plane** means the physical quantity represented by the calibrated sensor output at its actual position and orientation; **derived** means a quantity calculated from sensor channels, calibration functions, or spectral reconstruction; **inferred at the target plane or tissue** means a quantity extrapolated from the sensor position to the eye, skin, visual field, or another target. Near-corneal measurements approximate incident ocular exposure; they do not measure retinal irradiance.

## 1. Define the use case before choosing a device

- [ ] Write one sentence naming the **population, exposure, setting, time window, comparator, and outcome**.
- [ ] Name the target—ocular incident light, visual scene, skin/UV dose, environmental light opportunity, or intervention delivery/adherence—because each requires different sensors and placements.
- [ ] State the inference scale: moment, episode, biological day, participant average, or group average; validation at one scale does not transfer to another.
- [ ] Pre-specify the primary optical quantity, placement, metric, analysis window, and state mask (wake, pre-sleep, sleep, work, outdoors, intervention).
- [ ] Pre-specify the minimum useful effect or precision, then derive sample size and monitoring duration from pilot data, reliability, or power analysis. Cover relevant work/free days, schedules, and seasons. **No duration, epoch, or coverage threshold is universal.** One week at ≤2-min sampling was reliable in one outdoor-exposure study of children and young adults, not as a general rule. [L8]
- [ ] Register hypotheses, metrics, exclusions, transformations, and sensitivity analyses before examining outcomes.

### Match the design to the use case

**Circadian, sleep, and light-health studies**

- [ ] Prefer near-corneal placement; measure melanopic EDI, photopic illuminance, and, when validated, all five alpha-opic quantities. Align windows to sleep/wake or circadian phase; collect sleep timing, naps, wear, and shift schedule. Treat Brown targets as context for healthy day-active adults, not diagnostic cut-offs. [L1, L2a, L2b]

**Light intervention or therapy adherence**

- [ ] Measure where the dose should reach the eye. Record intervention and background light; spectrum, plane, distance, direction, timing, ramping, duration, interruptions, and adherence. Operational feedback may aid use; withhold exposure feedback unless it is part of the intervention because it can change behaviour. Use ENLIGHT where applicable. [L3]

**Large or long epidemiological studies**

- [ ] Balance fidelity, burden, and retention. If near-eye wear is infeasible, chest is generally a more defensible proxy than wrist; validate placement for the planned metrics and population. Pre-specify a small metric set and, where possible, include a simultaneous eye/body validation subsample.

**Workplace, building, transport, or urban studies**

- [ ] Combine personal sensing with time-location/activity and light-source context. Record dates, coordinates, weather/daylight opportunity, work/commute/outdoor periods, and relevant room, window, shading, luminaire, workstation, and view direction. A fixed outdoor reference describes available light, not personal ocular exposure. [L9]

**Visual experience, outdoor-time/myopia, UV, or photobiological dose**

- [ ] Measure at the relevant tissue or viewpoint. Visual experience may require luminance/radiance, field of view, scene images, or gaze; outdoor-time studies need validated placement and thresholds; UV/skin studies need anatomical site and action-weighted irradiance or dose. Photopic lux cannot substitute.

<!-- COLUMN -->

## 2. Specify, verify, and pilot the measurement system

### Device and data capability

- [ ] Require export of timestamps, raw or minimally processed channels, status flags, and calibration information, not only proprietary summaries.
- [ ] Document recording interval versus internal sampling/averaging; wavelength range and channel bandwidths; spectral responsivity; alpha-opic reconstruction; field of view and angular/cosine response; range, resolution, dark noise, linearity, saturation, and temporal response.
- [ ] Check battery life, storage, data-transfer failure modes, clock behaviour and drift, daylight-saving handling, temperature/humidity response, water resistance, ruggedness, buttons/indicators, and whether settings persist after charging.
- [ ] Assess comfort, weight, attachment, visibility, skin/contact risks, charging burden, phone/OS dependency, cloud location, privacy, licensing, warranty, recalibration, and spare-device needs. Use the specification helper to make procurement requirements auditable. [S6]

### Fit-for-purpose validation (V3)

- [ ] **Verify the sensor:** compare every unit, or a justified sample, with a traceably calibrated reference across the study's spectra, levels, angles, modulation, and environmental conditions. Test dark/noise floor and saturation. Quantify accuracy, repeatability, inter-unit variation, and uncertainty.
- [ ] Co-locate study units under stable conditions before deployment; repeat after batches or at study end to detect drift. Keep individual correction factors only when technically justified.
- [ ] **Validate the algorithm:** show that channel processing and derived quantities/metrics recover the intended physical construct under relevant scenes. A single lamp or overcast-sky comparison is not a complete validation.
- [ ] **Validate the claimed use:** for health or clinical claims, establish relevance in the intended population and setting; technical accuracy alone is insufficient. [L4, L5]
- [ ] Freeze and record manufacturer, model, serial number, device ID, firmware, settings, calibration date/method/factors, valid range, software/export version, and all repairs or swaps.

### Placement

- [ ] Specify anatomical site, side, height, sensor plane, orientation, field of view, and attachment with a photo or diagram; train staff to fit it consistently.
- [ ] For ocular questions, prefer near-eye placement aligned as closely as practical with habitual view. State clearly when a sensor is a proxy.
- [ ] If using chest, standardise height/orientation and log jacket, scarf, hair, bag-strap, or posture occlusion. If using wrist, log sleeve and hand orientation and justify why its error is acceptable.
- [ ] Do not apply a universal body-to-eye correction. Validate any translation between sensor placements for the planned metrics, population, and setting.

> **Context.** In the supplied multi-site analysis using identical devices, average momentary underestimation varied by context from about 4% to 23% at chest and 30% to 55% at wrist. Timing summaries were less sensitive than levels and temporal dynamics, and individual error remained large. [S7]

### End-to-end pilot

- [ ] Pilot recruitment, fitting, instructions, a normal day and night, non-wear logging, charging, downloads, timestamp joins, QC, and planned metrics in representative users.
- [ ] Confirm that the sensor range and epoch resolve the shortest relevant event without exhausting battery/storage.
- [ ] Use pilot feedback to reduce burden. Near-eye devices can improve biological relevance but size, weight, stability, appearance, and social reactions can reduce wear. [L10a, L10b]

<!-- PAGE -->

## 3. Run a field protocol that makes compliance observable

### Participant instructions

- [ ] Give a short written/illustrated SOP and demonstrate correct placement. Ask the participant to show it back ("teach-back").
- [ ] Define exactly when to wear, remove, recharge, or reposition the device. Explain how to handle showering, exercise, contact sports, work restrictions, travel, and device failure.
- [ ] Give non-wear and sleep different procedures. A useful option is an opaque bag for waking non-wear and a labelled, face-up bedside position for sleep-environment measurement. Bedside light is **ambient sleep-environment light**, not ocular wear.
- [ ] Provide a contact route, spare attachment materials, and simple reminders. Explain why correct wear matters without revealing hypotheses that could change behaviour.
- [ ] At study end, ask whether the device, feedback, or diaries changed clothing, location, lighting, outdoor time, sleep, or social behaviour.

### Auxiliary data not captured by the wearable sensor

- [ ] **Wear/non-wear:** start, end, reason, placement, black-bag confirmation, and late entry; combine self-report with event button and sensor evidence where available.
- [ ] **Sleep/wake:** attempted sleep, final wake, naps, shift or irregular schedule, and where/how the device was placed. Actigraphy may complement diaries but does not define ocular wear.
- [ ] **Context:** activity, indoor/outdoor/location, primary light source, intervention episode, relevant glasses/sunglasses/hat/clothing, and unusual exposure.
- [ ] **Experience and deviations:** discomfort, occlusion, displacement, charging, malfunction, travel, protocol deviations, and perceived behaviour change.
- [ ] **Environment when relevant:** photoperiod, weather/temperature, fixed reference logger, satellite daylight estimate, building/room characteristics. Collect only domains that justify their burden; sleep and wear are usually highest priority. [L6]

### During collection

- [ ] Synchronise device and study clocks before issue; record the check and any drift correction. Confirm device ID, participant ID, placement, start/end, battery, storage, and settings at handover.
- [ ] Review uploads or devices at a pre-specified cadence for missing files, flat lines, saturation, incorrect placement, battery failure, and overdue logs. Use neutral reminders and researcher-only operational alerts when feedback could cause reactivity.
- [ ] Keep a dated anomaly and contact log. Record device swaps as new intervals, never silently concatenate them.
- [ ] Download promptly, verify row count/time range, checksum and back up the untouched export, then document chain of custody.
- [ ] Complete and document a data-protection and privacy risk assessment. Check GPS, images, cloud services, exact home/work locations, participant lookup keys, retention, and sharing against applicable ethics approvals, institutional requirements, and privacy laws; minimise collection and access.

<!-- COLUMN -->

## 4. Use interoperable data and metadata

### Recommended time-series file

- [ ] Use rectangular **RFC 4180 CSV**, UTF-8, comma delimiter, dot decimal, one header row, and stable names. Use `Datetime` for the canonical time column and `snake_case` for other fields. Put units in metadata, not cells; use empty cells for missing values, never sentinel numbers or mixed text/numeric values. [S5]
- [ ] Use one logical record per participant-device-placement-timestamp. Include at least:

`participant_id, device_id, placement_id, Datetime, photopic_illuminance_lx, melanopic_edi_lx, worn, sleep_state, qc_flag`

- [ ] Store `Datetime` as RFC 3339 UTC with `Z` (for example, `2026-03-09T14:30:00Z`), ordered and unique. Store the IANA time zone (for example, `Europe/Berlin`), UTC offset, and optional device/local time separately. Document daylight-saving transitions and clock corrections.
- [ ] Keep status/QC in separate fields. Define allowed values for wear, sleep, placement, intervention, missing reason, and quality flags in a data dictionary.
- [ ] Preserve raw exports unchanged. Version derived tables and retain provenance. After regularising a grid, represent gaps as timestamped rows with empty measurements. A gap is not darkness; regularisation is not imputation.

### Recommended metadata package

- [ ] Package data using **GLC Data Package 3.0.1**, based on Frictionless Data Package: root `datapackage.json`; study, participant, device, device-datasheet, and dataset metadata; optional participant-characteristics table; schemas; data; README; licence; and checksums. Validate the exact release/commit. [S2]
- [ ] **Study:** title/ID, question, design, sample, setting, sites, coordinates, time zones, dates/seasons, groups/intervention, preregistration, ethics, contributors, funding, licence.
- [ ] **Participant/trial:** pseudonymous ID, group, inclusion-relevant characteristics, trial start/end, schedule. Store the identity lookup separately with restricted access.
- [ ] **Device/placement:** unique ID, manufacturer/model/serial/firmware, settings, calibration and uncertainty, valid range, channel definitions/units, mount/location/orientation, swaps and faults.
- [ ] **Dataset/variable:** exact path and checksum, format/encoding, raw or processed state, recording and aggregation intervals, time-zone semantics, preprocessing, variable name/label/type/unit/controlled term, factor levels, missing/QC codes, calibration equation.
- [ ] Include auxiliary-data schemas, a data dictionary, README, anomaly log, software/environment lockfile, and a machine-readable processing history.

<!-- PAGE -->

## 5. Preprocess and quality-control without hiding uncertainty

- [ ] Validate file structure, encoding, headers, data types, units, timestamp parsing, order, duplicates, regularity, and expected boundaries with the wearable file validator. [S5]
- [ ] Plot the complete raw timeline and distributions for every participant, device, and channel. Investigate flat lines, repeated patterns, spikes, impossible jumps, noise-floor values, saturation, resets, clock drift, and cross-device disagreement.
- [ ] Make all resampling explicit: target grid, alignment rule, averaging/integration method, minimum observations, and treatment of boundary points. LightLogR's `gap_handler()` exposes implicit gaps; it does **not** impute them. [S4]
- [ ] Keep distinct flags for implicit gap, waking non-wear, bedside/sleep state, occlusion, out-of-range, device fault, and unknown. Never convert one category to another merely because the light level is low.
- [ ] Establish non-wear from converging evidence. Self-report plus an opaque bag can support detection; an event button alone was unreliable in one field study. Low light can also be true darkness, so any algorithm and threshold need protocol- and device-specific validation. [L7]
- [ ] Apply the state mask required by the estimand **before** calculating metrics. State whether sleep, bedside, naps, intervention interruptions, or travel are retained.
- [ ] Quantify coverage at epoch, analysis-window, day, and participant levels. Define expected denominators and inclusion rules prospectively for each metric. The 50%-per-hour and 80%-per-day filters in the supplied MeLiDos analyses are study-specific examples, not defaults. [S1, S8]
- [ ] Publish the sample flow and missingness by reason, time, participant, placement, and group. Check whether missingness coincides with showers, sport, outdoors, work, sleep, or high/low light.

### Missing data and sensitivity

- [ ] Do not impute by default. If imputation is defensible, state the model, maximum gap, variables used, uncertainty propagation, and a no-imputation sensitivity analysis.
- [ ] Preserve exact zeros when they can represent darkness. If using logarithms or geometric means, state the offset or zero model, its unit, rationale, and inverse transform; test sensitivity. [L11]
- [ ] Run sensitivity analyses for plausible coverage rules, state definitions, gap handling, outlier/device limits, placement, and metric parameters. Use a common sample when comparing scenarios.

<!-- COLUMN -->

## 6. Match the metric set and model to the question

- [ ] **Specific hypotheses:** pre-specify a small core set: one primary metric per hypothesis or primary question, plus only a few complementary secondary metrics. Report effect sizes and uncertainty, not isolated p-values. [L12]
- [ ] **Exploratory analyses:** use a comprehensive, structured set across the relevant families below; label it exploratory and report the full set. S7/S8 show that results can differ by metric class and modelling scale.

For **every** metric report: optical quantity and unit; sensor and plane; epoch/aggregation; analysis window/state; expected denominator and coverage; threshold/event/gap rule; zero/transformation rule; and analysis level.

- [ ] **Data quality:** expected, recorded, valid, and worn minutes/percent; non-wear, gap, occlusion, saturation, and below-range time by window.
- [ ] **Level/distribution:** arithmetic mean when additive exposure is relevant; median and IQR for typical exposure; useful percentiles and below-range/zero fraction. Light is strongly skewed, so do not report the mean alone.
- [ ] **Dose/history:** time integral with correct units (for example, lx·h or W·m^{-2}·h; action-weighted dose for UV). Weight fragmented episodes by their duration.
- [ ] **Duration/events:** time or percentage above/below a justified threshold; longest/mean episode; pulse count or crossings. State minimum pulse, merge tolerance, and whether gaps break an episode.
- [ ] **Timing:** first/last crossing, exposure centroid or cumulative-exposure midpoint, and brightest/darkest-window onset/midpoint. Use circular methods or a justified anchor when values cross midnight; report undefined cases.
- [ ] **Daily pattern/dynamics:** time-binned profile, amplitude/contrast, intradaily variability, or interdaily stability. IS/IV need meaningful multi-day, regularly sampled coverage; single-day IS is not interpretable.
- [ ] **Spectrum:** validated alpha-opic EDI values and, if useful, melanopic daylight efficacy ratio. Handle division by zero. CCT alone is not a physiological exposure metric.
- [ ] If evaluating the Brown consensus for healthy adults with regular daytime schedules, report separately: daytime ≥250 lx melanopic EDI at eye level, 3 h pre-sleep ≤10 lx, and sleep environment ≤1 lx. Report duration/percentage and coverage; do not use these values as universal health diagnoses or exclusion criteria. [L2a, L2b]
- [ ] **Modelling scale:** match the model to each metric's support and distribution rather than forcing all metrics onto one scale. Examples include Gaussian models for suitable continuous outcomes; Tweedie models with a log link for non-negative, skewed outcomes with zeros; count models for crossings or pulses; and bounded or circular methods for bounded or clock-time outcomes. Report the family/link, transformation or offset, diagnostics, and uncertainty on both model and interpretable back-transformed scales. [S7, S8]

<!-- PAGE -->

## 7. Report, archive, and hand over

- [ ] Report recruitment and participant flow; protocol dates/site/season; schedule; device/firmware/calibration; exact placement; epoch; instructions; reminders; actual wear; burden/reactivity; auxiliary data; all processing, exclusions, coverage, and software versions.
- [ ] Use accurate language: "near-corneal measurement", "chest proxy", or "derived melanopic EDI", not "retinal dose" unless retinal exposure was genuinely modelled and validated.
- [ ] For interventions, report source and background spectra, intensity, geometry, timing, duration, adherence, and deviations. For buildings, report daylight/electric-light and spatial context. [L1, L3, L9]
- [ ] Release de-identified raw and derived data separately when consent permits, with metadata package, schemas, code, environment lockfile, README, data dictionary, anomaly log, checksums, licence, version, and persistent identifier. Protect precise locations and re-identification keys.
- [ ] State limitations from placement, angular/spectral response, low-light range, non-wear, missingness, reactivity, residual confounding, and generalisability. Agreement for one metric does not validate the full time series or other metrics.

### Red flags: stop and resolve

- [!] Photopic illuminance (lx) reported as melanopic EDI (lx). These are different quantities and are not interchangeable.
- [!] Alpha-opic values reported without validating the sensor and reconstruction method. Report them only after spectral and algorithm validation.
- [!] Wrist-level measurements presented as ocular exposure. Name the measured placement and treat any eye-level estimate as a validated proxy.
- [!] Darkness, true zeros, sleep, non-wear, and data gaps assigned one code. Preserve them as separate states because they have different meanings.
- [!] Timestamps relabelled with another time zone instead of converted. Preserve the UTC instant, IANA zone, and offset.
- [!] Minimum-data rules copied from another study without rationale. Before analysis, define how much valid data each metric requires and state the rationale.
- [!] A regular time grid described as imputation although gaps remain empty. Use “regularisation” unless values are actually filled or estimated.
- [!] Placement or device agreement assessed by correlation alone. Evaluate bias, limits of agreement, and metric-specific error.
- [!] One body-to-eye correction applied across participants, contexts, or metrics. Validate translation for the intended placement, population, and use.
- [!] Exposure summarised only by the arithmetic mean. Add distribution, timing, duration, or dose metrics that match the question.
- [!] A metric reported without its analysis window or how much data was expected. State both so the value and coverage are interpretable.

<!-- COLUMN -->

## Sources

### Project sources

- **[S0 Researcher Guide](https://doi.org/10.17617/6xca-cg59):** RDA Optical Radiation Exposure and Visual Experience Data Working Group. (2025). *Technical guide for wearable optical radiation dosimetry and visual experience assessment*.
- **[S1 MeLiDos project](https://github.com/MeLiDosProject):** MeLiDos Project. (2026). *MeLiDos project* [GitHub organisation]. GitHub.
- **[S2 GLC Data Package Viewer](https://github.com/tscnlab/glc-dp-viewer):** Translational Sensory and Circadian Neuroscience Lab. (2026). *GLC Data Package Viewer* [Computer software]. GitHub.
- **[S3 LightLogR webinar](https://github.com/tscnlab/LightLogR_webinar):** Translational Sensory and Circadian Neuroscience Lab. (2026). *LightLogR webinar* [Workshop materials]. GitHub.
- **[S4 LightLogR](https://doi.org/10.21105/joss.07601):** Zauner, J., Hartmeyer, S., & Spitschan, M. (2025). LightLogR: Reproducible analysis of personal light exposure data. *Journal of Open Source Software, 10*(107), 7601.
- **[S5 Wearable file validator](https://tscnlab.github.io/wearable_file_validator/):** Translational Sensory and Circadian Neuroscience Lab. (2026). *Wearable file validator* [Web application].
- **[S6 Device specification helper](https://github.com/tscnlab/wearable_devices_spechelper):** Zauner, J., Stefani, O., Biller, A. M., Guidolin, C., & Spitschan, M. (2026). *A web-based specification tool for wearable light loggers and optical radiation dosimeters* [Computer software].
- **[S7 Placement analysis repository](https://doi.org/10.5281/zenodo.21533915):** Zauner, J., de Vries, S. W., Didikoglu, A., van Duijnhoven, J., & Spitschan, M. (2026). *Toward scalable ambulatory light dosimetry: Sensor-placement bias under naturalistic conditions* [Analysis software] (Version 0.9.9). Zenodo.
- **[S8 Light exposome analysis artifact](https://github.com/tscnlab/ZaunerEtAl_bioRxiv_2026):** Zauner, J., Didikoglu, A., Aerts, S., et al. (2026). *Environmental and behavioural determinants of the personal light exposome* [Analysis artifact]. GitHub.

### Supporting literature and standards

- **[L1 CIE TN 011:2020](https://files.cie.co.at/CIE_TN_011_2020.pdf):** International Commission on Illumination. (2020). *What to document and report in studies of ipRGC-influenced responses to light* (CIE TN 011:2020).
- **[L2a CIE S 026/E:2018](https://www.cie.co.at/publications/cie-system-metrology-optical-radiation-iprgc-influenced-responses-light-0):** International Commission on Illumination. (2018). *CIE system for metrology of optical radiation for ipRGC-influenced responses to light* (CIE S 026/E:2018).
- **[L2b Brown et al. 2022](https://doi.org/10.1371/journal.pbio.3001571):** Brown, T. M., Brainard, G. C., Cajochen, C., et al. (2022). Recommendations for daytime, evening, and nighttime indoor light exposure to best support physiology, sleep, and wakefulness in healthy adults. *PLOS Biology, 20*(3), e3001571.
- **[L3 ENLIGHT](https://doi.org/10.1016/j.ebiom.2023.104889):** Spitschan, M., Kervezee, L., Lok, R., McGlashan, E., Najjar, R. P., ENLIGHT Consortium, Schlangen, L. J. M., & Smolders, K. C. H. J. (2023). ENLIGHT: A consensus checklist for reporting laboratory-based studies on the non-visual effects of light in humans. *eBioMedicine, 98*, 104889.
- **[L4 V3 framework](https://doi.org/10.1177/20552076221144858):** Spitschan, M., Smolders, K., Vandendriessche, B., Bent, B., Bakker, J. P., Rodriguez-Chavez, I. R., & Vetter, C. (2022). Verification, analytical validation and clinical validation (V3) of wearable dosimeters and light loggers. *Digital Health, 8*, 20552076221144858.
- **[L5 Wearable light-logger review](https://doi.org/10.1016/j.buildenv.2025.112771):** van Duijnhoven, J., Hartmeyer, S. L., Didikoglu, A., Stefani, O., Houser, K. W., Kalavally, V., & Spitschan, M. (2025). Measuring light exposure in daily life: A review of wearable light loggers. *Building and Environment, 274*, 112771.
- **[L6 Auxiliary data and QA/QC](https://doi.org/10.1038/s44323-025-00067-9):** Zauner, J., Stefani, O., Bocanegra, G., Guidolin, C., Schrader, B., Udovicic, L., & Spitschan, M. (2026). Auxiliary data, quality assurance and quality control for wearable light loggers and optical radiation dosimeters. *npj Biological Timing and Sleep, 3*, 11.
- **[L7 Non-wear intervals](https://doi.org/10.3758/s13428-025-02823-y):** Guidolin, C., Zauner, J., Hartmeyer, S. L., & Spitschan, M. (2026). Collecting, detecting, and handling non-wear intervals in longitudinal light exposure data. *Behavior Research Methods, 58*(1), 36.
- **[L8 Measurement duration and frequency](https://doi.org/10.1097/OPX.0000000000001041):** Ulaganathan, S., Read, S. A., Collins, M. J., & Vincent, S. J. (2017). Measurement duration and frequency impact objective light exposure measures. *Optometry and Vision Science, 94*(5), 588-597.
- **[L9 Field-study reporting recommendations](https://doi.org/10.1177/14771535241248540):** de Vries, S. W., Gkaintatzi-Masouti, M., van Duijnhoven, J., Mardaljevic, J., & Aarts, M. P. J. (2025). Recommendations for light-dosimetry field studies based on a meta-analysis of personal light levels of office workers. *Lighting Research & Technology, 57*(1), 47-70.
- **[L10a Five-day near-eye field study](https://doi.org/10.3390/clockssleep6040042):** Stefani, O., Marek, R., Schwarz, J., Plate, S., Zauner, J., & Schrader, B. (2024). Wearable light loggers in field conditions: Corneal light characteristics, user compliance, and acceptance. *Clocks & Sleep, 6*(4), 619-634.
- **[L10b 24-hour near-eye field study](https://doi.org/10.1159/000531404):** Balajadia, E., Garcia, S., Stampfli, J., Schrader, B., Guidolin, C., & Spitschan, M. (2023). Usability and acceptability of a corneal-plane alpha-opic light logger in a 24-h field trial. *Digital Biomarkers, 7*(1), 139-149.
- **[L11 Zero-inflated light exposure](https://doi.org/10.1177/07487304251336624):** Zauner, J., Guidolin, C., & Spitschan, M. (2025). How to deal with darkness: Modeling and visualization of zero-inflated personal light exposure data on a logarithmic scale. *Journal of Biological Rhythms, 40*(5), 480-490.
- **[L12 Quantification metrics](https://doi.org/10.1177/14771535231170500):** Hartmeyer, S. L., & Andersen, M. (2024). Towards a framework for light-dosimetry studies: Quantification metrics. *Lighting Research & Technology, 56*(4), 337-365.

**Interpretation rule.** Standards and consensus statements define quantities and reporting expectations; empirical studies show what happened in specific devices, populations and protocols. Transfer numerical thresholds only after checking that the quantity, placement, population, context, epoch, and intended inference match.

### MeLiDos project (22NRM05)

This checklist draws on research resources from **[MeLiDos (22NRM05)](https://melidosproject.github.io/.github/)**.

### Funding disclaimer

Funded by the European Union. Views and opinions expressed are however those of the author(s) only and do not necessarily reflect those of the European Union or EURAMET. Neither the European Union nor the granting authority can be held responsible for them.

The project has received funding from the European Partnership on Metrology, co-financed from the European Union's Horizon Europe Research and Innovation Programme and by the Participating States.

<!-- MeLiDos page-1 wordmark and funding banner source: https://github.com/MeLiDosProject/.github/blob/main/profile/assets/logo_banner.png -->
