import pyautogui as pg
import time
import pandas as pd
from pandas import DataFrame

pg.PAUSE = 0.5
# Passo 1: entrar no sistema da empresa
pg.press("win")
pg.write("chrome")
pg.press("enter")
#Url Sistema de Controle de Estoque
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pg.write(link)
pg.press("enter")
time.sleep(3)
# Passo 2: Fazer login
username = "davi@gmail.com"
password = "1234567@"
pg.click(x=425,y=414)
pg.write(username)
pg.click(x=411, y=509)
pg.write(password)
pg.press("tab")
pg.press("enter")
time.sleep(3)
# Passo 3: importar base de dados
tabela = pd.read_csv('produtos.csv')
# Passo 4: Cadastrar 1 produto
for i in tabela.index:
    pg.click(x=406, y=291)
    #codigoProduto
    codigo = tabela.loc[i,"codigo"]
    pg.write(codigo)
    pg.press("tab")
    #marca
    marca = tabela.loc[i,"marca"]
    pg.write(marca)
    pg.press("tab")
    #tipoProduto
    tipo = tabela.loc[i,"tipo"]
    pg.write(tipo)
    pg.press("tab")
    #categoriaProduto
    categoria = str(tabela.loc[i,"categoria"])
    pg.write(categoria)
    pg.press("tab")
    #precoUnitario
    precoUnitario = str(tabela.loc[i, "preco_unitario"])
    pg.write(precoUnitario)
    pg.press("tab")
    #custoProduto
    custoProduto = str(tabela.loc[i, "custo"])
    pg.write(custoProduto)
    pg.press("tab")
    #observacoes
    obs = tabela.loc[i, "obs"]
    if not pd.isna(obs):
        pg.write(obs)
        pg.press("tab")
    else:
        pg.press("tab")
    #enviar
    pg.press("enter")

    pg.scroll(5000)
# Passo 5: Repetir o processo de cadastro até acabar a base de dados




