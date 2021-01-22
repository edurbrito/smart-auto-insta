#!./env/bin/python3
import cred
from selenium import webdriver
from selenium.webdriver.chrome.options import *
from selenium.webdriver.common.keys import Keys
from pykeyboard import PyKeyboard

import time

def insta_poster(simulate=True):
    print("###############")
    print("#             #")
    print("#  INSTA BOT  #")
    print("#             #")
    print("###############")
    username = cred.username
    passwd = cred.passwd

    photopath = '../utils/post_image.jpg' #here you can put the image directory

    phototext = open('../utils/post_info','r+').read()
    print()
    print("TEXT TO SUBMIT:")
    print(phototext)
    print()
    print("######## LOGS ########")
    print()

    driverpth = "../utils/chromedriver"

    options = Options()
    options.add_argument("--log-level=3")
    options.add_argument("--silent")
    #options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-logging")
    options.add_argument("--mute-audio")
    #mobile_emulation = {"deviceName": "Nexus 5"}
    #options.add_experimental_option("mobileEmulation", mobile_emulation)
    options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')
    driver = webdriver.Chrome(executable_path=driverpth,options=options)
    driver.get("https://www.instagram.com/accounts/login/?hl=pt")
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id='react-root']/section/main/article/div/div/div/form/div[4]/div/label/input").send_keys(username)
    time.sleep(0.5)
    driver.find_element_by_xpath("//*[@id='react-root']/section/main/article/div/div/div/form/div[5]/div/label/input").send_keys(passwd)
    time.sleep(0.5)
    driver.find_element_by_xpath("//*[@id='react-root']/section/main/article/div/div/div/form/div[7]/button/div").click()
    while 1:
        time.sleep(1)
        try:
            print("Loop1")
            driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/button").click()
            break
        except:
            pass
    while 1:
        time.sleep(1)
        try:
            print("Loop2")
            driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]").click()
            break
        except:
            pass
    while 1:
        print("Loop3")
        time.sleep(1)
        driver.find_element_by_css_selector('body').send_keys(Keys.PAGE_DOWN)
        try:
            driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]").click()
            break
        except:
            pass

    driver.find_element_by_xpath("//div[@role='menuitem']").click()
    from copytoclipboard import fileManager,textToClipboard

    fileManager(photopath)
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id='react-root']/section/div[2]/div[2]/div/div/div/button[1]").click()
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id='react-root']/section/div[1]/header/div/div[2]/button").click()
    time.sleep(1)
    JS_ADD_TEXT_TO_INPUT = """
    var elm = arguments[0], txt = arguments[1];
    elm.value += txt;
    elm.dispatchEvent(new Event('change'));
    """
    elem = driver.find_element_by_xpath("//*[@id='react-root']/section/div[2]/section[1]/div[1]/textarea")
    elem.click()
    text = u'' + phototext
    time.sleep(0.5)
    driver.execute_script(JS_ADD_TEXT_TO_INPUT, elem, text)
    driver.find_element_by_xpath("//*[@id='react-root']/section/div[2]/section[1]/div[1]/textarea").send_keys("\n\n")
    time.sleep(1)
    
    if(not simulate): driver.find_element_by_xpath("//*[@id='react-root']/section/div[1]/header/div/div[2]/button").click()
    else: raise EOFError
    time.sleep(4)
    driver.close()

    #ctrl+l
    #ctrl+v
    #enter  

if __name__ == '__main__':
    insta_poster(False)