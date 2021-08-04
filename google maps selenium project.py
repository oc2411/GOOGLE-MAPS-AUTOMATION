from selenium import webdriver
from time import sleep

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://www.google.co.in/maps")

sleep(3)

def searchplace():
                place=driver.find_element_by_class_name("tactile-searchbox-input")
                place.send_keys("Bangalore")
                submit=driver.find_element_by_xpath("/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/button")
                submit.click()
searchplace()

def directions():
                sleep(5)
                directions=driver.find_element_by_xpath("/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[4]/div[1]/div/button/img")
                directions.click()
directions()

def find():
    sleep(5)
    find = driver.find_element_by_xpath(
        "/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/div/input")
    find.send_keys("pune")
    sleep(5)
    search = driver.find_element_by_xpath(
        "/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/button[1]")
    search.click()
find()

def kilometers():
                sleep(4)
                totalkilometers=driver.find_element_by_xpath("/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[5]/div[2]/div/div[1]/div[1]/div[2]/div")
                print("totalkilometers:",totalkilometers.text)
                sleep(3)

kilometers()





