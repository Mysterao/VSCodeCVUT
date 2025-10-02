import time
import brian.sensors as sensors
import brian.motors as motors
import brian.audio as audio
import math

# Component initialization --------------------------------------
object = sensors.EV3.UltrasonicSensorEV3(sensors.SensorPort.S2)
object.wait_until_ready()

color = sensors.EV3.ColorSensorEV3(sensors.SensorPort.S3)
color.wait_until_ready()

button = sensors.EV3.TouchSensorEV3(sensors.SensorPort.S1)
button.wait_until_ready()

motor_a = motors.EV3LargeMotor(motors.MotorPort.A)
motor_a.wait_until_ready()

motor_b = motors.EV3LargeMotor(motors.MotorPort.B)
motor_b.wait_until_ready()
# ---------------------------------------------------------------

#Plays tones before the match starts
button.wait_for_press()
audio.play_tone(880, 250)
time.sleep(0.75)
audio.play_tone(880, 250)
time.sleep(0.75)
audio.play_tone(880, 250)
time.sleep(0.75)
audio.play_tone(880, 250)
time.sleep(0.75)
audio.play_tone(100, 1000)
# ----------------------------------

# Turn the robot around --------------------
motor_a.rotate_by_angle(-240, 360, False)
motor_b.rotate_by_angle(240, 360)
time.sleep(0.5)
# ------------------------------------------

turn_back = 1 # Kedy otocit robota
current_turn = 0 # Otacanie, pocas ktoreho skenujeme objekt
max_turn = 360 # Maximalne otocenie
while object.distance_mm() > 300: #Toto bude asi viac, da sa spravit aj podla timeu
    motor_a.run_at_speed(200) # Toto zmen podla tocenia robota
    motor_b.run_at_speed(300)
    turn_back += 1
    if turn_back%301 == 0: # Toto zmen podla tocenia robota 300 JEDNOTIEK POHYBU !!!
        while current_turn != max_turn and object.distance_mm() > 300:
            motor_a.rotate_by_angle(-current_turn, 360, False) # Toci robota do druhej strany
            motor_b.rotate_by_angle(current_turn, 360)
            current_turn += 10 # Neviem, ako rychlo prejde jeden cyklus

while color.reflected_value > 20:
    if object.distance_mm() > 300:
        # seek_box(motor_a, motor_b)
        max_turn = 90
        current_turn = -90
        while current_turn != max_turn and object.distance_mm() > 300:
            motor_a.rotate_by_angle(current_turn, 360, False)
            motor_b.rotate_by_angle(-current_turn, 360)
            current_turn += 10 # Not sure how much will the robot turn by 1 step
    else:
        motor_a.run_at_speed(300)
        motor_b.run_at_speed(300)

motor_a.run_at_speed(-200)
motor_b.run_at_speed(-200)
time.sleep(0.5)

while True:
    motor_a.rotate_by_angle(-720, 360, False)
    motor_b.rotate_by_angle(720, 360)