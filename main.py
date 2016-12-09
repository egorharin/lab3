import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

from uid import *
from friends import *

input_id = input('Введите id: ')
user = GetID(input_id)
user_id = user.execute()

friends_client = GetFriends(user_id)
friends = friends_client.execute()

ages = []
counts = []

for (age, count) in friends:
    print('{} {}'.format(int(age), int(count)))
    ages.append(int(age))
    counts.append(int(count))

plt.grid()
plt.minorticks_on()
plt.axis([0, 120, 0, 50])
plt.figure(num=1, figsize=(8, 6))
plt.xlabel('age', size=14)
plt.ylabel('count', size=14)
plt.bar(ages, counts, width=0.5)
plt.show()
