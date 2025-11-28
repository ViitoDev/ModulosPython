import re

text = "Aprendendo conhecimentos sobre módulos"

#1- Indíce inicial de palavras
# O "r" significa uma row  string (string bruta)
match = re.search(r'Aprendendo', text)
print(f"índice inicial: {match.start()}")
print(f"índice final: {match.end()}")

#2- Buscando o índice que possui o ponto
site = "https://google.com"
match = re.search(r'\.', site)
print(match)

#3- Buscando uma lista de caracteres dentro de uma frase
pattern = "[g-m]"
result = re.findall(pattern, text)
print(result)

#4 - Verificando o inicio de uma string
rule = r'^A'
phrases = ["A casa está suja", "O dia está lindo", "Vamos passear"]
for f in phrases:
    if re.match(rule, f):
        print(f"Corresponde: {f}")
    else:
        print(f"Não corresponde: {f}")

#5 - Final de uma string
rule_end = r'!$'
phrase2 = "O dia está lindo!"
match = re.search(rule_end, phrase2)
if match:
    print("Sim corresponde")
else:
    print("Não corresponde")