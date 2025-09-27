import brian.sensors as sensors
import brian.motors as motors

# ADD ONLY IF YOU WANT TO START THE ROBOT BY BUTTON - PORT 1
# button = sensors.EV3.TouchSensorEV3(sensors.SensorPort.S1)
# button.wait_for_press()

color = sensors.EV3.ColorSensorEV3(sensors.SensorPort.S3)

motor_a = motors.EV3LargeMotor(motors.MotorPort.A)
motor_a.wait_until_ready()

motor_b = motors.EV3LargeMotor(motors.MotorPort.B)
motor_b.wait_until_ready()

while True:
    if color.reflected_value() > 50: # Vidím bílou
        motor_a.run_at_speed(300)
        motor_b.run_at_speed(-300) # Zatáčím doleva
    else: # Vidím černou
        motor_a.run_at_speed(-300)
        motor_b.run_at_speed(300)