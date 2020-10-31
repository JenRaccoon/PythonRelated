from datetime import datetime 
t = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
import csv
import pandas as pd
from datetime import datetime 



def new_file():
    import csv
    import pandas as pd
    
       
    name=['姓名','性別','年齡','身分證字號',"電話","病史 / 過敏史 / 目前用藥","初診日期","病歷代碼"]
    patient_list=[]
    patient_list = pd.DataFrame(columns=name,data=patient_list)
    patient_list.to_csv('patient.csv',encoding='utf-8')
    print(patient_list)

def show_menu():
# 主選單
    print("═" * 50)
    print("")
    print("  ╭╮　　╭╮　")
    print(" ╭＊════＊╮　 　")
    print(" ／／／／ )    ")
    print(" (│ ●ˍ● │)   ")
    print(" (╰┬○─○┬╯) 　　")
    print("")
    print("(﹌)____(﹌)")
    print("◆◆歡迎使用◆◆")
    print("")
    print("1. 建立新病歷表(首次紀錄請務必建立) / 清除病歷表資料(歷史資料會清空) ")
    print("2. 新增病患")
    print("3. 查詢病患")
    print("4. 刪除病患")
    
    print("5. 建立新帳單(首次記帳請先建立)/ 清除帳本(歷史記帳會清空)")
    print("6. 線上記帳")
    print("7. 入帳筆數/日")
    print("")
    print("0. 退出系統")
    print("═" * 50)

def new_patient():
    import pandas as pd
    
    df = pd.read_csv('patient.csv')

    patient_list=df.drop(df.columns[0],axis=1) 

   
    print("═" * 50)
    print("功能：新增患者")

   
    t = datetime.now().strftime('%Y-%m-%d')
    P_name = input("請輸入姓名：")
    sex = input("請輸入性別:")
    age = input("請輸入年齡:")
    ID = input("請輸入身分證字號：")
    phone = input("請輸入電話:")
    history = input("請輸入病史:")   
    # day = input("初診日期:")
    num = input("病歷代碼:")
    
    patient_dict = {"姓名": P_name,"性別": sex,"年齡": age,"身分證字號": ID,"電話": phone,"病史": history,"初診日期": t,"病歷代碼":num}
    patient_list=patient_list.append(patient_dict,ignore_index=True)
    t = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    print("新增成功")
    
    name=['姓名','性別','年齡','身分證字號',"電話","病史","初診日期","病歷代碼"]
    patient_list=pd.DataFrame(columns=name,data=patient_list)
    patient_list.to_csv('patient.csv',encoding='utf-8')
    a=len(patient_list)
    print("═" * 25)
    print("患者新增在第",a-1,"筆")
    print("═" * 25)
    print(pd.read_csv('patient.csv'))
    
        

            
def search_card():
    import pandas as pd
    print("═" * 50)
    print("功能：查詢患者資料")

    inputID = input("請輸入病患身分證：")
    
    patient_history=pd.read_csv('patient.csv')
    
    a = patient_history["身分證字號"] == inputID
    if a.bool:
        patient_history=pd.read_csv('patient.csv')
        filter= patient_history["身分證字號"] == inputID
        print(patient_history[filter])
    else:
        print("沒有此患者")  
        
def delete_patient():
    import pandas as pd
    print("═" * 50)
    print("功能：刪除患者資料")
    find_ID = str(input("請輸入病患身分證："))

    lines = list()
    with open('patient.csv','r',encoding='utf-8')as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            lines.append(row)
            for field in row:
                if field  == find_ID :
                    print("刪除下列資料!")
                    print("刪除患者為:",row)
                    lines.remove(row)
                        
    with open('patient.csv','w',encoding='utf-8')as writeFile:
        writer=csv.writer(writeFile)
        writer.writerows(lines)


    print("═" * 60)
    
