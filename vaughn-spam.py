from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
browser = webdriver.Chrome(options=options, executable_path=r'chromedriver.exe')

page = 'url of the stream you want to spam'
logIn = '//*[@id="menu2Signin"]'
unameField = '//*[@id="modalv3_content_signin"]/div/form/div[2]/input'
passField= '//*[@id="modalv3_content_signin"]/div/form/div[5]/input'
logInButton = '//*[@id="modalv3_content_signin"]/div/form/input[2]'
textArea = '//*[@id="vn_chat_message"]'
#make sure the messages are not same as vaughn picks up spam
message = 'message you want to spam'
message2 = 'message you want to spam'
sendButton = '//*[@id="CV3opt"]/div[11]/div'


browser.get(page)

clickLogIn = browser.find_element(By.XPATH, logIn).click()
time.sleep(5)
enterUname = browser.find_element(By.XPATH, unameField).send_keys("your username")
time.sleep(1)
enterPass = browser.find_element(By.XPATH, passField).send_keys("your password")
signIn = browser.find_element(By.XPATH, logInButton).click()
time.sleep(20)
spam = browser.find_element(By.XPATH, textArea)
send = browser.find_element(By.XPATH, sendButton)

while(True):
    spam.send_keys(message)
    send.click()
    #remove these timeouts if you want instant spam, or change the time
    #to whatever you want
    time.sleep(5)
    spam.send_keys(message2)
    send.click()
    time.sleep(5)
