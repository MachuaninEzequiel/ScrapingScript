import requests
from bs4 import BeautifulSoup

# Función para realizar el web scraping en Wikipedia
def wikipedia_scrape(search_query):
    # Paso 1: Obtener la página de resultados de Wikipedia
    base_url = 'https://es.wikipedia.org/wiki/'
    search_url = base_url + search_query
    response = requests.get(search_url)

    # Comprobar si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        # Paso 2: Analizar el contenido de la página con BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Paso 3: Encontrar y extraer los párrafos de texto dentro de la clase específica
        content_div = soup.find('div', {'class': 'mw-content-ltr mw-parser-output'})
        paragraphs = content_div.find_all('p') if content_div else None

        # Paso 4: Guardar los resultados en un archivo de texto
        if paragraphs:
            with open(f'{search_query}_output.txt', 'w', encoding='utf-8') as file:
                for paragraph in paragraphs:
                    file.write(paragraph.text + '\n')
            print(f'Los resultados se han guardado en {search_query}_output.txt')
        else:
            print('No se encontraron párrafos con texto en la página de Wikipedia.')
    else:
        print(f'Error al obtener la página de Wikipedia. Código de estado: {response.status_code}')

# Pedir al usuario que ingrese el término de búsqueda
search_query = input('Ingresa el término de búsqueda en Wikipedia: ')

# Llamar a la función de web scraping en Wikipedia
wikipedia_scrape(search_query)
