import requests
import pandas as pd
from datetime import date
from openpyxl import load_workbook
url = 'https://www1.nseindia.com/live_market/dynaContent/live_analysis/changePercentage.json'
r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
data = r.json()
advance = data['rows'][0]['advances']
decline = data['rows'][0]['declines']

toappend = pd.DataFrame({'Advance':advance, 'Decline':decline}, index =[0]);
toappend['Date'] = date.today()
writer = pd.ExcelWriter('D:\Python Exercices\McClellanOscillator.xlsx', engine = 'openpyxl')
toappend.to_excel(writer, index = False)
toappend.to_excel(writer, startrow = curr_count + 1, index = False)
writer.save();
