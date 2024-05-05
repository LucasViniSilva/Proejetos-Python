##Passo a Passo do Projeto

  ##Passo 1: Entrar no Sistema da Emmpresa

    ##Passo2: Fazer Login:
      ##Passo3: Importar a base de dados
        ##Passo4: Cadastrar 1 produto
          ##Passo5: Repetir o processo de cadastro até acabar

# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa 
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui
import time 

pyautogui.PAUSE = 0.5

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas

# abrir o navegador (chrome)
pyautogui.press("win")

pyautogui.write("chrome")

pyautogui.press("enter")

# entrar no link 
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

##Dar uma pausa de  5 segundo. Página carregar
time.sleep(5)
# Passo 2: Fazer loginrome
# selecionar o campo de email
# escrever o seu email
pyautogui.click(x=872, y=562)
pyautogui.write("Qualquergmail@gmail.com")

#Digitar sua senha

pyautogui.press("tab")
pyautogui.write("Nuncavinadanavida")
pyautogui.press("enter")

# Passo 3: Importar a base de produtos pra cadastraralqu
import pandas
tabela = pandas.read_csv("produtos.csv")
print(tabela)
# Passo 4: Cadastrar um produto
for linha in tabela.index:
    # clicar no campo de código
  pyautogui.click(x=604, y=395)

  codigo = tabela.loc[linha, "codigo"]
  pyautogui.write(codigo)
  pyautogui.press("tab")  

      # pegar da tabela o valor campo que a gente quer preencher
  pyautogui.write(tabela.loc[linha, "marca"])
  pyautogui.press("tab")
    
      # passar para o proximo campoQualquergmail@gmail.com  Nuncavinadanavida
  
  pyautogui.write(tabela.loc[linha, "tipo"])
  pyautogui.press("tab")
    
  # preencher o campo
  pyautogui.write(str(tabela.loc[linha, "categoria"]))
  pyautogui.press("tab")

  pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
  pyautogui.press("tab")


  pyautogui.write(str(tabela.loc[linha, "custo"]))
  pyautogui.press("tab")

  obs = (str(tabela.loc[linha, "obs"]))

  if not pandas.isna(obs):
    
      pyautogui.write(obs)
      #Pule para o botão enviar
      pyautogui.press("tab")
      #enviar
      pyautogui.press("enter")

      pyautogui.scroll(5000)
      
      
      
     # cadastra o produto (botao enviar)

    # dar scroll de tudo pra cima
    
    # Passo 5: Repetir o processo de cadastro até o fim



