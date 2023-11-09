# from django.test import TestCase
from entities import Event, Day, Month
# Create your tests here.


event = Event(time='10:00', value='')
event2 = Event(time='12:00', value='8923')
day = Day(number=1, day_of_week='Понедельник', events=[event, event2])
print(day.to_dict())
