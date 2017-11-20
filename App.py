from Clock import Clock
from Alarm_clock import Alarm_Clock

first_clock = Clock()
My_alarm_clock = Alarm_Clock()

print (first_clock.get_time())
first_clock.set_time(5,8,54)
print (first_clock.get_time())

for i in range(7):
  first_clock.tick() # parent method
  print (first_clock.get_time())

My_alarm_clock.set_time(2,59,55)
My_alarm_clock.set_alarm(3) # method overloading
# import pdb; pdb.set_trace()
print (My_alarm_clock.get_time())
for i in range(10):
  My_alarm_clock.tick() # child method
  print (My_alarm_clock.get_time())

My_alarm_clock.set_time(10,59,55)
My_alarm_clock.set_alarm(11,0,3) # method overloading
print (My_alarm_clock.get_time())
for i in range(10):
  My_alarm_clock.tick()
  print (My_alarm_clock.get_time())

print ('Clock count:',My_alarm_clock.count) #class variable
