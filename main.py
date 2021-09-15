#Necessário "pip install Pillow"
#Necessário "pip install selenium"
#Necessário "pip install pyautogui"

from selenium import webdriver
import pyautogui
import time

#pyautogui.alert('O código começará a ser executado. Após clicar em ok não mexa mais em nada do seu computador!!!')

navegador = webdriver.Chrome()
navegador.get('https://sed.educacao.sp.gov.br/')

#----------------------------------Acessando a tela de login da SED--------------------
time.sleep(5)
navegador.find_element_by_xpath('//*[@id="name"]').send_keys("rg30112680xsp")
navegador.find_element_by_xpath('//*[@id="senha"]').send_keys("999mangus")

pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(5)
#---------------------------------------------------------------------------------------

#----------------------------------Selecionando o tipo de acesso do servidor------------
navegador.find_element_by_xpath('//*[@id="sedUiModalWrapper_1body"]/ul/li[2]/a').click()
time.sleep(5)
#---------------------------------------------------------------------------------------


#----------------------------------Fechando janelas desnecessárias da SED---------------
navegador.find_element_by_xpath('//*[@id="sedUiModalWrapper_2close"]').click()
time.sleep(2)
navegador.find_element_by_xpath('//*[@id="sedUiModalWrapper_1close"]').click()
time.sleep(1)
#---------------------------------------------------------------------------------------


#----------------------------------Selecionando o Diário de Classe----------------------
navegador.find_element_by_xpath('//*[@id="decorAsidePopup"]/li[5]/a').click()
time.sleep(1)
navegador.find_element_by_xpath('//*[@id="decorAsidePopup"]/li[5]/ul/li[7]/a').click()
time.sleep(2)
#---------------------------------------------------------------------------------------


#----------------------------------Acessando a primeira sala de aula--------------------
#Acessando a primeira sala
for i in range(23):
    pyautogui.press('tab')
pyautogui.press('enter')
#---------------------------------------------------------------------------------------


#----------------------------------Acessando a data da aula-----------------------------
time.sleep(5)
navegador.find_element_by_xpath('//*[@id="modal_content"]/form/fieldset[1]/div[1]').click() #Botão do calendário


# time.sleep(1)
# calendario = pyautogui.locateCenterOnScreen('calendario.png')
# print(calendario)

time.sleep(1)
leftButton = pyautogui.locateCenterOnScreen('left_month.png')
print(leftButton)
pyautogui.click(leftButton)
pyautogui.click(leftButton)
