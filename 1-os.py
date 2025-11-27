import os

#1- Retornar pasta atual
print(os.getcwd())

#2- Listar arquivos e pastas
print(os.listdir())

#3- Verificar a versão do os
os.system('ver')

#4- Configurações da máquina
os.system('systeminfo')

#5- Limpar a tela do terminal
os.system('cls')

#6- Desliga o pc
# os.system('shutdown /s')
# os.system('shutdown /a')

def turn_off_one_hour():
    os.system('shutdown /s /t /3600')

def turn_off_half_an_hour():
    os.system('shutdown /s /t /1800')

def cancel_shutdown():
    os.system('shutdown /a')