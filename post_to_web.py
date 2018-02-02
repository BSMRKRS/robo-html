## Thanks for using post to web!
################################

#Begin with incude post_to_web as PTW
#put PTW.send(x) somewhere in your loop
#visit 192.168.21.x to view your dashboard

f = open('readings.txt','r+')

def send(text):
  f.seek(0)
  f.write('let msg = `' + str(text)+'`;')
  f.truncate()
