from bs4 import BeautifulSoup
import requests
import pandas as pd

def crawl(url):
    # Realizar una solicitud HTTP GET a la URL
    response = requests.get(url)
    # Comprobar si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        data = requests.get(url)