<div align="center">

<img src="https://media.tenor.com/KGigVwznyJYAAAAC/steal-flying.gif" height="220" alt="Minion flying through the sky"/>
&nbsp;&nbsp;
<img src="assets/pushing-the-button-stuart.gif" height="220" alt="Stuart pushing the launch button"/>

<sub><code>ignition sequence start…</code></sub>

<img src="assets/hero.svg" width="100%" alt="Manikandan Shanmugam: propulsion, energetics and autonomous flight"/>

<a href="https://www.linkedin.com/in/manikandanaerox"><img src="https://img.shields.io/badge/LinkedIn-manikandanaerox-0A66C2?style=for-the-badge&labelColor=0C1428" alt="LinkedIn"/></a> <a href="mailto:manikandan.mechx@gmail.com"><img src="https://img.shields.io/badge/Email-manikandan.mechx%40gmail.com-FF8A2A?style=for-the-badge&labelColor=0C1428" alt="Email"/></a> <img src="https://img.shields.io/badge/Base-Poitiers%2C%20France-5CD4FF?style=for-the-badge&labelColor=0C1428" alt="Poitiers, France"/> <img src="https://img.shields.io/badge/Internship-6%20months%20from%20Mar%202027-3DDC97?style=for-the-badge&labelColor=0C1428" alt="Seeking a 6-month internship from March 2027"/>

</div>

<br/>

```yaml
callsign:   manikandanaerox
status:     M2 MSc Aeronautics & Space, Propulsion & Energetics @ ISAE-ENSMA
background: Mechanical engineering → aerospace
two sides:  [propulsion & thermal systems, autonomous drones]
seeking:    6-month internship from March 2027
domains:    propulsion · energetics · thermal engineering · CFD · autonomous aerial systems
```

<img src="assets/stats.svg" width="100%" alt="Key numbers"/>

<img src="assets/divider.svg" width="100%" alt=""/>

## 🔥 Propulsion & Energetics

<img src="assets/atrex.svg" width="100%" alt="ATREX precooled air-turbo ramjet"/>

**ATREX precooled air-breathing engine: cycle and flight-domain analysis** · *Apr 2026*
Full thermodynamic cycle of a liquid-hydrogen ATREX engine at **12,000 m and Mach 3**: intake, precooler, compressor map, combustion chamber, heat exchanger, turbine and nozzle. I computed thrust, specific impulse and efficiencies, then built the flight domain under thrust, drag and temperature limits. Result: a **four-engine vehicle can reach 30 km at Mach 5–6**.

<table>
<tr>
<td width="50%" valign="top">
<img src="assets/thrust-chamber.svg" width="100%" alt="H2/O2 thrust chamber"/>

**H₂/O₂ combustion thermochemistry** · *Python, Cantera*
Stoichiometric H₂/O₂ combustion under rocket-propulsion conditions: adiabatic flame temperature, chemical equilibrium and dissociation from **0.1 to 10⁴ MPa**, cross-checked against an analytical estimate (**3,498 K**).
</td>
<td width="50%" valign="top">
<img src="assets/supersonic.svg" width="100%" alt="Mach 4 diamond airfoil"/>

**Supersonic CFD** · *STAR-CCM+*
A double-wedge airfoil at **Mach 4**, run inviscid (Euler) and viscous turbulent (Spalart–Allmaras) to separate wave drag from viscous drag, plus thickness and trailing-edge effects. I also modelled a Busemann biplane at incidence and nozzle flows at NPR 8 and 12.
</td>
</tr>
<tr>
<td width="50%" valign="top">
<img src="assets/thermosyphon.svg" width="100%" alt="Two-phase loop thermosyphon"/>

**Research Intern, Two-Phase Heat Transfer** · *Institut Pprime (CNRS · Univ. Poitiers · ISAE-ENSMA), Mar–Jul 2026*
Experimental research on two-phase loop thermosyphons for passive thermal management. I improved the rig's accuracy and repeatability and ran high-speed visualisation alongside T, P and ṁ measurements. I wrote MATLAB routines for heat-transfer rates, thermal resistances and HTCs (Nu, Re, Pr), then studied how heat transfer couples with flow instabilities. A manuscript I'm co-authoring is under internal review.
</td>
<td width="50%" valign="top">

**More from the lab bench** 🧪

- **Transient heat conduction in a sphere.** I wrote an explicit finite-volume solver in spherical coordinates with angle-dependent surface convection, derived its stability limit by von Neumann analysis and checked it with mesh refinement.
- **Automated thermal test interface** (*MATLAB, Fortran*). A GUI for multi-sensor acquisition, live plots and automated post-processing.
- **Coursework:** propulsion systems, combustion & thermochemistry, gas dynamics, heat transfer, fluid mechanics, numerical methods, instrumentation.

</td>
</tr>
</table>

<img src="assets/divider.svg" width="100%" alt=""/>

## 🛩️ Autonomous Flight

<img src="assets/vtol.svg" width="100%" alt="ENSMAERO VTOL 4+1 and mission planner"/>

| | Project | What I did |
|---|---|---|
| 🏆 | **Dassault UAV Challenge 2026** · ENSMAERO, ISAE-ENSMA<br/><sub>Propulsion & UAV Systems Engineer · Oct 2025 – now</sub> | **Jury's Favourite Award** (*Prix Coup de cœur du jury*) among 28 teams with a modular autonomous **VTOL 4+1, 2 m span**. I did the propulsion design and CFD optimisation, integrated sensors with a SpeedyBee F405, and wrote control algorithms in Python/C++ that we validated in ground and flight tests. |
| 🔥 | **Team Phoenix**, founder & captain · Team Turbonites LICET<br/><sub>Nov 2022 – Aug 2025</sub> | Founded and led a **20-member UAV team** that won an award at the **SAE Autonomous Drone Development Challenge 2024** (payload category). Took drones from CAD (SolidWorks) through FEA, 3D printing and flight test, with FC/IMU/GPS integration and Gazebo simulation. **100+ flight hours** as pilot. |
| 🛰️ | **VTOL R&D Intern** · Team Reconnaissance, HTBI Chennai<br/><sub>Jul 2024 – Mar 2025</sub> | Built autonomous VTOLs on a Holybro FC with an NVIDIA Jetson Nano companion computer. Ran flight-test campaigns and wrote Python pipelines (NumPy/Pandas/Matplotlib) for the flight data. Tuned mission planning for fixed-wing and multirotor platforms. |
| 🤖 | **Pixhawk MCP Server** · *ongoing* | A Python server that turns LLM tool calls into **MAVLink** commands (pymavlink) for Pixhawk/ArduPilot: telemetry, arm, take-off, GPS waypoints, land, RTL. Tested in ArduPilot SITL. |
| 🎛️ | **Custom quadcopter flight controller** | My own FC with **automatic PID tuning** of the control loops, so a quad is ready to fly once it's set up. |

```mermaid
flowchart LR
    A["🗣️ Natural-language command"] --> B["LLM tool call"]
    B --> C["MCP server · Python"]
    C -->|pymavlink| D["MAVLink"]
    D --> E["ArduPilot SITL"]
    D --> F["Pixhawk · real drone"]
    F -->|telemetry| C
```

<img src="assets/divider.svg" width="100%" alt=""/>

## 🧭 Flight Log

| When | Role | Where |
|---|---|---|
| 2025 – 2027 | 🎓 **MSc Aeronautics & Space, Propulsion & Energetics (M2)** | ISAE-ENSMA · Poitiers, FR |
| Mar – Jul 2026 | 🔬 Research Intern, two-phase heat transfer | Institut Pprime · Poitiers, FR |
| Oct 2025 – now | ✈️ Propulsion & UAV Systems Engineer | ENSMAERO / Dassault UAV Challenge |
| Jul 2024 – Mar 2025 | 🛠️ R&D Engineering Intern, VTOL design | Team Reconnaissance, HTBI · Chennai, IN |
| Feb – Apr 2024 | ⚙️ Automation & Systems Integration Intern | Loyola-ICAM (LICET) · Chennai, IN |
| Jul 2023 | 🌬️ Wind Turbine Technician Intern | Litewind Ltd · Chennai, IN |
| Jun – Jul 2023 | 📐 CMM Programmer Intern | Unique Measurement Service · Chennai, IN |
| 2021 – 2025 | 🎓 **B.E. Mechanical Engineering** | Loyola-ICAM College of Engg. & Tech. · Chennai, IN |

<details>
<summary><b>Leadership & activities</b></summary>
<br/>

- **Joint Secretary, ISHRAE Chennai Chapter** (Sep 2023 – Aug 2025): ran technical workshops and speaker sessions for a 500+ member student organisation.
- **3D Printing Student Lead, LICET Fablab** (Jul 2023 – Aug 2025): organised fabrication and 3D-printing workshops and demos.
- **Languages:** English (fluent) · French (A2) · Tamil (native)

</details>

<img src="assets/divider.svg" width="100%" alt=""/>

## 🧰 Toolbox

<div align="center">

**Code**<br/>
<img src="https://img.shields.io/badge/Python-0C1428?style=for-the-badge&logo=python&logoColor=FFD27A"/> <img src="https://img.shields.io/badge/NumPy%20·%20SciPy%20·%20Pandas-0C1428?style=for-the-badge&logo=numpy&logoColor=5CD4FF"/> <img src="https://img.shields.io/badge/MATLAB-0C1428?style=for-the-badge"/> <img src="https://img.shields.io/badge/C%2FC%2B%2B-0C1428?style=for-the-badge&logo=cplusplus&logoColor=5CD4FF"/> <img src="https://img.shields.io/badge/Fortran-0C1428?style=for-the-badge&logo=fortran&logoColor=E9EEF8"/> <img src="https://img.shields.io/badge/Git-0C1428?style=for-the-badge&logo=git&logoColor=FF8A2A"/> <img src="https://img.shields.io/badge/Linux%20·%20bash-0C1428?style=for-the-badge&logo=linux&logoColor=FFD27A"/>

**Simulation & CFD**<br/>
<img src="https://img.shields.io/badge/STAR--CCM%2B-0C1428?style=for-the-badge"/> <img src="https://img.shields.io/badge/ANSYS%20Fluent-0C1428?style=for-the-badge"/> <img src="https://img.shields.io/badge/Cantera-0C1428?style=for-the-badge"/> <img src="https://img.shields.io/badge/Finite%20Volume-0C1428?style=for-the-badge"/> <img src="https://img.shields.io/badge/Gazebo-0C1428?style=for-the-badge"/> <img src="https://img.shields.io/badge/ArduPilot%20SITL-0C1428?style=for-the-badge"/>

**CAD & Manufacturing**<br/>
<img src="https://img.shields.io/badge/CATIA-0C1428?style=for-the-badge"/> <img src="https://img.shields.io/badge/SolidWorks-0C1428?style=for-the-badge"/> <img src="https://img.shields.io/badge/Fusion%20360-0C1428?style=for-the-badge&logo=autodesk&logoColor=FF8A2A"/> <img src="https://img.shields.io/badge/FEA-0C1428?style=for-the-badge"/> <img src="https://img.shields.io/badge/3D%20Printing-0C1428?style=for-the-badge"/> <img src="https://img.shields.io/badge/CMM%20Inspection-0C1428?style=for-the-badge"/>

**UAV & Embedded**<br/>
<img src="https://img.shields.io/badge/Pixhawk%20Cube%20Orange-0C1428?style=for-the-badge"/> <img src="https://img.shields.io/badge/ArduPilot-0C1428?style=for-the-badge"/> <img src="https://img.shields.io/badge/MAVLink-0C1428?style=for-the-badge"/> <img src="https://img.shields.io/badge/QGroundControl%20·%20Mission%20Planner-0C1428?style=for-the-badge"/> <img src="https://img.shields.io/badge/Jetson%20Nano-0C1428?style=for-the-badge&logo=nvidia&logoColor=76B900"/> <img src="https://img.shields.io/badge/ESP32-0C1428?style=for-the-badge&logo=espressif&logoColor=FF4D3D"/> <img src="https://img.shields.io/badge/ATmega328-0C1428?style=for-the-badge"/> <img src="https://img.shields.io/badge/UART%20·%20I2C%20·%20SPI%20·%20CAN%20·%20PWM%20·%20RS485-0C1428?style=for-the-badge"/>

</div>

## 🏅 Awards & Certifications

- 🏆 **Dassault UAV Challenge 2026**: *Prix Coup de cœur du jury* (Jury's Favourite Award), ENSMAERO team, among 28 teams
- 🥇 **SAE Autonomous Drone Development Challenge 2024**: award winner (payload category), as founder & captain of Team Phoenix
- 🪪 **EU Certified Drone Pilot (DGAC)**: A1/A3 Open Category

<img src="assets/divider.svg" width="100%" alt=""/>

<div align="center">

**Building something that flies, burns or transfers heat? Let's talk.**

[linkedin.com/in/manikandanaerox](https://www.linkedin.com/in/manikandanaerox) · manikandan.mechx@gmail.com

<sub>All illustrations are hand-built animated SVGs (<code>assets/generate.py</code>). Clear skies ✈️</sub>

</div>
