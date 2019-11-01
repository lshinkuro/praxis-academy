

import statistics
import random

data = random.sample(range(1000),10)

# data=[3,8,9,0,8,7,6]
print("data saya adalah :" + str(data))

a=statistics.mean(data)
print(a)
median =statistics.median(data)
print("nilai medianya adala:" +str(median))
varian =statistics.variance(data)
print(varian)