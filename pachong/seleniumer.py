#!/usr/bin/env python3
#-*- coding: UTF-8 -*-
from selenium import webdriver # 从selenium导入webdriver

driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
driver.get('https://ssa.jd.com/sso/login?ReturnUrl=http://netsim.jd.com/netProject/projectBasicInfo?id=75') # 获取百度页面
searchButton1 = driver.find_element_by_class_name('login_form_inp_input')
searchButton2 = driver.find_element_by_class_name('login_from_row_password')
searchButton3 = driver.find_element_by_class_name('fromsubmit_btn')


# inputElement = driver.find_element_by_id('inputS1') #获取输入框
# searchButton = driver.find_elements_by_class_name('card-title') #获取搜索按钮

searchButton1.send_keys('gaolei82')
searchButton2.send_keys('Gl1176623625!')
searchButton3.click()
# inputElement.send_keys("5") #输入框输入"Python"
# searchButton.click() #搜索
