class Light(object):
    def __init__(self, adc):
        self.adc = adc

    def get_value(self):
        return 65535 - self.adc.value
