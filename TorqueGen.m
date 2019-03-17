% Assuming free space except for external field %

B = 7e-4; % T

N = 100; % Turns 

theta = pi/2; % Alignment Angle. pi/2 being orthogonal.

I = 0.3; % Amps

A = pi * (0.03)^2; % m^2


TorqueGoal = 2.25 * 10^(-5) ;% Nm. This gives an angular acc. of 5rad/s^2 with an assumed mass of 20g.


sin(theta)*N*B*A*I / TorqueGoal % If ~1, we are good.
