import requests
import xlsxwriter  
from selenium import webdriver
import selenium.webdriver.support.expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from datetime import date

options = Options()
options.add_experimental_option("detach", True)

navegador = webdriver.Chrome(ChromeDriverManager().install(), options=options)

navegador.get("https://www.portal.prograd.ufu.br/sismat/matriculaonline/divulgacao/convocacao/194/733")

cont = 1
cont_alunos = 1
n_cursos = 0

while(True):
    #O loop se encerrará quando não existir mais nenhum link de nenhum curso no HTML da página. Todos os existentes são salvos na lista 'cursos'
    try:
        print('//*[@id="content"]/div[2]/div['+ str(cont)+ ']/h3')
        print(navegador.find_element(By.XPATH, '//*[@id="content"]/div[2]/div['+ str(cont)+ ']/h3').text)
        n_cursos = n_cursos + 1
    except:
        break
    
    cont = cont + 1

print(n_cursos)

n_alunos = 1


for i in range(1, n_cursos + 1):

    n_alunos =  1

    while(True):

        try: 
           navegador.find_element( By.XPATH, '//*[@id="content"]/div[2]/div[' +str(n_cursos) + ']/table[1]/tbody/tr[' +str(n_alunos) +']')

        except:
            break


        try:
            print(navegador.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[' +str(n_cursos) + ']/table[1]/tbody/tr[' +str(n_alunos) +']/th[1]').text)

        except:
            print(navegador.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[' +str(n_cursos) + ']/table[1]/tbody/tr['+str(n_alunos) + ']/td[1]').text)

        n_alunos = n_alunos + 1    


print()
