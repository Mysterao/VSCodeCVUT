import brian.sensors as sensors
import brian.motors as motors
from time import sleep

# ADD ONLY IF YOU WANT TO START THE ROBOT BY BUTTON - PORT 1
# button = sensors.EV3.TouchSensorEV3(sensors.SensorPort.S1)
# button.wait_for_press()

color = sensors.EV3.ColorSensorEV3(sensors.SensorPort.S3)
object = sensors.EV3.UltrasonicSensorEV3(sensors.SensorPort.S2)

motor_a = motors.EV3LargeMotor(motors.MotorPort.A)
motor_a.wait_until_ready()

motor_b = motors.EV3LargeMotor(motors.MotorPort.B)
motor_b.wait_until_ready()

def obstacle(motor_a, motor_b, color):
    motor_a.brake()
    motor_b.brake()
    motor_a.rotate_by_angle(100, 300, False) # Agjust the parameter for robot to turn accordingly after stopping before an obstacle
    motor_b.rotate_by_angle(-100, 300)
    
    black_again = False
    while black_again == False:
        motor_a.run_at_speed(-300)
        motor_b.run_at_speed(300)
        if color.reflected_value() < 50:
            black_again = True

while True:
    if object.distance_mm() < 50: # Distance threshold for obstacle, triggers if object is closer than 50 mm
        obstacle(motor_a, motor_b)
    if color.reflected_value() > 50: # Vidím bílou
        motor_a.run_at_speed(300)
        motor_b.run_at_speed(-300) # Zatáčím doleva
    else: # Vidím černou
        motor_a.run_at_speed(-300)
        motor_b.run_at_speed(300) # Zatáčam vpravo