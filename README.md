# TOPAS-FISPACT-Activation-Simulation

💡 Project Overview: OPT Beamline Proton Therapy Simulation (UCSF), TOPAS example file
This repository contains Monte Carlo simulation code using TOPAS v3.7.0 for modeling the OPT (Ocular Proton Therapy) beamline at the University of California, San Francisco (UCSF). The simulation is designed to study dose delivery and particle spectra during ocular melanoma treatment using a monoenergetic proton beam.

🧪 Simulation Summary
Proton Beam Specification:

Energy: 67.5 MeV

Energy Spread: 0.7% FWHM (Gaussian)

Spot Size at Exit Window: 10 mm (σ)

Phantom Setup:

A water phantom is placed at the downstream end to verify a Spread-Out Bragg Peak (SOBP) with an absolute dose of 15 Gy.

Simulation Parameters:

Total number of protons: ~5.5 × 10⁷

Simulation type: 4D Monte Carlo (dynamic propeller motion)

Propeller rotation: 150 ms cycle, repeating over a 1-minute treatment scenario.

Physics Model:

QGSP_BIC_HP: Used for hadronic interactions with high-precision neutron modeling, recommended for low-energy proton therapy simulations.

Reference: [1] J. Perl, J. Shin, J. Schumann, B. Faddegon, H. Paganetti, TOPAS: an innovative 
proton Monte Carlo platform for research and clinical applications, Med. Phys. 39 
(2012) 6818–6837

☢️ FISPACT-II Simulation for Beamline Activation and Clearance Assessment
This repository contains FISPACT-II simulation input and output files for assessing component activation, radionuclide inventory, and clearance feasibility following proton therapy beamline irradiation.

🧪 Scenario Setup
🔹 2.1.a. Simple Scenario
A rapid estimation model to identify significant nuclides before detailed analysis.

No cooling time between patients

No weekend cooldown

15-year continuous operation assumed

Purpose: Identify radionuclides exceeding clearance levels

🔹 2.1.b. Detailed Scenario
A realistic clinical operation model incorporating patient workflow and decay.

10 patients/day, 1 min beam-on per patient → 10 min/day

30 min cooling between patients

Remaining ~19.3 hours/day used for passive cooldown

~351 patients/year × 4 fractions → ~4 patients/day

Purpose: Detailed activation profile for long-term planning

Reference: [2] G. Bailey, D. Foster, P. Kanth, M. Gilbert, The FISPACT-II user manual. https://f 
ispact.ukaea.uk/documentation-2/manual/, 2021. (Accessed 25 October 2024).

[3] J.C. Sublet, J.W. Eastwood, J.G. Morgan, M.R. Gilbert, M. Fleming, W. Arter, 
FISPACT-II: an advanced simulation system for activation, transmutation and 
material modelling, NDS 139 (2017) 77–137.

[4] https://fispact.ukaea.uk/wiki/Main_Page
