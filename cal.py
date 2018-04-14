#!/usr/bin/env python3
import sys
import csv


arg = sys.argv[1:]


if arg[0] == '-c' :
    filename_cfg = arg[1]
if arg[2] == '-d':
    filename_user = arg[3]
if arg[4] == '-o':
    filename_out = arg[5]


#保险费比例初始化0
baoxian_bl = 0.00
dict1 = {}
#filename_cfg = 'F:\\work\\python\\shiyanlou-00001\\test.cfg'    
try:
    with open(filename_cfg) as file:
        list_l0 = file.readlines()
        for list_s0 in list_l0:
            list_s = list_s0.split('=')
            dict1[list_s[0].strip()] = float(list_s[1].strip())
except:
    print("File Error or Format Error")
#print(dict1)
#dict1 = {'YangLao':0.08,'YiLiao':0.02,'ShiYe':0.005}

#baoxian_bl = 0.08 + 0.02 + 0.005 + 0.00 + 0.00 + 0.06
baoxian_bl = dict1['YangLao'] + dict1['YiLiao'] + dict1['ShiYe'] + dict1['GongShang'] + dict1['ShengYu'] + dict1['GongJiJin']

#print(format(baoxian_bl,".3f"))

dict2 = {}
#filename_user = 'F:\\work\\python\\shiyanlou-00001\\user.csv'
try:
    with open(filename_user) as file:
        list_l2 = file.readlines()
        for list_s02 in list_l2:
            list_s2 = list_s02.split(',')
            dict2[list_s2[0].strip()] = int(list_s2[1].strip())
except:
    print("File Error or Format Error")

#print(dict2)


result = []
for key,value in dict2.items() :
    #value = arg.split(':')
    try:
        #if len(sys.argv) != 2 :
        #    raise ValueError
        #gongzi = int(sys.argv[1])
        #gongzi = int(value[1])
        gongzi = value

    except:
        print("Parameter Error")

    #工资 gongzi
    #gongzi = int(sys.argv[1])

    #保险费初始化0
    baoxian = 0
    
    #养老保险8%--医疗保险2%--失业保险0.5%--工伤保险0%--生育保险0%--公积金6%
    #baoxian_bl = 0.08 + 0.02 + 0.005 + 0.00 + 0.00 + 0.06
    #baoxian_bl = YangLao + YiLiao + ShiYe + GongShang + ShengYu + GongJiJin
    baoxian = gongzi * baoxian_bl

    #起征点初始化为 3500
    qzd = 3500

    #应纳税所得额sde = 工资 － 各项保险费 －起征点
    sde = gongzi - baoxian - qzd
    #若应纳税所得额sde的结果为负数或0，则不需纳税
    if sde <= 0:
        sde = 0   

    #应纳税额yns为浮点数
    #应纳税俄＝应纳税所得额X税率－速算扣除数
    yns = 0.00


    #税率值不能直接用百分数，要转成浮点小数才可正常计算
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


    #税后工资sh_gz=工资gongzi-保险费baoxian-应纳税额yns
    sh_gz = gongzi - baoxian - yns

    #print(format(yns,".2f"))
    #print('{}:{}'.format(value[0],format(sh_gz,".2f")))
    #输出：工号，税前工资，社保金额，个税金额，税后工资
    #print('{}:{}:{}:{}:{}'.format(key,value,baoxian,yns,format(sh_gz,".2f")))
    #print('{}:{}'.format(key,format(sh_gz,".2f")))
    res_tuple1 = (key,value,format(baoxian,".2f"),format(yns,".2f"),format(sh_gz,".2f"))
    result.append(res_tuple1)

#result = ['101,3500,577.50,0.00,2922.50','203,5000,825.00,20.25,4154.75']
#filename_out = 'F:\\work\\python\\shiyanlou-00001\\gongzi.csv'
try:
    with open(filename_out,'w',newline='') as f:
        writer = csv.writer(f)
        writer.writerows(result)
except:
    print("File Error or Format Error")