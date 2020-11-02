#-*- coding:utf-8 -*-

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.common.keys import Keys
import os

# os.system('pause')

btn_list = {
    '실습교육':'//*[@id="content-box"]/ul[1]/li[1]/div[1]/p[5]/a',
    '실험전후안전':'//*[@id="content-box"]/ul[1]/li[2]/div[1]/p[5]/a',
    '안전관리실무2':'//*[@id="content-box"]/ul[1]/li[3]/div[1]/p[5]/a',
    '안전의식':'//*[@id="content-box"]/ul[1]/li[4]/div[1]/p[5]/a'
}

sub_btn_list = {
    '실습교육':['//*[@id="content-box"]/div/ul[1]/li/h4/span/a',
            '//*[@id="content-box"]/div/ul[2]/li/h4/span/a'],
    '실험전후안전':['//*[@id="content-box"]/div/ul[1]/li/h4/span/a',
              '//*[@id="content-box"]/div/ul[2]/li/h4/span/a'],
    '안전관리실무2':['//*[@id="content-box"]/div/ul[1]/li/h4/span/a',
               '//*[@id="content-box"]/div/ul[2]/li/h4/span/a',
               '//*[@id="content-box"]/div/ul[3]/li/h4/span/a',
               '//*[@id="content-box"]/div/ul[4]/li/h4/span/a'],
    '안전의식':['//*[@id="content-box"]/div/ul[1]/li/h4/span/a',
            '//*[@id="content-box"]/div/ul[2]/li/h4/span/a',
            '//*[@id="content-box"]/div/ul[3]/li/h4/span/a',
            '//*[@id="content-box"]/div/ul[4]/li/h4/span/a']
}

print("================================")
print("안전교육 자동화를 시작합니다")
print("================================")

info = []

try:
    with open("secu.txt", "r") as f_r:
        line = f_r.readline()
        info = line.split(',')

except Exception as e:
    with open("secu.txt", "w") as f_w:
        id = input("id : ")
        pw = input("pw : ")
        total = id + "," + pw
        f_w.write(total)
        info = [id, pw]
        print("================================")

id = info[0]
pw = info[1]

chromdriver = './chromedriver'

options = webdriver.ChromeOptions()
# options.add_argument("headless")
options.add_argument("disable-gpu")
options.add_argument("lang=ko_KR")

driver = webdriver.Chrome(chromdriver, options=options)

driver.get('https://edu.labs.go.kr/')

driver.find_element_by_name('loginDTO.userId').send_keys(id)
driver.find_element_by_name('loginDTO.userPass').send_keys(pw)

login = driver.find_element_by_xpath('//*[@id="body_login_btn"]')
print("로그인 합니다")
print("================================")
login.click()

mypage = driver.find_element_by_xpath('//*[@id="main02"]/div[1]/fieldset/ul/li[1]/a')
print("마이페이지로 갑니다")
print("================================")
mypage.click()

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
lecture_list = soup.select('div.floatL > p.mT10')

lecture_text_list = []

for lecture in lecture_list:
    lecture_text_list.append(lecture.text)

print("학습하실 강좌 리스트\n")

for lecture in lecture_text_list:
    print(lecture)
print("================================")

study_bool = True

while(study_bool):
    # print("3, 4번만 가능합니다.")
    num = input("1. 실습교육 \n2. 실험전후안전 \n3. 안전관리실무2 \n4. 안전의식 \n 선택 : ")

    print("================================")

    if num == "1":
        btn_code = btn_list['실습교육']
    elif num == "2":
        btn_code = btn_list['실험전후안전']
    elif num == "3":
        btn_code = btn_list['안전관리실무2']
    elif num == "4":
        btn_code = btn_list['안전의식']

    study = driver.find_element_by_xpath(btn_code)
    study.click()

    driver.switch_to.frame('listContentsInfoFrame')

    if num == "1":
        sub_btn_codes = sub_btn_list['실습교육']
    elif num == "2":
        sub_btn_codes = sub_btn_list['실험전후안전']
    elif num == "3":
        sub_btn_codes = sub_btn_list['안전관리실무2']
    elif num == "4":
        sub_btn_codes = sub_btn_list['안전의식']

    sub_study_bool = True

    parent_window = driver.current_window_handle
    print(parent_window)

    while(sub_study_bool):
        sub_study_html = driver.page_source
        sub_sutdy_soup = BeautifulSoup(sub_study_html, 'html.parser')
        sub_lecture_list = sub_sutdy_soup.select('li > h4 > a')

        sub_lecture_text_list = []

        for lecture in sub_lecture_list:
            sub_lecture_text_list.append(lecture.text.strip())

        print("학습하실 강좌 리스트\n")

        for i, lecture in enumerate(sub_lecture_text_list):
            print(str(i) + ". " + lecture)

        all_window = driver.window_handles
        print(all_window)

        sub_num = input("선택 : ")
        sub_num = int(sub_num)
        print("================================")

        sub_study = driver.find_element_by_xpath(sub_btn_codes[sub_num])
        sub_study.click()

        driver.implicitly_wait(10)

        all_window = driver.window_handles
        print(all_window)

        child_window = all_window[-1]

        driver.switch_to.window(child_window)
        print(driver.current_window_handle)

        driver.switch_to.frame('contentsMain')

        driver.maximize_window()

        while(True):
            try:
                time.sleep(2)

                if sub_num < 2:
                    video_html = driver.page_source
                    video_soup = BeautifulSoup(video_html, 'html.parser')
                    times = video_soup.select('div.vjs-duration.vjs-time-control.vjs-control > div')
                    print(times)
                    time_min_sec = []

                    times = times[0].text

                    time_min_sec = times.split('Time')

                    time_min_sec = time_min_sec[1].split(":")

                    min = int(time_min_sec[0])
                    sec = int(time_min_sec[1])
                    total_time = (min * 60) + sec + 3

                    print(time_min_sec)

                else:
                    # driver.implicitly_wait(300)
                    video_html = driver.page_source
                    video_soup = BeautifulSoup(video_html, 'html.parser')
                    times = video_soup.select('div.time > span.time--duration')

                    time_min_sec = []

                    times = times[0].text
                    # print("times :", times)
                    time_min_sec = times.split(":")

                    # print("time :", time)

                    min = int(time_min_sec[0])
                    sec = int(time_min_sec[1])
                    total_time = (min * 60) + sec + 3

                try:
                    if sub_num < 2:
                        mute_btn = driver.find_element_by_xpath('/html/body/footer/nav/ul/li[13]/i[2]')
                    else:
                        mute_btn = driver.find_element_by_xpath('/html/body/div/div[3]/div[6]/div[10]')

                    mute_btn.click()

                except:
                    pass

                # driver.implicitly_wait(total_time)
                time.sleep(total_time)
                # print("sleep")
                if sub_num < 2:
                    print("0")
                    next_btn = driver.find_element_by_xpath('/html/body/footer/nav/ul/li[17]/i')
                else:
                    next_btn = driver.find_element_by_xpath('/ html / body / div / div[3] / div[6] / div[13]')
                next_btn.click()


            except UnexpectedAlertPresentException as e:
                print(e.__dict__["msg"])
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
                driver.switch_to.frame('listContentsInfoFrame')

                break

            except Exception as e:
                print(e)
                continue


        next = input("강의를 다 보셨으면 0번을 누르세요")

        if(next=="0"):
            break
        else:
            continue

    # driver.switch_to_default_content()
    # driver.switch_to.frame('ec141b1710aa0db35ed5a5d406a9d641')
    driver.find_element_by_class_name("close").click()
    # driver.find_element_by_xpath('//*[@id="modal1_box"]/div/div[1]/button').send_keys(Keys.ENTER)
    # close_btn = driver.find_element_by_xpath('//*[@id="modal1_box"]/div/div[1]/button')
    # close_btn.click()
    driver.switch_to_default_content()
    # driver.switch_to.frame('listContentsInfoFrame')
    # driver.switch_to.window(window_name=parent_window)
    print("================================")

driver.quit()