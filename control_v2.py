import math

def pwm_levels(target_global, heading_global, b_target_local):
    '''
    Returns the PWM levels for x- and y- axes.
    
    Inputs: See "Figure: Code Explanation" in accompanying submission.
      target_global: Angle to target in global frame
      heading_global: Heading angle in global frame
      b_target_global: Angle of background magnetic field vector in global frame

    Output:
      x, y: PWM levels for x- and y-coils; sum to 1.0
    '''
    def global_to_local(angle):
        return angle - heading_global
    heading_local = global_to_local(heading_global)  # identically zero
    target_local = global_to_local(target_global)
    delta = b_target_local - target_local  # b_target_local = target_local + delta
    b_generated_local = heading_local + delta
    x = math.cos(b_generated_local)
    y = math.sin(b_generated_local)
    return x, y

# Test that math module import works on the device!
print(compute(1, 2, 3))