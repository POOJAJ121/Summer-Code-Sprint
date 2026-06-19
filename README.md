# 🚀 Summer Engineering Sprint (2026)

Welcome to my portfolio for the 2026 summer vacation! After finishing my 1st year of B.Tech in Electronics and Communication Engineering, I am using this break to master programming, simulate hardware, and bridge the gap between software and core electronics.

## 📅 Roadmap Overview
* **Weeks 1-2:** Core Software Foundations & Logic (Python/C)
* **Weeks 3-4:** Virtual Hardware Control (MicroPython + Wokwi)
* **Weeks 5-6:** Scientific Modeling & Trajectory Simulations

---

## 💻 Projects Completed

### Day 1 : Microcontroller Thermal Protection Logic
* **Language:** Python
* **What it does:** Simulates an automated cooling system for an embedded chip, changing fan speeds or triggering emergency shutdowns based on real-time temperature thresholds.

### Day 2: Automated Battery Charging Simulator
* **Language:** Python
* **Concepts Used:** `while` loops, assignment operators (`+20`), loop control termination states.
* **What it does:** Simulates an embedded power management chip that monitors battery levels during a charge cycle, providing real-time telemetry output and disconnecting safely once maximum capacity ($100\%$) is reached.

 ### Day 3: IoT Smart Streetlight Automation
* **Hardware Simulated:** ESP32 Microcontroller, 4-Pin LDR (Light Dependent Resistor) Sensor Module, LED Actuator.
* **Language:** MicroPython
* **Concepts Used:** Analog-to-Digital Conversion (ADC), Sensor data calibration, Hardware-Software integration loops.
* **What it does:** Simulates an automated municipal streetlight system. Reads continuous analog voltage data from an environmental light sensor and uses threshold logic to dynamically toggle high-power streetlights on/off based on real-time daylight levels.

  ### Day 4: Proximity Radar & Automated Braking Logic
* **Hardware Simulated:** ESP32 Microcontroller, HC-SR04 Ultrasonic Distance Sensor, Warning LED Actuator.
* **Language:** MicroPython
* **Concepts Used:** High-resolution microsecond timing (`time_pulse_us`), Signal propagation math ($Distance = \frac{Time \times Speed}{2}$), Real-time debugging and module imports.
* **What it does:** Simulates an automotive safety system. The controller shoots sound pulses, measures echo time to calculate object distances, and triggers a critical proximity alert and visual brake system warning if an obstacle comes within $20\text{ cm}$.

### Day 5: Servo Actuator Angle Positioning & PWM
* **Hardware Simulated:** ESP32 Microcontroller, SG90 Servo Motor Actuator.
* **Language:** MicroPython
* **Concepts Used:** Pulse Width Modulation (PWM), Duty Cycle Mapping, Nested loops (`for` loops with directional steps).
* **What it does:** Generates precise 50Hz PWM timing signals to sweep a robotic servo motor smoothly across its entire $180^\circ$ positional range, acting as the fundamental mechanism for steering, robotic arms, and articulation joints.
