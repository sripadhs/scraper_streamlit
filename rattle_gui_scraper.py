import streamlit as sl
from bs4 import BeautifulSoup
import requests
sl.title('Welcome to rattle_scraper')
sl.markdown('WARNING!:Only scrap the web with the permission of owner of that website')
inp=sl.text_input('Enter the URL of the website include https://:')

if sl.button('Scrap!'):
    web=requests.get(inp)
    soup=BeautifulSoup(web.content,'html.parser')
    sl.code(soup.prettify())