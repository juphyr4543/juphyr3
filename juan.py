import requests
from bs4 import BeautifulSoup

# Realizar la solicitud HTTP a la página web
url = "https://openai.com/blog/"
response = requests.get(url)

# Crear el objeto BeautifulSoup para analizar el contenido HTML
soup = BeautifulSoup(response.text, "html.parser")

# Encontrar todos los elementos de título de las noticias
news_titles = soup.find_all("h4", class_="u-contentSansThin")

# Imprimir los títulos de las noticias
for title in news_titles:
    print(title.text.strip())
#Juan Miramag 
#analiza pinturas
#IEM_ESCUELA_NORMAL_PASTO
#11-1
