## Thanks for using post to web!
################################

#Begin with incude post_to_web as PTW
#put PTW.post() somewhere in your loop
#update the PTW.state dictionary with your data
#visit 192.168.21.x to view your dashboard

import time

global tState
tState = time.time()
global state
state = dict()
#print 'ptw', state, tState

f = open('/home/student/robo-html/readings.txt','r+')

def send(d):
  f.seek(0)
  msg = (',').join(map(lambda reading: str(reading) + '=' + str(d[reading]), d.keys()))
  f.write('let msg = `' + msg+'`;')
  f.truncate()

def post(interval = 0.5):
  global tState
  if time.time() - tState > interval:
    send(state)
    tState = time.time()
