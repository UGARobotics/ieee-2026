# Robotics Motor & Scheduler System

A Python-based framework for controlling motors, subsystems, and autonomous routines using a generator-driven scheduler. Designed for modular, non-blocking, and safe robotics operation with Phoenix6 TalonFX motors.

---

## Overview
---------------
                     +----------------+
                     |   Scheduler    |
                     | (50 Hz tick)   |
                     +--------+-------+
                              |
         +------+------+------+------+------+------+------ ...
         |                    |                    |
    +-----v-----+       +-----v-----+        +-----v-----+
    | Drivetrain|       |  Odometry |        |   Other   |
    +-----+-----+       +-----------+        +-----------+
          |                   |                    |
    +---+---+---+         +---+---+               ...
    |   |   |   |         |   |   |         
    m0  m1 m2  m3        w0  w1   w2        
---------------


This project provides:

- A **Motor utility class** with internal state management (IDLE / RUNNING)  
- A **Drivetrain subsystem** to manage multiple motors  
- A **Scheduler** that ticks all subsystems at a configurable frequency  
- **Generator-based autonomous routines** for non-blocking command sequences  
- Safe **emergency stop** handling  

The system is designed to run all motors and subsystems at a fixed tick rate (e.g., 50 Hz) while allowing autonomous routines to be written sequentially using `yield` / `yield from`.

---

## Features

- **Motor Class**
  - Low-level wrapper for TalonFX motors
  - Handles initialization and duty-cycle control with duration
  - Maintains internal state (IDLE / RUNNING)
  - Designed to be managed by higher-level subsystems like Drivetrain

- **Scheduler**
  - Manages all subsystems uniformly  
  - Feeds the enable signal periodically (`feed_enable`)  
  - Supports generator-based autonomous routines  
  - Stops all motors safely on completion or emergency  

- **Autonomous Routines**
  - Written as Python generators for sequential commands  
  - Interleaves subsystem updates automatically  
  - Non-blocking: motors can run simultaneously without freezing the loop  

---

## Installation for Pi

TODO