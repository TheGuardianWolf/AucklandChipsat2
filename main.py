import time
import board
import busio
import analogio
import pulseio
from imu import IMU
from light import Light
from helpers import convert_duty


# Board Components
i2c = busio.I2C(board.SCL, board.SDA)
adc = analogio.AnalogIn(board.PA06)
pwm0 = pulseio.PWMOut(board.PA08, frequency=10000)
pwm1 = pulseio.PWMOut(board.PA09, frequency=10000)
pwm2 = pulseio.PWMOut(board.PA10, frequency=10000)

# Sensors
light = Light(adc)
imu = IMU(i2c, -1.34)

# Task Globals
light_max = 0
zero_point_last_light = 0
zero_point_gyro_angle = 0
zero_point_calibrated = False

# Tasks


def task_imu():
    imu.angle_update()
    mag_x, mag_y, mag_z = imu.get_mag()
    # print(imu.angle, mag_x, mag_y, mag_z)


def task_light():
    global light_max
    light_curr = light.get_value()

    if light_curr > light_max:
        light_max = light_curr


def task_zero_point():
    global zero_point_calibrated
    global zero_point_gyro_angle
    global zero_point_last_light

    if not zero_point_calibrated:
        if imu.raw_angle >= 360 or imu.raw_angle <= -360:
            zero_point_calibrated = True
            # print("calibrated with max_light {0} angle {1}".format(zero_point_last_light, zero_point_gyro_angle))

        if zero_point_last_light < light_max:
            zero_point_last_light = light_max
            zero_point_gyro_angle = imu.angle
            # print("max_light {0} angle {1}".format(zero_point_last_light, zero_point_gyro_angle))


def task_control():
    if zero_point_calibrated:
        # Run control
        pass

def task_log():
    print(light.get_value(), imu.raw_angle)

tasks = [
    {
        "name": "imu",
        "task": task_imu,
        "period": 0.05,
        "last_run": 0
    },
    {
        "name": "light",
        "task": task_light,
        "period": 0.1,
        "last_run": 0
    },
    {
        "name": "zero_point",
        "task": task_zero_point,
        "period": 0.1,
        "last_run": 0
    },
    {
        "name": "log",
        "task": task_log,
        "period": 0.2,
        "last_run": 0
    }
]

# System boot
time.sleep(1)

while True:
    runtime = time.monotonic()
    for task in tasks:
        if runtime - task["last_run"] >= task["period"]:
            task["task"]()
            task["last_run"] = runtime
