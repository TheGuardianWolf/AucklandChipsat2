% Assuming free space except for external field %

B = 5e-5; % T

N = 1000; % Per m

theta = pi/2; % Alignment

I = 0.3; % Amps

A = pi * (0.03)^2; % m^2

TorqueGoal = 2.25 * 10^(-5) ;% Nm


sin(theta)*N*B*A*I / TorqueGoal