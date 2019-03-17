import math

def compute(target_global, heading_global, b_target_local):
    def global_to_local(angle):
        return angle - heading_global
    heading_local = global_to_local(heading_global)  # identically zero
    target_local = global_to_local(target_global)
    delta = b_target_local - target_local  # b_target_local = target_local + delta
    b_generated_local = heading_local + delta
    x = math.cos(b_generated_local)
    y = math.sin(b_generated_local)
    return x, y

print(compute(1, 2, 3))