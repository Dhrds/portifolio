from selenium import webdriver


import PyPDF2
from selenium import webdriver
from time import sleep

arquivo = r"C:/Users/douglas/Downloads/resumo.pdf"
lerpdf = PyPDF2.PdfFileReader(arquivo)
pagina = lerpdf.getPage(0)
conteudo =pagina.extractText()
lista_pdf = []
print(conteudo.split())
for i in conteudo.split() :
    lista_pdf.append(i)
inome = lista_pdf.index('CLIENTE:')
nome = lista_pdf[inome+1]

navegador = webdriver.Chrome()

navegador.get("https://tapweb.com.br/login")
navegador.find_element_by_xpath('//*[@id="nome"]').send_keys('Douglas')
navegador.find_element_by_xpath('//*[@id="senha"]').send_keys('123')
navegador.find_element_by_xpath('/html/body/app-root/login/div/div/div/div[2]/div/form/button').click()
sleep(10)
navegador.find_element_by_xpath('//*[@id="cliente"]').click()
navegador.find_element_by_xpath('//*[@id="page-wrapper"]/admin-cliente/div/div[2]/button').click()
navegador.find_element_by_xpath('//*[@id="modalCliente"]/div/div/div[2]/div/div/admin-cliente-geral/div/div[1]/div/form/div[1]/div/input-container/div/input').send_keys(nome)