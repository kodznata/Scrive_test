from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

driver_path = "C:/Users/Natasha/GitProjects/Scrive_test/chromedriver.exe"
driver = webdriver.Chrome(service=Service(driver_path))

driver.get("https://staging.scrive.com/t/9221714692410699950/"
            "7348c782641060a9")


def fill_name(id, name):
    name_input = driver.find_element(By.ID, id)
    name_input.send_keys(name)


def click_on_button(xpath):
    button = driver.find_element(By.XPATH, xpath)
    button.click()


def take_screenshot(selector):
    modal = driver.find_element(By.CSS_SELECTOR, selector)
    modal.screenshot("modal.png")


def verify_message(xpath, text):
    message = driver.find_element(By.XPATH, xpath)
    message_text = message.text
    assert text in message_text, \
    f"Expected {text}, but got '{message_text}'"


fill_name("name", "Natallia Kodz")
click_on_button("/html/body/div/div/div[3]/div[4]/div[1]/a[1]")
time.sleep(2)
take_screenshot("body > div > div > div.main > div.section.sign.above-overlay")
click_on_button("/html/body/div/div/div[3]/div[4]/div[1]/a[1]")
time.sleep(2)
verify_message("/html/body/div/div/div[3]/div[2]/div[2]/div/div[1]/h1/span",
               "Document signed!")

driver.quit()
