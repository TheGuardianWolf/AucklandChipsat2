import math

def compute(target_global, heading_global, b_target_local):

    def global_to_local(angle):
        return angle - heading_global

    heading_local = global_to_local(heading_global)  # identically zero
    target_local = global_to_local(target_global)
    delta = b_target_local - target_local  # b_target_local = target_local + delta
    b_generated_local = heading_local + delta
    a = b_generated_local  # save ink
    x = math.cos(a)
    y = math.sin(a)
    return x, y