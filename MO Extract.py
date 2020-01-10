from bs4 import BeautifulSoup
import pandas as pd
import requests


url = "https://www1.nseindia.com/live_market/dynaContent/live_market.htm"
webpage = requests.get(url);
soup = BeautifulSoup(webpage.content, "html.parser");
#soup.findAll('table')
#advance = soup.find_all("td",attrs={"id":"advanceDecline - "})
for tr in soup.find_all('tr'):
    advance = tr.find_all('td')
    print(advance)
    
#################################################################

import requests

url = 'https://www1.nseindia.com/live_market/dynaContent/live_analysis/changePercentage.json'
r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
data = r.json()
advance = data['rows'][0]['advances']
decline = data['rows'][0]['declines']

