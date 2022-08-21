import random
import unidecode
from collections import Counter
from termcolor import colored 

#Função para gerar a palavra 
def carrega_palavra():
  
  arquivo = open("Palavras.txt", "r", encoding="utf-8")
  palavras = []
  
  for palavra in arquivo:
    if (len(palavra) - 1 == tamanho):
      palavras.append(palavra[0:len(palavra)-1])
      
  arquivo.close()
      
  numero = random.randrange(0, len(palavras))
  palavra_secreta = palavras[numero]
  
  return palavra_secreta, palavras

#Função para receber tentativa 
def receberPalavra(palavras_aceitaveis):
  
  while(1):     
    tentativa = input("\nDigite a palavra: ")
    
    if len(tentativa) != tamanho:
      print("Digite uma palavra com o tamanho informado.")
    elif tentativa not in palavras_aceitaveis:
      print("Digite uma palavra válida.")
    else:
      break
      
  return tentativa

#Função para verificar se tentativa é a palavra
def jogada(num_tentativas):

  palavra, palavras_aceitaveis = carrega_palavra()
  palavra = unidecode.unidecode(palavra) 
  
  while (num_tentativas > 0):

    tentativa = receberPalavra(palavras_aceitaveis)
        
    tentativa = tentativa.lower()
    tentativa = unidecode.unidecode(tentativa)

    if (tentativa == palavra):
      return ("\nVENCEU")

    tentativa = list(tentativa)
    counter = Counter(palavra) 

    for i in range(tamanho):
      if (tentativa[i] not in palavra):
        counter[tentativa[i]] -= 1
        tentativa[i] = tentativa[i].upper()
        tentativa[i] = colored(tentativa[i], 'red') 
        
    for i in range(tamanho):
      if (tentativa[i] == palavra[i]):
        counter[tentativa[i]] -= 1
        tentativa[i] = tentativa[i].upper()
        tentativa[i] = colored(tentativa[i], 'green')

    for i in range(tamanho):
      if (tentativa[i] in palavra and counter[tentativa[i]] != 0):
        counter[tentativa[i]] -= 1
        tentativa[i] = tentativa[i].upper()
        tentativa[i] = colored(tentativa[i], 'yellow') 
    
    for i in range(len(tentativa)):
      print(tentativa[i], end="")

    print()
    num_tentativas -= 1
    
  return print("\nPERDEU - A palavra era", palavra)

  
#Entrada de dados
print(colored("**By: Beatriz Araújo, Bianca Rangel & Maria Teixeira**\n\n", 'magenta'))
print(colored("*********************************", 'magenta'))
print("*** Bem vindo ao jogo GotIt! *** ")
print(colored("*********************************\n\n", 'magenta'))

print(colored("Verde",'green') + ": Letra está no lugar correto.")
print(colored("Amarelo",'yellow') + ": Letra está no lugar errado.")
print(colored("Vermelho",'red') + ": Letra não está na palavra.\n\n")

while (1):
  num = ['2','3','4','5','6']
  tamanho = input("Escolha o tamanho da palavra: ")
  if tamanho not in num:
    print("Informe um número válido\n")
  else:
    tamanho = int(tamanho)
    break
  
while (1):
  tentativa = input("\nDeseja escolher o número de tentativas? (SIM/NAO) ")
  tentativa = tentativa.upper()
  if (tentativa == "SIM" or tentativa == "NAO"):
    break
  else:
    print("Digite apenas SIM ou NAO.")

while (1): 
  if (tentativa == "SIM"):
    num = ['1','2','3','4','5','6']
    num_tentativas = input("\nInforme o número de tentativas desejadas: ")

    if num_tentativas not in num:
      print("Informe um número válido\n")
    else:
      num_tentativas = int(tamanho)
      break
      
  elif (tentativa == "NAO"):
    num_tentativas = 6
    break

print(jogada(num_tentativas))
