import random
import time
import tkinter
import tkinter as tk
from threading import Thread
from tkinter import *
from tkinter import ttk
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

root = Tk()

class GrepolisBot:
    def __init__(self):
        # self.username = input("Name: ")
        # self.password = input("Password: ")
        self.browser = None
        self.alive = None
    def alive_set(self):
        self.alive = True
        print(20 * '-', 'Start farm', '_' * 20)

    def alive_clean(self):
        self.alive = False
        print(20 * '-', 'Stop farm', '_' * 20)

    def login(self):

        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument('--window-size=1366,768')
        options.add_argument('disable-infobars')
        options.add_argument("--enable-extensions")
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')

        extension_path = r"D:\pythonProject\ATT\Tampermonkey.crx"
        options.add_extension(extension_path)
        #options.add_extension('chrome-extension://dhdgffkkebhmkfjojejmpbldmpobfkfo/ask.html?aid=ac2cf4c5-c630-4071-a9f0-01008468d953')
        options.add_argument('--user-agent=Chrome/120.0.6099.130')
        driver_path = r"D:\pythonProject\ATT\chromedriver.exe"
        service = Service(driver_path)
        self.browser = webdriver.Chrome(service=service, options=options)

        buton1=self.browser.get("https://www.tuto-de-david1327.com/annuaire/scripts/dio-tools-david1327-js.html")
        time.sleep(6)
        a=self.browser.title
        self.browser.implicitly_wait(10)
        handles = self.browser.window_handles
        self.browser.implicitly_wait(10)
        #self.browser.switch_to.window(self.browser.window_handles[2])
        self.browser.implicitly_wait(10)
        #buton=self.browser.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/table/tr[2]/td/div/div/div/div[2]/div/div/input[1]')
        self.browser.implicitly_wait(10)
        #buton.click()
        time.sleep(3)
        self.browser.switch_to.window(self.browser.window_handles[1])
        time.sleep(3)
        buton2=self.browser.get("https://www.grcrt.net/scripts/GrepolisReportConverterV2.user.js")
        time.sleep(2)
        self.browser.switch_to.window(self.browser.window_handles[2])
        time.sleep(2)
        #butons=self.browser.find_element(By.XPATH,'//*[@id="input_SW5zdGFsbF91bmRlZmluZWQ_bu"]')
        self.browser.implicitly_wait(10)
        time.sleep(3)
        #butons.click()
        time.sleep(2)
        window_handles = self.browser.window_handles

        # selectează fereastra a doua
        second_window_handle = window_handles[1]
        self.browser.switch_to.window(second_window_handle)
        # închide fereastra a doua
        self.browser.close()

        # selectează fereastra principală
        main_window_handle = window_handles[0]
        self.browser.switch_to.window(main_window_handle)
        time.sleep(1)
        self.browser.get("https://en.grepolis.com/game/index")
        time.sleep(2)

        # username_field = self.browser.find_element(By.NAME, 'login[userid]')
        # username_field.send_keys(self.username)
        #
        # password_field = self.browser.find_element(By.NAME, 'login[password]')
        # password_field.send_keys(self.password)
        # password_field.send_keys(Keys.RETURN)

        self.browser.implicitly_wait(30)
        self.browser.maximize_window()
        time.sleep(15)
    def farm(self):
        time.sleep(4)
        while True:
            if self.alive is True:
                while True:
                    try:
                        webdriver.ActionChains(self.browser).send_keys('x').perform()
                        time.sleep(0.5)
                        element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="fto_town_wrapper"]/div/div[9]/span[2]/a')))
                        self.browser.implicitly_wait(10)
                        time.sleep(random.uniform(0.95, 2.5))
                        webdriver.ActionChains(self.browser).move_to_element_with_offset(element, random.uniform(0.3, 5),random.uniform(0.3, 5)).click().perform()
                        time.sleep(1)
                        self.browser.implicitly_wait(10)
                        collect = self.browser.find_element(By.CSS_SELECTOR, '#fto_claim_button > div.caption.js-caption')
                        time.sleep(random.uniform(0.95, 2.5))
                        self.browser.implicitly_wait(10)
                        webdriver.ActionChains(self.browser).move_to_element_with_offset(collect,random.uniform(-30,+30),random.uniform(0.5,5)).click().perform()
                        time.sleep(2)
                        time.sleep(random.uniform(0.95, 1.4))
                        self.browser.implicitly_wait(10)
                        webdriver.ActionChains(self.browser).send_keys(Keys.ESCAPE).perform()
                        # perform este folosita pentru a executa actiuni in browser.
                        i = 600
                        time.sleep(i)
                        print(i)
                        i = random.uniform(0, 60)
                        print(i)
                        time.sleep(i)
                    except:
                        print("A aparut o eroare necunoscuta")
                        time.sleep(10)
                        print("Atentie,a aparut o eroare necunoscuta!")
                    ###va urma....

# if __name__ == '__main__':
clicker = GrepolisBot()
clicker.login()
time.sleep(5)
t2 = Thread(target=clicker.farm)
t2.start()
s = ttk.Style()
s.theme_use('clam')
s.configure("3.Horizontal.TProgressbar", troughcolor='black', background='red')
my_progress = ttk.Progressbar(root, style='3.Horizontal.TProgressbar',
                              orient=HORIZONTAL, length=100, mode='determinate')
my_progress.pack(padx=10, pady=5)

canvas = tk.Canvas(root, height=300, width=300, bg="#000000")
canvas.pack()

b1 = tkinter.Button(root, text="Start farm", command=clicker.alive_set)
b1.pack()
b2 = tk.Button(root, text="Stop farm", command=clicker.alive_clean)
b2.pack()
root.mainloop()
