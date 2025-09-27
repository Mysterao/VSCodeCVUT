# import brian.sensors as sensors
import brian.motors as motors
from time import sleep

# ADD ONLY IF YOU WANT TO START THE ROBOT BY BUTTON - PORT 1
# button = sensors.EV3.TouchSensorEV3(sensors.SensorPort.S1)
# button.wait_for_press()

# color = sensors.EV3.ColorSensorEV3(sensors.SensorPort.S3)

motor_a = motors.EV3LargeMotor(motors.MotorPort.A)
motor_a.wait_until_ready()

motor_b = motors.EV3LargeMotor(motors.MotorPort.B)
motor_b.wait_until_ready()

# Test run both motors
motor_a.run_at_speed(300)
motor_b.run_at_speed(300)
sleep(1) # Wait

# Test run turning
motor_a.rotate_by_angle(100, 300, False)
motor_b.rotate_by_angle(-100, 300)