import requests
from bs4 import BeautifulSoup
import time

# Función para realizar el web scraping en Bing
def bing_scrape(search_query):
    # Paso 1: Obtener la página de resultados de Bing
    base_url = 'https://www.bing.com/search?form=NTPCHB&q='
    search_url = base_url + search_query
    response = requests.get(search_url)

    # Comprobar si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        # Esperar 5 segundos para dar tiempo a que se genere la información
        time.sleep(30)

        # Paso 2: Analizar el contenido de la página con BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Paso 3: Encontrar y extraer los fragmentos de texto
        snippets = soup.find_all('div', {'class': 'ac-textBlock'})

        # Paso 4: Guardar los resultados en un archivo de texto
        if snippets:
            with open(f'{search_query}_bing_output.txt', 'w', encoding='utf-8') as file:
                for snippet in snippets:
                    # Extraer solo el texto sin formato
                    text = ''.join(snippet.stripped_strings)
                    file.write(text + '\n\n')
            print(f'Los resultados de Bing se han guardado en {search_query}_bing_output.txt')
        else:
            print('No se encontraron fragmentos de texto en la página de Bing.')
    else:
        print(f'Error al obtener la página de Bing. Código de estado: {response.status_code}')

# Pedir al usuario que ingrese el término de búsqueda en Bing desde el textarea
search_query = input('Ingresa el término de búsqueda en Bing desde el textarea: ')

# Llamar a la función de web scraping en Bing
bing_scrape(search_query)

# ESTE CODIGO TIENE EL PROBLEMA DE QUE BEAUTIFULSOUP NO DETECTA ACTUALIZACIONES JAVASCRIPT EN LAS PAGINAS, LO QUE SE REQUEIRE SELENIUM PARA ESTO
