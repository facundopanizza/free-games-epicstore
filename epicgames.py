from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyotp
import time

twoFactorKey = ''
email = ''
password = ''

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1200x600')

driver = webdriver.Chrome(options=options)
driver.get('https://epicgames.com/login')

time.sleep(5)

emailElement = driver.find_element_by_name('usernameOrEmail')
passwordElement = driver.find_element_by_name('password')

emailElement.send_keys(email)
passwordElement.send_keys(password)
passwordElement.send_keys(Keys.RETURN)

time.sleep(5)

try:
    token = pyotp.TOTP(twoFactorKey).now()
    driver.find_element_by_name('code').send_keys(token)
    driver.find_element_by_name('code').send_keys(Keys.RETURN)
except Exception as e:
    print(e)

time.sleep(5)

driver.get('https://www.epicgames.com/store/es-ES/free-games')

time.sleep(5)

gamesDiv = driver.find_element_by_xpath('/html/body/div/div/div[4]/main/div/div/div/div/div[2]/section[2]/div/div/section/div')
gamesLinks = []

for link in gamesDiv.find_elements_by_tag_name('a'):
    gamesLinks.append(link.get_attribute('href'))

for link in gamesLinks:
    driver.get(link)
    time.sleep(5)

    gameName = driver.find_element_by_xpath('/html/body/div/div/div[4]/main/div/nav[1]/div/nav/div/ul/li[2]/a/h2/span').text

    try:
        driver.find_element_by_xpath('/html/body/div/div/div[4]/main/div[2]/div/div[2]/div/button').click()
    except Exception as e:
        print(e)
        print('No es necesario ser mayor de edad.')

    time.sleep(5)

    try:
        driver.find_element_by_xpath('/html/body/div/div/div[4]/main/div/div/div[2]/div/div[2]/div[2]/div/div/div[3]/div/div/div[3]/div/button').click()
    except Exception as e:
        print(e)
        print('Ya tenes el juego ' + gameName + ' o todavia no esta disponible.')
        print(link)

    time.sleep(5)

    try:
        driver.find_element_by_xpath('/html/body/div[3]/div/div/div[4]/div/div[4]/div[1]/div[2]/div[5]/div/div/button').click()
    except Exception as e:
        print(e)

    time.sleep(5)
