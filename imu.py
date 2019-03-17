import time
import board
import busio
import adafruit_lsm9ds1


class IMU(object):
    def __init__(self, bus, angle_bias=-1.34):
        self.bus = bus
        self.sensor = adafruit_lsm9ds1.LSM9DS1_I2C(bus)
        self.angle = 0
        self.raw_angle = 0
        self.gyro_x = 0
        self.angle_bias = angle_bias
        self.last_time = time.monotonic()

    def angle_update(self):
        current_time = time.monotonic()
        gyro_x, gyro_y, gyro_z = self.get_gyro()
        self.gyro_z = gyro_z
        timestep = current_time - self.last_time
        angle_increment = gyro_z * timestep - (timestep * self.angle_bias)
        self.angle = (self.angle + angle_increment) % 360
        self.raw_angle += angle_increment
        self.last_time = current_time

    def angle_reset(self):
        self.angle = 0
        self.raw_angle = 0

    def get_mag(self):
        return self.sensor.magnetic

    def get_gyro(self):
        return self.sensor.gyro


class KalmanFilter(object):
    def __init__(self, process_variance, estimated_measurement_variance):
        self.process_variance = process_variance
        self.estimated_measurement_variance = estimated_measurement_variance
        self.posteri_estimate = 0.0
        self.posteri_error_estimate = 1.0

    def input_latest_noisy_measurement(self, measurement):
        priori_estimate = self.posteri_estimate
        priori_error_estimate = self.posteri_error_estimate + self.process_variance

        blending_factor = priori_error_estimate / (priori_error_estimate + self.estimated_measurement_variance)
        self.posteri_estimate = priori_estimate + blending_factor * (measurement - priori_estimate)
        self.posteri_error_estimate = (1 - blending_factor) * priori_error_estimate

    def get_latest_estimated_measurement(self):
        return self.posteri_estimate
