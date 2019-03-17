import board
from analogio import AnalogOut

CLOCK_FREQUENCY_HZ = 16e6

analog_out = AnalogOut(board.A0)


def determine_attitude():
    return 1, 1


def compute_pid(x, y, e, i):
    '''
    x - target angle
    y - current estimate of angle
    '''
    Kp = 0.6  #  gain for proportional term
    Ti = 0.5  
    Td = 0.5
    dt = 1.0/CLOCK_FREQUENCY_HZ  # time step size

    enew = x - y  # current error
    d = (enew - e)/dt  # approximates error derivative
    e = enew  # update for next tick
    i = i + (1/dt)*e  # approximates error integral
    u = Kp*e + (Kp/Ti)*i + (Kp/Td)*d
    return u, e, i


x = 1.0
y = 2.0
e = x - y
i = 0.0

while True:
    x, y = determine_attitude()
    u, e, i = compute_pid(x, y, e, i)

    analog_out.value = u
