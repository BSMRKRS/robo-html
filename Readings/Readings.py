import RoboPiLib as RPL
RPL.RoboPiInit("/dev/ttyAMA0",115200)

def setupSensor(x):
    sensor_pin = x
    RPL.pinMode(sensor_pin,RPL.INPUT)

def ui():
    global sensorPinList, motorPinList

    print "#" * 60
    print "How many motors do you have?"
    numMotors = input("$: ")
    motorPinList = []
    if numMotors > 0:
        print "#" * 60
        print "What is the number of the first pin for your sensors (need to \nuse pins next to each other)"
        motorPin = input("$: ")
        print "#" * 60
        for i in range(0, numMotors):
            x = motorPin + i
            motorPinList.append(x)

    print "How many sensors are on your robot"
    numSensors = input("$: ")
    print "#" * 60
    sensorPinList = []
    if numSensors > 0:
        print "What is the number of the first pin for your sensors (need to \nuse pins next to each other)"
        sensorPin = input("$: ")
        print "#" * 60
        for i in range(0, numSensors):
            x = sensorPin + i
            setupSensor(x)
            sensorPinList.append(x)

space = '&nbsp' # half a character
separator = '#' * 63

def motorMsg():
    motorMessage = """
    %s <br />
    ## %s Motor Readings %s ## <br />
    %s <br />
    """ % (separator, space * 56, space * 56, separator)
    for i in motorPinList:
        motorMessage = motorMessage + "Motor " + str(i) + " = "  + str(RPL.servoRead(i)) + "<br />"
    return motorMessage

def sensorMsg():
    sensorMessage = """
    %s <br />
    ## %s Sensor Readings %s ## <br />
    %s <br />
    """ % (separator, space * 55, space * 55, separator)
    for i in sensorPinList:
        sensorMessage = sensorMessage + "Sensor " + str(i) + " = "  + str(RPL.digitalRead(i)) + "<br />"
    return sensorMessage

f = open('readings.txt','r+')

def writeReadings(text):
  f.seek(0)
  f.write('let msg = `' + str(text)+'`;')
  f.truncate()

ui()
while True:

    f = motorMsg() + ("<br />"*2) + sensorMsg()

    #Write to readings.txt temp file
    writeReadings(f)
