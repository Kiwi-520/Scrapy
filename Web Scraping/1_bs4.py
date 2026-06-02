from bs4 import BeautifulSoup

with open('file.html', 'r') as f:
    content = f.read()

soup = BeautifulSoup(content, 'html.parser')
# print(soup.prettify())

# print(soup.title)
print(soup.title.string)
print("TItle text: ")
print(soup.title.text)
print(soup.title.name)
print(soup.p['class'])