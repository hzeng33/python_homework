# Task 6: Scraping Structured Data

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

try: 
    driver.get("https://owasp.org/www-project-top-ten/")
    
    top10_h2 = driver.find_element(By.XPATH, '//h2[@id="top-10-web-application-security-risks"]')
    ul_element = top10_h2.find_element(By.XPATH, './following::ul[1]')
    list_items = ul_element.find_elements(By.TAG_NAME, 'li')
    
    vulnerbilities = []
    
    for li in list_items:
        a_tag = li.find_element(By.TAG_NAME, 'a')
        title = a_tag.text.strip()
        href = a_tag.get_attribute('href')
        vulnerbilities.append({"Title": title, "url":href})
    
    if len(vulnerbilities) > 0:
        df = pd.DataFrame(vulnerbilities)
        print("Extracted data: \n")
        print(df)
        
        df.to_csv('owasp_top_10.csv', index=False)
        print("DataFrame has been written to owasp_top_10.csv")
    else:
        print("No data.")
    
except Exception as e:
    print(f"An exception occurred: {type(e).__name__} {e}")
    
finally:
    driver.quit()