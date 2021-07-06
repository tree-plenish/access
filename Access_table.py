import re
import pandas as pd

def datatable():
    
    ip_pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
    ip = []
    date_pattern = re.compile(r'(\d{2}/[A-z]{3}/\d{4}\:\d{2}\:\d{2}\:\d{2})')
    date = []
    parameter = []
    campaign_id = []
    
    with open('access.log','r') as file:
        access = file.readlines()
        
    for line in access:
        ip.append(ip_pattern.search(line)[0])
        date.append(date_pattern.search(line)[0])
        if line.find("?") == -1:
            parameter.append('none')
            campaign_id.append('0') # Appending empty str instead of empty array
        else:
            parameter.append(re.findall('[a-zA-Z]+\=[a-zA-Z\d+\-\%\_\:]+',line))
            c = (re.findall(r'[c]\=(\d+)',line))
            if len(c):
                campaign_id.append(c[0]) # Appending value excluding brackets
            else:
                campaign_id.append('0')

            
    df = pd.DataFrame({'IP Address': ip, 'Date' : date, 'Parameter' : parameter, 'Campaign ID' : campaign_id})
    df.to_csv('items.csv', index=False, encoding='utf-8')
    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_colwidth', 1000)
    print(df)
    
datatable()
