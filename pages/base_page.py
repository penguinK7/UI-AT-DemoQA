from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find(self, locator):
        """Находит элемент на странице по заданному локатору."""
        return self.driver.find_element(*locator)

    def find_visible(self, locator):
        """Ожидает, пока элемент станет видимым, и возвращает его."""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        """Кликает по элементу, найденному по заданному локатору."""
        self.find(locator).click()

    def send_keys(self, locator, keys):
        """Отправляет текстовые ключи элементу, найденному по заданному локатору."""
        self.find(locator).send_keys(keys)

    def get_element_text(self, locator):
        """Получает текст видимого элемента."""
        element = self.find_visible(locator)
        return element.text

    def get_table_cell(self, table_id, row, col):
        """Находит ячейку таблицы по ее индексам строки и колонки."""
        cell_locator = (By.XPATH, f'//table[@id="{table_id}"]/tbody/tr[{row}]/td[{col}]')
        return self.find_visible(cell_locator)

    def get_table_data(self, table_id):
        """Считывает все данные из таблицы и возвращает их в виде списка списков."""
        data = []
        rows = self.driver.find_elements(By.XPATH, f'//table[@id="{table_id}"]/tbody/tr')
        
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, 'td')
            data.append([col.text for col in cols])
        
        return data