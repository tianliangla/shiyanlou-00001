#!/usr/bin/env python3

import sys

#print(len(sys.argv))
#gongzi = 0

try:
    if len(sys.argv) != 2 :
        raise ValueError
    gongzi = int(sys.argv[1])

except:
    print("Parameter Error")

#gongzi
#gongzi = int(sys.argv[1])

#baoxianfei set 0
baoxian = 0

#qizhengdian set 3500
qzd = 3500

#ying_nasui_suode_e
sde = gongzi - baoxian - qzd

#ying_nasui
yns = 0.00

if sde <= 1500 :
    yns = sde * 0.03 - 0
elif sde > 1500 and sde <= 4500:
    yns = sde * 0.1 - 105
elif sde > 4500 and sde <= 9000:
    yns = sde * 0.2 - 555
elif sde > 9000 and sde <= 35000:
    yns = sde * 0.25 - 1005
elif sde > 35000 and sde <= 55000:
    yns = sde * 0.3 - 2755
elif sde > 55000 and sde <= 80000:
    yns = sde * 0.35 - 5505
else :
    yns = sde * 0.45 - 13505

print(format(yns,".2f"))

