# scroll down through the manage.py file until it matches the code below. Modified code has been commented so it is easily identifiable.


#Drive train setup
if cfg.DONKEY_GYM:
pass
elif cfg.DRIVE_TRAIN_TYPE == "SERVO_ESC":
    from donkeycar.parts.actuator import PCA9685, PWMSteering, PWMThrottle
    
    # add in frequency=60 because supposedly the PCA9685 doesn't support individual frequency. 
    steering_controller = PCA9685(cfg.STEERING_CHANNEL, cfg.PCA9685_I2C_ADDR, frequency=60, busnum=cfg.PCA9685_I2C_BUSNUM)
    steering = PWMSteering(controller=steering_controller,
                                    left_pulse=cfg.STEERING_LEFT_PWM, 
                                    right_pulse=cfg.STEERING_RIGHT_PWM)
    
    # change frequency to 60
    throttle_controller = PCA9685(cfg.THROTTLE_CHANNEL, cfg.PCA9685_I2C_ADDR1, frequency=60, busnum=cfg.PCA9685_I2C_BUSNUM)
    throttle = PWMThrottle(controller=throttle_controller,
                                    max_pulse=cfg.THROTTLE_FORWARD_PWM,
                                    zero_pulse=cfg.THROTTLE_STOPPED_PWM, 
                                    min_pulse=cfg.THROTTLE_REVERSE_PWM)

    V.add(steering, inputs=['angle'])
    V.add(throttle, inputs=['throttle'])
