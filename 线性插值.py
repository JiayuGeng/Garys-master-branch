import math

def insert_num(x,y,num_list):
    last_x,last_y=num_list[-1][0],num_list[-1][1]
    step=math.trunc((y-last_y)/(x-last_x))
    for num in range(1,x-last_x):
        num_list.append([last_x+num,last_y+step*num])
while True:
    try:
        m,n=[int(i) for i in input().split()]
        num_list=[]
        for i in range(int(m)):
            x,y=[int(j) for j in input().split()]
            if len(num_list)>0:
                if num_list[-1][0]==x:
                    continue
                elif num_list[-1][0]+1<x:
                    insert_num(x,y,num_list)
                    num_list.append([x,y])
                else:
                    num_list.append([x,y])
            else:
                num_list.append([x,y])
        for number in num_list:
            print (number[0],number[1])
    except:
        break