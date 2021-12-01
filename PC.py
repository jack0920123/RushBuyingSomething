import select
from  selenium import webdriver
from  selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import datetime

def rush():
    # driver = webdriver.Chrome('./chromedriver.exe')
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')  # 啟動無頭模式 原文網址：https://itw01.com/FYB2UED.html
    chrome_options.add_argument('--disable-gpu')  # windowsd必須加入此行 原文網址：https://itw01.com/FYB2UED.html
    driver = webdriver.Chrome(chrome_options=chrome_options)

    driver.get('https://www.huahuacomputer.com.tw/products/gigabyte-%E6%8A%80%E5%98%89-aorus-15g-yb-%E6%A9%9F%E6%A2%B0%E8%BB%B8%E9%9B%BB%E7%AB%B6%E7%AD%86%E9%9B%BB-1')
    element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="#btn-variable-buy-now"]/div'))
        )

    element.click()

    element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="checkout-container"]/div/div[3]/div[6]/div[2]/section/div[2]/a'))
        )

    element.click()

    username = driver.find_element_by_id('order-customer-name')
    username.send_keys('張銘勛')
    email = driver.find_element_by_id('order-customer-email')
    email.send_keys('jack0920123@gmail.com')
    hometel = driver.find_element_by_id('order-customer-phone')
    hometel.send_keys('033684013')
    phone = driver.find_element_by_id('user-field-60cf368a7bd14300174f3033')
    phone.send_keys('0933247900')

    checkbox = driver.find_element_by_xpath('//*[@id="delivery-form-content"]/div[1]/label/input')
    checkbox.click()

    selectHowntown = driver.find_element_by_xpath('//*[@id="delivery-form-content"]/div[4]/div[1]/span/select')
    choose = Select(selectHowntown)
    choose.select_by_value('object:42')
    time.sleep(0.3)

    selectCode = driver.find_element_by_xpath('//*[@id="delivery-form-content"]/div[4]/div[2]/span/select')
    choose1 = Select(selectCode)
    choose1.select_by_value('object:67')

    address = driver.find_element_by_xpath('//*[@id="delivery-form-content"]/div[5]/input')
    address.send_keys('介壽路二段933巷42弄6衖9號')

    selectBill = driver.find_element_by_xpath('//*[@id="carrier-type"]')
    choose2 = Select(selectBill)
    choose2.select_by_value('1')
    time.sleep(0.3)

    billCode = driver.find_element_by_id('invoice-mobile-barcode')
    billCode.send_keys('/X3YLNBS')


    checkboxs=driver.find_elements_by_css_selector('input[type=checkbox]')
    for checkbox in checkboxs:
        checkbox.click()


    send = driver.find_element_by_id('place-order-btn')
    send.click()
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="checkout-container"]/div/div[3]/div[1]/div[2]/div[1]/div[2]/span[2]'))
    )
    return element.text
def buy(times):
    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        print(now)
        if now >= times:

            while True:
                print('重製中')
                try:
                    if rush() == '訂單處理中':
                        print('成功')
                        break
                except:

                    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')

                    print('失敗')
                    print(now)
                    pass


        # driver = webdriver.Chrome('./chromedriver.exe')
        # driver.close()
            time.sleep(0.01)

if __name__ == "__main__":
    buy("2021-11-11 23:11:00.000000")
    # buy("2021-11-11 23:41:00.000000","2021-11-11 18:41:30.000000")