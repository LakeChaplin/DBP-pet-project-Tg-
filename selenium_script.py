import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
import os

def scrape_best_story(driver):
    best_story = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.stories-feed__container .story:not([style*="display: none"])')))
    story_id = best_story.get_attribute('data-story-id')
    story_title = best_story.find_element(By.CSS_SELECTOR, '.story__title-link').text
    story_url = best_story.find_element(By.CSS_SELECTOR, '.story__title-link').get_attribute('href')
    story_author = best_story.find_element(By.CSS_SELECTOR, '.story__user-link').text
    story_date = best_story.find_element(By.CSS_SELECTOR, '.story__datetime').get_attribute('datetime')
    story_rating = best_story.find_element(By.CSS_SELECTOR, '.story__rating-count').text

    return story_id, story_title, story_url, story_author, story_date, story_rating

def get_best_story_data():
    driver_path = os.environ.get('CHROMEDRIVER_PATH', 'D:/Projects/DBP/chromedriver_win32/chromedriver.exe')
    service = Service(driver_path)

    chrome_options = Options()
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--ignore-ssl-errors')

    with webdriver.Chrome(service=service, options=chrome_options) as driver:
        driver.get('https://pikabu.ru/best?twoday')
        return scrape_best_story(driver)

















































# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.support import expected_conditions as EC
# import ssl
# import os

# from db import insert_post

# def scrape_story_data(driver):
#     first_story = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.stories-feed__container .story:not([style*="display: none"])')))
#     story_id = first_story.get_attribute('data-story-id')
#     story_title = first_story.find_element(By.CSS_SELECTOR, '.story__title-link').text
#     story_url = first_story.find_element(By.CSS_SELECTOR, '.story__title-link').get_attribute('href')
#     story_author = first_story.find_element(By.CSS_SELECTOR, '.story__user-link').text
#     story_date = first_story.find_element(By.CSS_SELECTOR, '.story__datetime').get_attribute('datetime')
#     story_rating = first_story.find_element(By.CSS_SELECTOR, '.story__rating-count').text

#     return story_id, story_title, story_url, story_author, story_date, story_rating

# def process_page(driver):
#     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.stories-feed__container .story:not([style*="display: none"])')))
#     story_id, story_title, story_url, story_author, story_date, story_rating = scrape_story_data(driver)
#     insert_post(story_title, story_author, story_date, story_url, story_rating)

#     print('Story ID:', story_id)
#     print('Story title:', story_title)
#     print('Story URL:', story_url)
#     print('Story author:', story_author)
#     print('Story date:', story_date)
#     print('Story rating:', story_rating)

# def go_to_next_page(driver, prev_story_id):
#     next_button = driver.find_element(By.CSS_SELECTOR, '.pager__item.pager__item_next')
#     next_button.click()

#     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.stories-feed__container .story:not([style*="display: none"])')))
#     current_story_id = driver.find_element(By.CSS_SELECTOR, '.stories-feed__container .story:not([style*="display: none"])').get_attribute('data-story-id')

#     if prev_story_id == current_story_id:
#         time.sleep(2)
#         return go_to_next_page(driver, prev_story_id)

#     return current_story_id

# import random

# def get_random_story(driver):
#     stories = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.stories-feed__container .story:not([style*="display: none"])')))
#     random_story = random.choice(stories)
#     story_id = random_story.get_attribute('data-story-id')
#     story_title = random_story.find_element(By.CSS_SELECTOR, '.story__title-link').text
#     story_url = random_story.find_element(By.CSS_SELECTOR, '.story__title-link').get_attribute('href')
#     story_author = random_story.find_element(By.CSS_SELECTOR, '.story__user-link').text
#     story_date = random_story.find_element(By.CSS_SELECTOR, '.story__datetime').get_attribute('datetime')
#     story_rating = random_story.find_element(By.CSS_SELECTOR, '.story__rating-count').text

#     return story_id, story_title, story_url, story_author, story_date, story_rating



# driver_path = os.environ.get('CHROMEDRIVER_PATH', 'D:/Projects/DBP/chromedriver_win32/chromedriver.exe')
# service = Service(driver_path)

# chrome_options = Options()
# chrome_options.add_argument('--ignore-certificate-errors')
# chrome_options.add_argument('--ignore-ssl-errors')

# with webdriver.Chrome(service=service, options=chrome_options) as driver:
#     driver.get('https://pikabu.ru/best?twoday')

#     while True:
#         try:
#             process_page(driver)
#             story_id = go_to_next_page(driver, story_id)
#         except (ssl.SSLError, ConnectionResetError) as e:
#             print('Error:', e)
#             continue
#         except TimeoutException as e:
#             print('Timeout error:', e)
#             continue
#         except Exception as e:
#             print('Error:', e)
#             break

