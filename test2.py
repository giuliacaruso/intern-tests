import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool

def scrape_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            data = soup.find('div', class_='example-class').text
            return data
        else:
            print(f"No se pudo extraer información de {url}. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"No se pudo extraer información de {url}: {str(e)}")
        return None

url_list = ['https://example.com/page1', 'https://example.com/page2', 'https://example.com/page3']

for url in url_list:
    result = scrape_url(url)
    if result:
        print(result)

