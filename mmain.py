from bs4 import BeautifulSoup
import requests

# Получаем HTML-код страницы
url = 'https://example.com/dictionary'
response = requests.get(url)
html = response.text

# Создаем объект BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Ищем нужное слово в тексте страницы
word = soup.find(text='искомое слово')
print(word)