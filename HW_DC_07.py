from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException

options = Options()
options.add_argument('start-maximized')
options.headless = False
driver = webdriver.Chrome(options=options)

driver.get("https://www.avito.ru/")

input_avito = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//div[@class='suggest-input-qc1oR']//input"))
)
input_avito.send_keys("авто")

# Нажатие кнопки ENTER
input_avito.send_keys(Keys.ENTER)
time.sleep(5)

list_of_products = []
while True:
# Чтоб прокрутить карточки до самого конца используем while True
    while True:
        try:
            wait = WebDriverWait(driver, 10)
            products = wait.until(EC.presence_of_all_elements_located ((By.XPATH, "//div[@data-marker='catalog-serp']//div[@data-marker='item']")))
            print(len(products))
            count = len(products)
            driver.execute_script("window.scrollBy(0,15000)")
            time.sleep(5)
            products = driver.find_elements(By.XPATH, "//div[@data-marker='catalog-serp']//div[@data-marker='item']")
            if len(products) == count:
                break
        except TimeoutException:
            print("Не удалось найти продукты на странице. Возможно, это последняя страница или страница не загрузилась.")
            break

    
    for product in products:
        product_info = {}
        try:
            name = product.find_element(By.XPATH, ".//h3").text
            price = product.find_element(By.XPATH, ".//div[contains(@class, 'price')]//strong").text
            product_url = product.find_element(By.XPATH, ".//a[@class='iva-item-sliderLink-Fvfau']").get_attribute("href")

            product_info["name"] = name
            product_info["price"] = price
            product_info["url"] = product_url
            list_of_products.append(product_info)
        except Exception as e:
            print(f"Ошибка при извлечении данных для продукта: {e}")

    # Сохранение списка продуктов в JSON файл
    with open("avito_product.json", "w", encoding="utf-8") as f:
        json.dump(list_of_products, f, ensure_ascii=False, indent=4) 

    
    time.sleep(3)
    # Проверяем наличие кнопки "Следующая страница"
    
    try:
        button_next = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//li/a[@aria-label='Следующая страница']")))
        actions = ActionChains(driver)
        actions.move_to_element(button_next).click()
        actions.perform()
        # button_next.click()
    except TimeoutException:
        print("Кнопка 'Следующая страница' не найдена, возможно, вы на последней странице.")
        break

# Закрытие драйвера
driver.quit()
