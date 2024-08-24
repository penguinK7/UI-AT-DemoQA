from selenium.webdriver.common.by import By
from .base_page import BasePage

class ModalPage(BasePage):
    def __init__(self, driver):        
        super().__init__(driver)

    def verify_success_message(self, message):
        """Проверяет, что сообщение об успешности в модальном окне соответствует ожидаемому сообщению."""
        success_message = self.get_element_text((By.CLASS_NAME, 'modal-title'))
        assert success_message == message, f"Ожидалось сообщение '{message}', но было получено '{success_message}'"

    def get_value_from_table(self, label):
        """Получает значение из таблицы по метке"""
        row_locator = (By.XPATH, f'//td[text()="{label}"]/following-sibling::td')
        value = self.get_element_text(row_locator)
        return value

    def verify_modal_data(self, expected_data):
        """Проверяет данные в модальном окне по ожидаемым значениям."""
        for label, expected_value in expected_data.items():
            actual_value = self.get_value_from_table(label)
            assert actual_value == expected_value, f"Ожидалось, что {label} будет '{expected_value}', но было получено '{actual_value}'"
