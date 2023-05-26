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

        # EQUIPOS EN LA WEB
        equiposAll = soup.find_all('span', class_='nombre-equipo')

        # Lista vacia para guardar solamente los nombres de los equipos
        equiposExtraidos = []

        count = 0
        for equipo in equiposAll:
            if count < 20:  # Los primeros 20
                equiposExtraidos.append(equipo.text)
                count += 1
            else:
                break

        # PUNTOS EN LA WEB
        puntosWeb = soup.find_all('td', class_='destacado')
        puntosExtraidos = []
        count = 0
        for punto in puntosWeb:
            if count < 20:
                puntosExtraidos.append(punto.text)
                count += 1
            else:
                break

        content = pd.DataFrame({
            "Nombre": equiposExtraidos,
            "Puntos": puntosExtraidos,
        },
            index=list(range(1, 21))  # ID
        )

        # Exportamos los datos a un archivo CVS(excel)
        content.to_csv('Clasificacion_Mundial.cvs', index=False)  # Sin guardar el ID

        return content