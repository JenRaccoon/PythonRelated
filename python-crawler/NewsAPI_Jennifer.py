#!/usr/bin/env python
# coding: utf-8

# In[1]:


from newsapi import NewsApiClient
API_KEY = 'e5198c27d35d4b25bde13c560a3b14f7'

import datetime as dt
import pandas as pd


# In[2]:


newsapi = NewsApiClient(api_key = API_KEY)
# data = newsapi.get_everything(q = "武漢肺炎 NOT 外遇",page_size = 100 )
all_articles =newsapi.get_everything(q='武漢肺炎 NOT 外遇',
                                      domains='ettoday.net,storm.mg,chinatimes.com,udn.com',
                                      from_param='2020-05-05',
                                      to='2020-06-05',
                                      language='zh',
                                      sort_by='publishedAt',
                                      page_size=100
                                      )
all_articles


# In[4]:


import json
with open('exam_2.json', 'w', encoding='utf-8') as f:
    for item in all_articles['articles']:
        line = json.dumps(item, ensure_ascii=False)
        f.write(line+',')

