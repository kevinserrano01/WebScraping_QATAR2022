from bs4 import BeautifulSoup
import requests
import pandas as pd

def crawl(url):
    # Realizar una solicitud HTTP GET a la URL
    response = requests.get(url)
    # Comprobar si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        data = requests.get(url)

        # Identificar elementos html
        soup = BeautifulSoup(data.content, "html.parser")

        # Equipos de la web
        equiposAll = soup.find_all('span', class_='nombre-equipo')

        # Lista vacia para guardar solamente los nombres de los equipos
        equiposExtraidos = []

        count = 0
        for equipo in equiposAll:
            if count < 20:  # Los primeros 10
                equiposExtraidos.append(equipo.text)
                count += 1
            else:
                break