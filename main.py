#!/usr/bin/python

flag = 0

while 1:
    print ('welcome')
    a = int(input('请输入数学成绩：'))
    if a == 100:
        print('特别棒')
    elif a > 80:
        print('不错')

    elif a > 60:
        print('别活了')

    if a > 100:
        print("你别乱输入")



print ("Good bye!")