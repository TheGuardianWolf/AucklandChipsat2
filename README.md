# AucklandChipsat2 - Attitude Determination and Control

Overview:
Design an attitude control system for a ChipSat for the following conditions:
 - Orbiting a planet with an unknown or changing magnetic field
 - Planet has significant infrared or radio emissions
 - Orbit is not necessarily known

Aim of the control system:
 - To allow a ChipSat to de-tumble and orient relative to the planet orbited
 
Hardware used (for real satellite):
 - Gyroscope
 - Magnetometer
 - Radio antenna or IR sensor
 - 3 Magnetorquer
 
Hardware used for demo:
 - Gyroscope
 - Magnetometer
 - LDR
 - 2 axis magnetorquer

Attitude determination algorithm:
The ChipSat uses a gyroscope for dead-reckoning of attitude. This is expected to
introduce error over time due to bias and numerical errors. To correct for this,
measurements from the a light sensor are taken as the ChipSat tumbles. The light
intensity is used to detect the angle at which the target planet was visible. This
known point is used to calibrate the dead-reckoning calculation to provide a better
angle estimate.

Attitude control:
The attitude determination algorithm gives the chipsat its current attitude and
angle to the target planet. The satellite then determines the error between
its current and desired attitude.

Next, the satellite measures the magnetic field of the orbited planet. This is done
at the magnetic field is not necessarily known. Using the error angle calculated
previously, the satellite calculates a new magnetic field, which is the planet's
field rotated by the error angle.

Finally, the satellite energises it's magnetorquers to generate this magnetc field.
This will create a torque which will cause the satellite to rotate such that the
generated field and planet field are aligned.

