import post_to_web as PTW

######## Gobal Variables ########

motorLpin = 0
motorRpin= 1
sensor1pin = 16
sensor2pin = 17

space = '&nbsp' # half a character
separator = '#' * 63

def setupSensor(x):
    sensor_pin = x
    RPL.pinMode(sensor_pin,RPL.INPUT)

setupSensor(sensor1pin)
setupSensor(sensor2pin)

while True:

    # Current value being sent to motors
    motorL = 1
    motorR = 2

    # Get sensor readings
    sensor1 = RPL.digitalRead(sensor1pin)
    sensor2 = RPL.digitalRead(sensor2pin)


    # Message displayed on html site
    readings = """
    %s <br />
    ## %s Motor Readings %s ## <br />
    %s <br />
    motor L: %d <br />
    motor R: %d <br />

    <br /><br />

    %s <br />
    ## %s Sensor Readings %s ## <br />
    %s <br />
    Sensor %d: %d <br />
    Sensor %d: %d <br />
    """ % (separator, space * 56, space * 56, separator, motorL, motorR, separator, space \
    * 55, space * 55, separator, sensor1pin, sensor1, sensor2pin, sensor2)

    # Write to readings.txt temp file
    PTW.send(readings)
