# missile-trajectory-and-intercept

Joshua Santy | Missile Trajectory and Intercept Simulation | June 2025

This program will simulate realistic 3D projectile motion of missiles and include a missile intercept system

User creates missile vehicle objects with initial conditions as simple or complex as desired

Simulation time-steps and state variables are stored at every time-step value

Missile intercept contains a guidance system and predicts incoming missile trajectory

**Current Features**:
- 2D Ballistic Motion, including constant thrust (no drag)
- Visualization of trajectory and output of initial and kinematic values

**Immediate To Do**:
- Double check ending values with thrust are correct
- See why gravity isn't changing with altitude
- Add a window/widget to the plot visualizaiton for initial/current conditions and environment parameters
- Add x and y pos of max height, along with t
- Eventually, time-dependent thrust

**Future Additions:**
- 3D visualization and environment
- Thrust acceleration contribution
- Shear drag / air resistance acceleration contribution
- Time-dependent mass / mass flow rate
- Altitude/environment-dependent acceleration contribution (air density, altitude, acceleration due to gravity)
- Guidance system and predictive calculations for interception missiles/artillery
- Full time-steppable simulation and output of all desired kinematic and aerodynamic variables
