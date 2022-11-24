import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from datetime import date
from selenium.webdriver.common.by import By
import csv

hoje = date.today()

with open('entrega_650.csv', 'a', newline='', encoding='UTF-8') as f:

    linha = str(hoje) + '\n'
    f.write(linha)
    f.write('Frete SP'+ '\n')
options = Options()

def load_data(filename):
    mylist = []
    with open(filename) as numbers:
        numbers_data = csv.reader(numbers, delimiter=',')
        next(numbers_data)
        for row in numbers_data:
            mylist.append(row[0])
        return mylist

new_list = load_data('650.csv')

url = 'https://www.montecarlo.com.br/aneis-joliejolie-aneis-nim030267/p'

navegador = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

navegador.get(url)
sleep(5)
input_class = navegador.find_element(By.XPATH, "//input[@class='vtex-address-form-4-x-input ma0 border-box vtex-address-form-4-x-hideDecorators vtex-address-form-4-x-noAppearance br2  br-0 br--left  w-100 bn outline-0 bg-base c-on-base b--muted-4 hover-b--muted-3 t-body pl5 ']")

print(type(input_class))

sleep(2)
for row in new_list:

    input_class.click()
    input_class.send_keys(Keys.CONTROL, "a", Keys.DELETE)
    input_class.send_keys(row)
    print("teste")
    try:
        navegador.find_element(By.XPATH, "//div[@class='vtex-button__label flex items-center justify-center h-100 ph5 w-100 border-box ']").click()
    except:
        print("Nao conseguiu clickar")

    sleep(4)

    site = BeautifulSoup(navegador.page_source, 'html.parser')

    try:
        frete = site.find('td', class_='vtex-store-components-3-x-shippingTableCell vtex-store-components-3-x-shippingTableCellDeliveryEstimate pv1 ph3 t-small c-muted-2').get_text().strip()
        print(frete)
    except:
        frete = frete = site.find('span', class_='vtex-store-components-3-x-shippingNoMessage dib t-small mt4').get_text().strip()
    print(frete)

    with open('entrega_650.csv', 'a', newline='', encoding='UTF-8') as f:

        linha = frete + '\n'
        f.write(linha)
