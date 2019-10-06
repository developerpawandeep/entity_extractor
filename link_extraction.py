from bs4 import BeautifulSoup

with open("Papers.html", encoding="utf-8") as f:
    data = f.read()
    soup = BeautifulSoup(data, 'html.parser')

links_with_text = []
for a in soup.find_all('a', href=True): 
    if a.text: 
        links_with_text.append(a['href'])