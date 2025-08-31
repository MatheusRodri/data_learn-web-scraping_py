import requests
from bs4 import BeautifulSoup


pagina = requests.get("https://quotes.toscrape.com/")
dados_pagina = BeautifulSoup(pagina.text,'html.parser')

todas_frases = dados_pagina.find_all('div',class_="quote")

for div in todas_frases:
        frase = div.find('span',class_="text").text
        autor = div.find('small',class_="author").text
        print(f"{frase} - {autor}")