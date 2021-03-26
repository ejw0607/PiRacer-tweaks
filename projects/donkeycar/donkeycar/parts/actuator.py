class PWMThrottle:

# Wrapper over a PWM motor cotnroller to convert -1 to 1 throttle
# values to PWM pulses.

MIN_THROTTLE = -1
MAX_THROTTLE = 1

def __init__(self, controller=None,
                   max_pulse=4095,
                   min_pulse=-4095,
                   zero_pulse=0):

    self.controller = controller
    self.max_pulse = max_pulse
    self.min_pulse = min_pulse
    self.zero_pulse = zero_pulse
    
    #send zero pulse to calibrate ESC
    print("Init ESC")
    self.controller.set_pulse(self.zero_pulse)
    time.sleep(1)


def run(self, throttle):
    if throttle > 0:
        pulse = dk.utils.map_range(throttle,
                                0, self.MAX_THROTTLE, 
                                self.zero_pulse, self.max_pulse)
        self.controller.pwm.set_pwm(self.controller.channel,0,pulse)
        self.controller.pwm.set_pwm(self.controller.channel+1,0,0)
        self.controller.pwm.set_pwm(self.controller.channel+2,0,4095)
        self.controller.pwm.set_pwm(self.controller.channel+3,0,0)
        self.controller.pwm.set_pwm(self.controller.channel+4,0,pulse)
        self.controller.pwm.set_pwm(self.controller.channel+7,0,pulse)
        self.controller.pwm.set_pwm(self.controller.channel+6,0,0)
        self.controller.pwm.set_pwm(self.controller.channel+5,0,4095)
    else:
        pulse = dk.utils.map_range(throttle,
                                self.MIN_THROTTLE, 0, 
                                self.min_pulse, self.zero_pulse)
        #added in these 4, uncommented.
        #self.controller.pwm.set_pwm(self.controller.channel,0,self.zero_pulse)
        #self.controller.pwm.set_pwm(self.controller.channel,0,pulse)
        #self.controller.pwm.set_pwm(self.controller.channel,0,self.zero_pulse)
        #self.controller.pwm.set_pwm(self.controller.channel,0,pulse)
         
         self.controller.pwm.set_pwm(self.controller.channel,0,- pulse)
         self.controller.pwm.set_pwm(self.controller.channel+2,0,0)
         self.controller.pwm.set_pwm(self.controller.channel+1,0,4095)
         self.controller.pwm.set_pwm(self.controller.channel+3,0,- pulse)
         self.controller.pwm.set_pwm(self.controller.channel+4,0,0)
         self.controller.pwm.set_pwm(self.controller.channel+7,0,- pulse)
         self.controller.pwm.set_pwm(self.controller.channel+5,0,0)
         self.controller.pwm.set_pwm(self.controller.channel+6,0,4095)
         

def shutdown(self):
    self.run(0) #stop vehicle
