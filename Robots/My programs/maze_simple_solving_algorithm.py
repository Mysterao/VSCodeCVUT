import time
import brian.sensors as sensors
import brian.motors as motors

object = sensors.EV3.UltrasonicSensorEV3(sensors.SensorPort.S2)
object.wait_until_ready()

color = sensors.EV3.ColorSensorEV3(sensors.SensorPort.S3)
color.wait_until_ready()