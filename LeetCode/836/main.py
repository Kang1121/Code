import numpy as np


rec1 = [0,0,2,2]
rec2 = [1,1,3,3]

if rec1 == rec2:
    print(True)

if ((rec1[0] == rec2[0]) & (rec1[2] == rec2[2])):
    if ((rec1[1] > rec2[1]) & (rec1[1] < rec2[3])) | ((rec1[3] > rec2[1]) & (rec1[3] < rec2[3])):
        print(True)
    else:
        print(False)
if ((rec1[1] == rec2[1]) & (rec1[3] == rec2[3])):
    if ((rec1[0] > rec2[0]) & (rec1[0] < rec2[2])) | ((rec1[2] > rec2[0]) & (rec1[2] < rec2[2])):
        print(True)
    else:
        print(False)
a1 = (rec1[2] - rec1[0]) * (rec1[2] - rec1[0]) + (rec1[3] - rec1[1]) * (rec1[3] - rec1[1])
a2 = (rec2[2] - rec2[0]) * (rec2[2] - rec2[0]) + (rec2[3] - rec2[1]) * (rec2[3] - rec2[1])
# print(1)
if a1 > a2:
    max = rec1
    min = rec2
else:
    max = rec2
    min = rec1

if ((min[0] > max[0]) & (min[0] < max[2]) & (min[3] > max[1]) & (min[3] < max[3])) | ((min[2] > max[0]) & (min[2] < max[2]) & (min[1] > max[1]) & (min[1] < max[3])) | ((min[0] > max[0]) & (min[0] < max[2]) & (min[1] > max[1]) & (min[1] < max[3])) | ((min[2] > max[0]) & (min[2] < max[2]) & (min[3] > max[1]) & (min[3] < max[3])):
    print(True)
else:
    print(False)