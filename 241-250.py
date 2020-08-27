#241
import time
import datetime
import os

print(datetime.datetime.now())

#242
print(type(datetime.datetime.now()))

#243
now = datetime.datetime.now()
for day in range(5, 0, -1):
    delta = datetime.timedelta(days=day)
    date = now - delta
    print(date)

#244
a = datetime.datetime.now().strftime("%H:%M:%S")
print(datetime.datetime.now().strftime("%H:%M:%S"))
print(type(a))

#245
print(datetime.datetime.strptime("2020-05-04","%Y-%m-%d"))
b = datetime.datetime.strptime("2020-05-04","%Y-%m-%d")
print(type(b))

#246
'''
while True:
    now = datetime.datetime.now()
    print(now)
    time.sleep(1)
'''

#247
import math
from math import *

#248
print(os.getcwd())

#249

#250
import numpy as np
for i in np.arange(0, 5.1, 0.1):
    print(i)
