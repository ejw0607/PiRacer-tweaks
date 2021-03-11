# all values have been modified in the myconfig.py file

PCA9685_I2C_ADDR = 0x40 #steering I2C address, use i2cdetect to validate this number
PCA9685_I2C_ADDR1 = 0x40 #throttle I2C address, use i2cdetect to validate this number

#STEERING
STEERING_CHANNEL = 1 #channel on the 9685 pwm board 0-15
STEERING_LEFT_PWM = 420 #pwm value for full left steering
STEERING_RIGHT_PWM = 290 #pwm value for full right steering

#THROTTLE
THROTTLE_CHANNEL = 0 #channel on the 9685 pwm board 0-15
THROTTLE_FORWARD_PWM = 500 #pwm value for max forward throttle
THROTTLE_STOPPED_PWM = 370 #pwm value for no movement
THROTTLE_REVERSE_PWM = 220 #pwm value for max reverse throttle
