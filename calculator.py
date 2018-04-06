#!/usr/bin/env python3

import sys

#print(len(sys.argv))
#gongzi = 0
#arg = sys.argv[1:]

#命令行参数技巧：
#先用 sys.argv[1:]切片存储多个命令行参数
#参数列表是 sys.argv[1:]（这种切片的方式是去掉第一个 sys.argv[0]之后的参数列表），
#然后使用 for 循环取出每个参数 for arg in sys.argv[1:]:，
# arg 的值类似 101:3500 的字符串，然后使用这个字符串的 arg.split(':') 分成两部分
# 的列表，前一部分是101，后面的是 3500，注意这都是字符串，再使用 int() 转成数字。

for arg in sys.argv[1:] :
    value = arg.split(':')
    try:
        #if len(sys.argv) != 2 :
        #    raise ValueError
        #gongzi = int(sys.argv[1])
        gongzi = int(value[1])

    except:
        print("Parameter Error")

    #工资 gongzi
    #gongzi = int(sys.argv[1])

    #保险费初始化0
    baoxian = 0
    #保险费比例初始化0
    baoxian_bl = 0.00
    #养老保险8%--医疗保险2%--失业保险0.5%--工伤保险0%--生育保险0%--公积金6%
    baoxian_bl = 0.08 + 0.02 + 0.005 + 0.00 + 0.00 + 0.06
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
    print('{}:{}'.format(value[0],format(sh_gz,".2f")))

