import re
from bs4 import BeautifulSoup

with open("pagina.html", encoding="utf-8") as arquivo:
    html = arquivo.read()

sopa = BeautifulSoup(html, "html.parser")

print("Título da página:", sopa.title.string if sopa.title else "sem título")
print("Ocorrências de 'price':", html.count("price"))
print("Ocorrências de 'card':", html.count("card"))
print("Ocorrências de 'R$':",html.count("R$"))

print("\nTags com 'card' na classe:")
for tag in sopa.find_all(class_=re.compile("card", re.I))[:10]:
    print(" ", tag.name, tag.get("class"))

print("\nTamanho do arquivo:", len(html), "caracteres")
print("Começo do arquivo:")
print(html[:500])