def sign():
    return (1, -1)[x < 0]


def convert_duty(duty_percentage):
    return int(65535 * duty_percentage)
