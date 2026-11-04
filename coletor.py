import requests

URL = "https://www.pelando.com.br/"


CABECALHOS = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64)"}

resposta = requests.get(URL, headers=CABECALHOS, timeout=15)

print("Status:", resposta.status_code)
print("Tamanho:", len(resposta.text), "caracteres")

with open("pagina.html", "w", encoding="utf-8") as arquivo:
    arquivo.write(resposta.text)