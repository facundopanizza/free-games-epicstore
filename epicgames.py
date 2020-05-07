#!"C:\Python38\python.exe"

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyotp
import time
from config import two_factor_key, email, password, headless

options = webdriver.ChromeOptions()

if headless == True:
	options.add_argument('headless')
else:
	options.add_argument('--window-size=1200x600')

driver = webdriver.Chrome(options=options)

def get_token():
    return pyotp.TOTP(two_factor_key).now()

def login():
    # Go to epic store and login
    driver.get('https://epicgames.com/login')

    time.sleep(5)

    email_element = driver.find_element_by_name('usernameOrEmail')
    password_element = driver.find_element_by_name('password')
    email_element.send_keys(email)
    password_element.send_keys(password)
    password_element.send_keys(Keys.RETURN)

    time.sleep(5)

    try:
        token = get_token()
        driver.find_element_by_name('code').send_keys(token)
        driver.find_element_by_name('code').send_keys(Keys.RETURN)
    except Exception as e:
        print(e)


def get_free_games_links():
    driver.get('https://www.epicgames.com/store/es-ES/free-games')
    games_section = ''

    for section in driver.find_elements_by_tag_name('section'):
        if section.get_attribute('class').find('FreeGamesCollection') != -1:
            games_section = section
            break;

    game_links = []

    for link in games_section.find_elements_by_tag_name('a'):
        game_links.append(link.get_attribute('href'))

    return game_links

def claim_games(games_links):
    for link in games_links:
        driver.get(link)
        time.sleep(5)

        game_name = driver.find_element_by_xpath(
            '/html/body/div/div/div[4]/main/div/nav[1]/div/nav/div/ul/li[2]/a/h2/span').text

        try:
            driver.find_element_by_xpath('/html/body/div/div/div[4]/main/div[2]/div/div[2]/div/button').click()
        except Exception as e:
            print(e)
            print('No es necesario ser mayor de edad.')

        time.sleep(5)

        try:
            buttons = driver.find_elements_by_tag_name('button')
            for button in buttons:
                if button.get_attribute('class').find('PurchaseButton-button') != -1:
                    get_games_button = button

            if get_games_button.get_attribute('disabled') == 'true':
                print('Ya tenes el juego ' + game_name + ' o todavia no esta disponible.')
            else:
                get_games_button.click()
        except Exception as e:
            print(e)
            print('Error desconocido tratando de adquirir el juego: ' + game_name)
            print(link)

        time.sleep(5)

        try:
            driver.find_element_by_class_name('confirm-container').find_element_by_tag_name('button').click()
        except Exception as e:
            print(e)

        time.sleep(5)

