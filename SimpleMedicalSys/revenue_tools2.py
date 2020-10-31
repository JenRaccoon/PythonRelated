import pandas as pd
import time
import csv
from datetime import datetime 

    




def new_account():
    Money_list=[]
    name=['姓名','日期','金額']
    Money_list=pd.DataFrame(columns=name,data=Money_list)
    Money_list.to_csv('Money.csv',encoding='utf-8')
    print(Money_list)
    
def account():
    
    import pandas as pd
    from datetime import datetime 
    import time
    
    print("═" * 50)
    print("功能：紀錄營收")
    
    Money_list=[]
    df = pd.read_csv('Money.csv')
    Money_list = df.drop(df.columns[0],axis=1)
   

    Name = input("請輸入姓名：")
    money = input("請輸入金額：")
    Dayinput =eval( input("是否自行輸入日期?(1:自行輸入/2:顯示當日)"))
    if Dayinput== 1 :
        time = input("輸入日期")
    elif Dayinput==2 :
        time = time.strftime("%Y%m%d", time.localtime()) 


    Money_dict = {"姓名": Name,"日期":time,"金額":money}
    
    Money_list = Money_list.append(Money_dict,ignore_index=True)
    print(Money_list)

    name=['姓名','日期','金額']
    Money_list=pd.DataFrame(columns=name,data=Money_list)
    Money_list.to_csv('Money.csv',encoding='utf-8')
    x=pd.read_csv('Money.csv')
    x=pd.DataFrame(x,columns=['姓名','日期','金額'])

def people():
    
    import pandas as pd
    import time
    
    print("═" * 50)
    print("功能：統計人數")
    
    time = time.strftime("%Y%m%d", time.localtime()) 
    revenue = pd.read_csv('Money.csv')
    Day = eval(input("請輸入日期："))
    filter_M = revenue['日期'] == Day
    revenue[filter_M ]
    count = (revenue['日期'] == Day).sum()
    print(Day,"共",count,"筆收入")
    x=revenue['金額'].values
    sum=0
    for i in range(len(x)):
        sum = x[i] +sum
    print(Day,"總收入:",sum)
