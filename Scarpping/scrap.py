import requests
from bs4 import BeautifulSoup as BS
import pandas as pd

def scrap(URL, TAG, NAM):
    url = URL
    response = requests.get(url)
    soup = BS(response.text, 'html.parser')
    table = soup.find('table', {'class':TAG})
    rows = table.find_all('tr')
    data = []
    for row in rows:
        cols = row.find_all(['th','td'])
        cols = [i.text.strip() for i in cols]
        data.append(cols)
        df = pd.DataFrame(data)
        df.to_csv(f'{NAM}.csv', index=False)

# Scrape Gold Data
scrap(URL = "https://goldpricez.com/gold/history/lkr/years-3", TAG = 'tb', NAM = "Gold")

# Scarp Petrol
scrap(URL = "https://ceypetco.gov.lk/historical-prices/", TAG = 'ea-advanced-data-table ea-advanced-data-table-static ea-advanced-data-table-9fdc03b ea-advanced-data-table-sortable ea-advanced-data-table-paginated ea-advanced-data-table-searchable'
      , NAM = "Petrol")
    