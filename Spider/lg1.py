from selenium import webdriver
import time
from datetime import timedelta, date

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from post import *
from ph1 import *

import os

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')
chromedriver = "/usr/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver

d = webdriver.Chrome(chrome_options=chrome_options, executable_path=chromedriver)
# d = webdriver.Chrome()


# d = webdriver.Firefox()
global sys1
sys1 = 0

d.implicitly_wait(5)


def rw():
    time.sleep(1)


def dl(phone):
    d.get('https://www.chaojijishi.com/h5/#/pages/login/login?from=user')
    d.find_element_by_xpath(
        '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[5]/uni-view[1]/uni-input/div/input').send_keys(
        phone)
    rw()
    d.find_element_by_xpath(
        '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[5]/uni-view[2]/uni-input/div/input').send_keys(
        123456)
    rw()
    t = d.find_element_by_xpath(
        '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[5]/uni-view[3]/uni-view[1]/uni-view')
    d.execute_script("arguments[0].click();", t)
    rw()
    t = d.find_element_by_xpath(
        '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[5]/uni-view[5]/uni-view/uni-view')
    d.execute_script("arguments[0].click();", t)
    rw()
    t = d.find_element_by_xpath(
        '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[5]/uni-view[4]')
    d.execute_script("arguments[0].click();", t)
    rw()
    d.get('https://www.chaojijishi.com/h5/#/pages/subpack1/set/user-id-card-data?type=1')


def jiance():
    try:
        WebDriverWait(d, 10).until(lambda d: d.find_element_by_xpath('/html/body/uni-app/uni-toast/div/p'))
        # ?????????????????????
        time.sleep(0.6)
        tip_msg = d.find_element_by_xpath('/html/body/uni-app/uni-toast/div/p').text
        print(tip_msg)
        if tip_msg == "????????????":
            return 1
        return 0
    except TimeoutError:
        d.refresh()
        return 1
        #
    # retries = 1
    # while retries <= 5:
    #     try:
    #         quote = \
    #         wait.until(EC.element_to_be_clickable((By.XPATH, '//h4[@class="quote-number ng-binding"]'))).text.split(
    #             "#")[1]
    #     except TimeoutException:
    #         driver.refresh()
    #         retries += 1


def dj():
    time.sleep(0.8)
    # ????????????
    d.find_element_by_xpath(
        '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[4]/uni-view/uni-image/img').click()

    # ???????????????

    time.sleep(0.6)
    d.find_element_by_xpath(
        '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[1]/uni-view[3]/uni-view').click()

    time.sleep(0.5)
    # ????????????
    d.find_element_by_xpath('/html/body/uni-app/uni-tabbar/div[1]/div[5]').click()

    # ????????????
    time.sleep(2)
    d.find_element_by_xpath(
        '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[1]/uni-view[1]/uni-view[3]/uni-view/uni-view[1]/uni-image').click()

    # ??????????????????
    time.sleep(0.6)
    d.find_element_by_xpath(
        '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[2]/uni-view/uni-text[1]').click()
    # ?????????
    time.sleep(0.6)
    d.find_element_by_xpath(
        '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view/uni-view[3]').click()
    time.sleep(0.4)


def sm(xm, sfz):
    # ????????????
    rw()
    box_name = d.find_element_by_xpath(
        '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[1]/uni-view[2]/uni-input/div/input')
    box_name.send_keys(xm)

    time.sleep(0.9)
    # ???????????????
    box_id = d.find_element_by_xpath(
        '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[1]/uni-view[3]/uni-input/div/input')
    box_id.send_keys(sfz)
    time.sleep(1)

    # ??????
    time.sleep(0.6)
    d.find_element_by_xpath(
        '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[3]/uni-view').click()

    a = jiance()
    if a == 1:
        print('??????')
    else:
        print('??????')
        d.refresh()
    print(d.title)
    print(d.current_url)

    time.sleep(3)
    # d.close()
    return a


def zy():
    rw()
    d.get('https://www.chaojijishi.com/h5/#/pages/subpack1/set/pay-pwd?type=1')
    rw()
    d.find_element_by_xpath(
        '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[1]/uni-view[1]/uni-view[2]/uni-view/uni-input/div/input').send_keys(
        123456)
    rw()
    d.find_element_by_xpath(
        '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[1]/uni-view[2]/uni-view[2]/uni-view/uni-input/div/input').send_keys(
        123456)
    rw()
    d.find_element_by_xpath('/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[2]').click()


def zz():
    rw()
    d.get('https://www.chaojijishi.com/h5/#/pages/subpack1/pay-model/JDpay')
    rw()
    d.find_element_by_xpath(
        '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view/uni-view[1]/uni-view[1]').click()
    rw()
    # ????????????
    d.find_element_by_xpath(
        '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[2]/uni-view[2]/uni-view/uni-view/uni-view[2]/uni-view[2]/uni-input/div/input').send_keys(
        17020411836)
    rw()
    # ????????????
    d.find_element_by_xpath(
        '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[2]/uni-view[2]/uni-view/uni-view/uni-view[3]/uni-view[2]/uni-input/div/input').send_keys(
        5)

    # ????????????
    rw()
    d.find_element_by_xpath(
        '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[2]/uni-view[2]/uni-view/uni-view/uni-view[4]/uni-view[2]/uni-input/div/input').send_keys(
        123456)
    # ??????
    rw()
    d.find_element_by_xpath(
        '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[2]/uni-view[2]/uni-view/uni-view/uni-view[5]/uni-view[2]').click()


def auto():
    global sys1
    p = writeexcle()
    while p is None:
        return 0
    dl(p)
    # dj()
    x = outid()
    sys1 += 1
    a = sm(x[0], x[1])
    while a == 0:
        x = outid()
        sys1 += 1
        a = sm(x[0], x[1])
    zy()
    zz()
    d.close()
    return 1


i = 0
try:
    while auto() == 1:
        i += 1
        print(i)
        d = webdriver.Chrome(chrome_options=chrome_options, executable_path=chromedriver)
        d.implicitly_wait(5)
    print("?????????", sys1)
except Exception:
    print("?????????", sys1)
