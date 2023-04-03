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
cursos = []

while(True):
    #O loop se encerrará quando não existir mais nenhum link de nenhum curso no HTML da página. Todos os existentes são salvos na lista 'cursos'
    try:
        aux_curso = navegador.find_element(By.XPATH, '//*[@id="content"]/div[2]/div['+ str(cont)+ ']/h3').text
        n_cursos = n_cursos + 1
    except:
        break
    cursos.append(aux_curso)
    
    cont = cont + 1


print(n_cursos)
print(cursos)

n_alunos = 1

lista_elementos = []

linhas = []


for i in range(1, n_cursos + 1):
    n_alunos =  1

    while(True):

        linha  =  '//*[@id="content"]/div[2]/div[' + str(i) + ']/table[1]/tbody/tr[' +str(n_alunos) +']'   

        try:
            texto = (navegador.find_element(By.XPATH, linha).text)

        except:
            break

        n_alunos = n_alunos + 1

        linhas.append(texto)

    lista_elementos.append(linhas)    
    linhas = []
    n_alunos = n_alunos + 1


modalidade = []
modalidade_aux=[]
classificacao =[]
codigo = []
nome=[]
numero=[]
curso_aluno = []


for j in range((n_cursos)):
    
    print(lista_elementos[j])

    for i in range(1, len(lista_elementos[j])):

        curso_aluno.append(cursos[j])
        print(lista_elementos[j][i])

        #Modalidade
        aux = lista_elementos[j][i].split(" ")[0]
        print(aux)

        if(aux == "Modalidade" or aux == "Ampla"):
            print("Primerio if")
            modalidade_aux.append(aux)

        elif(aux.split("º")[0].isnumeric()):
            print("Segundo if")
            classificacao.append(aux)
            numero.append(lista_elementos[j][i].split(" ")[-1])
            aluno = lista_elementos[j][i].split(" ")[2]
            print(aluno)
            

            for g in range(3,  len(lista_elementos[j][i].split(" ")) - 1) :
                aluno = aluno + " " + lista_elementos[j][i].split(" ")[g]
            
            nome.append(aluno)

            print(aluno)

            print("\n")

            aluno = []

            modalidade.append(modalidade_aux[-1])



print(len(modalidade))
print(len(nome))
print(len(numero))

print((modalidade))
print((nome))
print((numero))
print((curso_aluno))
