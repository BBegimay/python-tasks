import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login():
   driver = webdriver.Chrome('/Users/begimaybaiturinova/Downloads/chromedriver')
   driver.get('http://petfriends1.herokuapp.com/login')

   # Вводим email
   driver.find_element_by_id('email').send_keys('vasya@mail.com')
   # Вводим пароль
   driver.find_element_by_id('pass').send_keys('12345')
   # Нажимаем на кнопку входа в аккаунт
   driver.find_element_by_css_selector('button[type="submit"]').click()
   # Проверяем, что мы оказались на главной странице пользователя

   assert driver.find_element_by_tag_name('h1').text == "PetFriends"


def test_pets_count_matches():
   driver = webdriver.Chrome('/Users/begimaybaiturinova/Downloads/chromedriver')
   driver.get('http://petfriends1.herokuapp.com/login')

   # Вводим email
   driver.find_element_by_id('email').send_keys('vasya@mail.com')
   # Вводим пароль
   driver.find_element_by_id('pass').send_keys('12345')
   # Нажимаем на кнопку входа в аккаунт
   driver.find_element_by_css_selector('button[type="submit"]').click()
   driver.implicitly_wait(5)

   driver.get('http://petfriends1.herokuapp.com/my_pets')
   WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.ID, "all_my_pets"))
   )

   info_block = driver.find_element_by_css_selector('body > div.task2.fill > div > div.\.col-sm-4.left').text.split("\n")
   pets_count = int(info_block[1].replace('Питомцев: ', ''))

   pet_rows = driver.find_elements_by_css_selector('#all_my_pets > table > tbody > tr')
   assert pets_count == len(pet_rows)

   images = driver.find_elements_by_css_selector('#all_my_pets > table > tbody > tr > th > img')
   assert pets_count / 2 <= len(images)


def test_half_pets_have_images():
   driver = webdriver.Chrome('/Users/begimaybaiturinova/Downloads/chromedriver')
   driver.get('http://petfriends1.herokuapp.com/login')

   # Вводим email
   driver.find_element_by_id('email').send_keys('vasya@mail.com')
   # Вводим пароль
   driver.find_element_by_id('pass').send_keys('12345')
   # Нажимаем на кнопку входа в аккаунт
   driver.find_element_by_css_selector('button[type="submit"]').click()

   driver.implicitly_wait(5)

   driver.get('http://petfriends1.herokuapp.com/my_pets')
   WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.ID, "all_my_pets"))
   )

   pet_rows = driver.find_elements_by_css_selector('#all_my_pets > table > tbody > tr')
   images = driver.find_elements_by_css_selector('#all_my_pets > table > tbody > tr > th > img')
   assert len(pet_rows) / 2 <= len(images)


def test_all_pets_have_names_ages_types():
   driver = webdriver.Chrome('/Users/begimaybaiturinova/Downloads/chromedriver')
   driver.get('http://petfriends1.herokuapp.com/login')

   # Вводим email
   driver.find_element_by_id('email').send_keys('vasya@mail.com')
   # Вводим пароль
   driver.find_element_by_id('pass').send_keys('12345')
   # Нажимаем на кнопку входа в аккаунт
   driver.find_element_by_css_selector('button[type="submit"]').click()

   driver.implicitly_wait(5)

   driver.get('http://petfriends1.herokuapp.com/my_pets')
   WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.ID, "all_my_pets"))
   )

   pet_rows = driver.find_elements_by_css_selector('#all_my_pets > table > tbody > tr')

   for i in range(len(pet_rows)):
      assert pet_rows[i].find_element_by_css_selector('td:nth-child(2)').text != '' #name
      assert pet_rows[i].find_element_by_css_selector('td:nth-child(3)').text != '' #age
      assert pet_rows[i].find_element_by_css_selector('td:nth-child(4)').text != '' #type


def test_all_pets_have_unique_names():
   driver = webdriver.Chrome('/Users/begimaybaiturinova/Downloads/chromedriver')
   driver.get('http://petfriends1.herokuapp.com/login')

   # Вводим email
   driver.find_element_by_id('email').send_keys('vasya@mail.com')
   # Вводим пароль
   driver.find_element_by_id('pass').send_keys('12345')
   # Нажимаем на кнопку входа в аккаунт
   driver.find_element_by_css_selector('button[type="submit"]').click()

   driver.implicitly_wait(5)

   driver.get('http://petfriends1.herokuapp.com/my_pets')
   WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.ID, "all_my_pets"))
   )

   pet_rows = driver.find_elements_by_css_selector('#all_my_pets > table > tbody > tr')
   names = set()

   for i in range(len(pet_rows)):
      name = pet_rows[i].find_element_by_css_selector('td:nth-child(2)').text
      assert name not in names
      names.add(name)


def test_all_pets_are_unique():
   driver = webdriver.Chrome('/Users/begimaybaiturinova/Downloads/chromedriver')
   driver.get('http://petfriends1.herokuapp.com/login')

   # Вводим email
   driver.find_element_by_id('email').send_keys('vasya@mail.com')
   # Вводим пароль
   driver.find_element_by_id('pass').send_keys('12345')
   # Нажимаем на кнопку входа в аккаунт
   driver.find_element_by_css_selector('button[type="submit"]').click()

   driver.implicitly_wait(5)

   driver.get('http://petfriends1.herokuapp.com/my_pets')
   WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.ID, "all_my_pets"))
   )

   pet_rows = driver.find_elements_by_css_selector('#all_my_pets > table > tbody > tr')
   pets = set()

   for i in range(len(pet_rows)):
      pet = pet_rows[i].text
      assert pet not in pets
      pets.add(pet)