import requests
from bs4 import BeautifulSoup
from time import sleep

def ValorDolar():
        url_valor = 'https://br.advfn.com/cambio'

        req = requests.get(url_valor)

        soup = BeautifulSoup(req.text, 'html.parser')


        valores = soup.find_all('td', class_ = 'quote-cell')

        for dolar in valores:
            dolar_font = dolar.find_all('big')
        for dolar_text in dolar_font:
            dolar_text = dolar_text.next_element
            return dolar_text

