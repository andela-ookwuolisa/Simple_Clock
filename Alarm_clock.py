from Clock import Clock
# Inheritance: Alarm_Clock is a subclass of Clock.
class Alarm_Clock(Clock):
  def __init__(self, hours = 0, minutes = 0, seconds = 0):
    Clock.__init__(self,hours, minutes, seconds)
    self.__Alarm_hours = 0
    self.__Alarm_minutes = 0
    self.__Alarm_seconds = 0
  
  # Setting a default value on the arguments permits method overloading
  def set_alarm(self, Alarm_hours, Alarm_minutes=0, Alarm_seconds=0):
    self.__Alarm_hours = Alarm_hours
    self.__Alarm_minutes = Alarm_minutes
    self.__Alarm_seconds = Alarm_seconds
  
  # Polymorphism: tick() has same method name and argument as the super class, but diferent implementations
  def tick(self):
    if  ((self.__Alarm_hours == self.get_hours()) and (self.__Alarm_minutes == self.get_minutes())
    and (self.__Alarm_seconds == self.get_seconds())):
      print ('Alarm Ring!')
      return
    if (self.get_seconds() == 59):
      self.set_seconds(0)
      if (self.get_minutes() == 59):
        self.set_minutes(0)
        if (self.get_hours == 23):
          self.set_hours(0)
        else:
          self.set_hours(self.get_hours()+1)
      else:
        self.set_minutes(self.get_minutes()+1)
    else:
      self.set_seconds(self.get_seconds()+1)
