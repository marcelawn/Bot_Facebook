from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from time import sleep


def iniciar_driver():

    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=1300,1000', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,

    })
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()), options=chrome_options)

    return driver


driver = iniciar_driver()
# Abrir o facebook
driver.get('https://facebook.com')
sleep(2)
email = driver.find_element(By.ID, 'email')
sleep(1)
email.send_keys('email')
sleep(1)
senha = driver.find_element(By.ID, 'pass')
sleep(1)
senha.send_keys('senha')
sleep(1)
botao_login = driver.find_element(By.NAME, 'login')
sleep(1)
botao_login.click()
sleep(7)
botao_pagina_inicial = driver.find_element(
    By.XPATH, '//a[@aria-label="Página inicial"]')
sleep(1)
botao_pagina_inicial.click()
sleep(1.5)
campo_postagem = driver.find_element(
    By.XPATH, '//*[text()="No que você está pensando, Leonardo?"]')
sleep(1)
campo_postagem.click()
sleep(1)
campo_status = driver.find_element(
    By.XPATH, '//p[@class="xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8"]')
sleep(1)
campo_status.click()
campo_status.send_keys('Olá a todos!')
sleep(2)
botao_publicar = driver.find_element(
    By.XPATH, '//div[@class="x1n2onr6 x1ja2u2z x78zum5 x2lah0s xl56j7k x6s0dn4 xozqiw3 x1q0g3np xi112ho x17zwfj4 x585lrc x1403ito x972fbf xcfux6l x1qhh985 xm0m39n x9f619 xn6708d x1ye3gou xtvsq51 x1r1pt67"]')
sleep(2)
botao_publicar.click()


input('')
driver.close()
