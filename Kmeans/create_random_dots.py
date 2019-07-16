import random
from matplotlib.pyplot import *

all_points=[]
for i in range(20):
    generate_date=[random.randint(1,100),random.randint(1,100)]
    if not generate_date in all_points:
        all_points.append(generate_date)

for i in range(20):
    plot(all_points[i][0],all_points[i][1],"x")

show()
print(all_points)

