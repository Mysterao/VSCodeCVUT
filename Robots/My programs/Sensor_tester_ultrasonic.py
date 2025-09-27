import brian.sensors as sensors

# ADD ONLY IF YOU WANT TO START THE ROBOT BY BUTTON - PORT 1
# button = sensors.EV3.TouchSensorEV3(sensors.SensorPort.S1)
# button.wait_for_press()

object = sensors.EV3.UltrasonicSensorEV3(sensors.SensorPort.S2)

while True:
    print(object.distance_mm())