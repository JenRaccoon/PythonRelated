#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup as bs
res = requests.get("https://technews.tw/")
tech = bs(res.text,"lxml")

# tech


# In[2]:


cat = tech.find_all('div',class_= "cat01")
sum_title = tech.find_all('div',class_="sum_title")
sum_title_url = tech.find_all('div', class_="img")
# sum_title[0].text.strip()


# In[3]:


spot_list_data = tech.find_all('li',class_="spotlist")
spot_list1 = []
for i in range(len(spot_list_data)):
    dic2_title = {}
    dic2_title['title'] = spot_list_data[i].text.strip()
    dic2_title['url'] = 'http:'+spot_list_data[i].find('a').get('href')
    spot_list1.append(dic2_title)

# spot_list1


# In[10]:


spot = []
for i in range(len(spot_list1)//3):
    dic = []
    spot_dic = {}
    dic.append(spot_list1[i])
    dic.append(spot_list1[i*3+1])
    dic.append(spot_list1[i*3+2])
    spot.append(dic)
#spot


# In[11]:


resultNew = []
for i in range(len(cat)):
    dic_title = {}
    dic_title['category'] = cat[i].text
    dic_title['sum_title'] = sum_title[i].text.strip()
    dic_title['sum_title_url'] = 'https:'+sum_title_url[i].find('a').get('href')
    dic_title['spotlist'] = spot[i]
    resultNew.append(dic_title)

#print(resultNew)


# In[6]:


import json

file_name = 'exam1_1.json'
with open(file_name,'w',encoding = 'utf8') as file_object:
    json.dump(resultNew,file_object,ensure_ascii=False)


# In[1]:


import json
with open("exam1_1.json","r",encoding = 'utf8') as f:
    data = json.load(f)
# data


# In[2]:


#輸出sum_
import requests
from bs4 import BeautifulSoup as bs
from lxml import html
from lxml import cssselect
for x in range(len(data)):
    page = data[x].get('sum_title_url')
    res_page = requests.get(page)
    page_bs = bs(res_page.text,"lxml")
    content = page_bs.select("div > div.entry-content > div.indent > p")
    
    category = data[x].get('category')
    sum_title = data[x].get('sum_title')
    file = "sum_{}_{:.4s}".format(category,sum_title)
    with open(file,"w",encoding='utf8') as f:
        for i in content:
            f.write(i.text)
            
#輸出spot_
for x in range(8):
    for y in range(3):
        page = data[x].get('spotlist')[y].get('url')
        res_page = requests.get(page)
        page_bs = bs(res_page.text,"lxml")
        content = page_bs.select("div > div.entry-content > div.indent > p")
#         print(x,y)
        category = data[x].get('category')
        sum_title = data[x].get('spotlist')[y].get('title')
        file = "spot_{}_{:.4s}".format(category,sum_title)
        with open(file,"w",encoding='utf8') as f:
            for i in content:
                f.write(i.text)


# In[ ]:




