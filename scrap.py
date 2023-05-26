from bs4 import BeautifulSoup
import requests
import pandas as pd

def crawl(url):
    # Realizar una solicitud HTTP GET a la URL
    response = requests.get(url)
    