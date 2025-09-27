import brian.sensors as sensors

# ADD ONLY IF YOU WANT TO START THE ROBOT BY BUTTON - PORT 1
# button = sensors.EV3.TouchSensorEV3(sensors.SensorPort.S1)
# button.wait_for_press()
color = sensors.EV3.ColorSensorEV3(sensors.SensorPort.S3)

while True:
    print(color.reflected_value())