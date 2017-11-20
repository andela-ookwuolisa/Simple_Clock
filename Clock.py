class Clock:
  count = 0
  def __init__(self, hours=0, minutes=0, seconds=0):
    Clock.count += 1 
    self.__hours = hours
    self.__minutes = minutes
    self.__seconds = seconds

  def get_time(self):
    return (self.__hours, self.__minutes, self.__seconds)

  def set_time(self, hours, minutes, seconds):
    self.__hours = hours
    self.__minutes = minutes
    self.__seconds = seconds

  # abstraction and encapsulation. Private variables can only be accessed with getters and setters
  def set_hours(self, hours):
    self.__hours = hours
  

  def get_hours(self):
    return self.__hours

  def set_minutes(self, minutes):
    self.__minutes = minutes
  

  def get_minutes(self):
    return self.__minutes

  def set_seconds(self, seconds):
    self.__seconds = seconds
  

  def get_seconds(self):
    return self.__seconds

  def tick(self):
    if (self.__seconds == 59):
      self.__seconds = 0
      if (self.__minutes == 59):
        self.__minutes = 0
        if (self.__hours == 23):
          self.__hours = 0
        else:
          self.__hours += 1
      else:
        self.__minutes += 1
    else:
      self.__seconds += 1