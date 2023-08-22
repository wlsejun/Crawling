from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os

driver = webdriver.Firefox()
wait = WebDriverWait(driver, 10)

def find_present(css):
    return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css)))

def finds_present(css):
    find_present(css)
    return driver.find_elements(By.CSS_SELECTOR, css)

def find_visible(css):
    return wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, css)))

def finds_visible(css):
    find_visible(css)
    return driver.find_elements(By.CSS_SELECTOR, css)

def choose_one(qestion, stocks):
    print('-------------')
    print(qestion)
    print('-------------')
    for i, stock in enumerate(stocks, start=1):
        print(f"{i}. {stock}")
    choose = input("->")
    return int(choose) -1

driver.get("https://finance.naver.com/sise/sise_market_sum.naver")

#종목 선택
stocks = finds_visible("table.type_2 > tbody:nth-child(4) > tr > td > a")
stocks_text = [x.text for x in stocks if x.text.strip()]  # 공백이 아닌 종목만 선택
i = choose_one("종목을 골라주세요.", stocks_text)
stocks[i].click()

#투자자별 매매동향 이동
investor = finds_visible("ul.tabs_submenu > li:nth-child(4) > a")
investor[0].click()

#
for i in range(4, 10):
    volume = finds_visible(f"table.type2:nth-child(4) > tbody:nth-child(2) > tr:nth-child({i}) > td")
    
    if len(volume) >= 7:  # td 요소가 최소한 7개 이상인 경우에만 선택
        print("날짜:", volume[0].text)
        print("거래량:", volume[4].text)
        print("기관:", volume[5].text)
        print("외국인:", volume[6].text)
        print("-------------")

time.sleep(5)

driver.quit()