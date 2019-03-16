def compute_pid(x, y, e, i):
    '''
    x - target angle
    y - current angle
    '''
    Kp = 0.5  #  gain for proportional term
    Ti = 0.5
    Td = 0.5
    dt = 1/16e6

    enew = x - y
    if e is None:
        d = 0
    else:
        d = (enew - e)/dt
    e = enew
    i = i + (1/dt)*e
    u = Kp*e + (Kp/Ti)*i + (Kp/Td)*d
    return u, e, i


x = 1.0
y = 2.0
e = None
i = 0.0

while True:
    u, e, i = compute_pid(x, y, e, i)
