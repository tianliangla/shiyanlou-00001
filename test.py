#!/usr/bin/env python3
import sys
import csv


dict1 = {}
filename_cfg = 'F:\\work\\python\\shiyanlou-00001\\test.cfg'
with open(filename_cfg) as file:
    list_l0 = file.readlines()
    for list_s0 in list_l0:
        list_s = list_s0.split('=')
        dict1[list_s[0].strip()] = float(list_s[1].strip())

#print(dict1)
#dict1 = {'YangLao':0.08,'YiLiao':0.02,'ShiYe':0.005}

#baoxian_bl = 0.08 + 0.02 + 0.005 + 0.00 + 0.00 + 0.06
baoxian_bl = dict1['YangLao'] + dict1['YiLiao'] + dict1['ShiYe'] + dict1['GongShang'] + dict1['ShengYu'] + dict1['GongJiJin']

print(format(baoxian_bl,".3f"))

dict2 = {}
filename_user = 'F:\\work\\python\\shiyanlou-00001\\user.csv'
with open(filename_user) as file:
    list_l2 = file.readlines()
    for list_s02 in list_l2:
        list_s2 = list_s02.split(',')
        dict2[list_s2[0].strip()] = float(list_s2[1].strip())


print(dict2)

result = ['101,3500,577.50,0.00,2922.50','203,5000,825.00,20.25,4154.75']
filename_out = 'F:\\work\\python\\shiyanlou-00001\\gongzi.csv'
with open(filename_out,'w',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(result)


