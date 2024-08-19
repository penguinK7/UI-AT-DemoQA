from selenium import webdriver
from pages.registration_page import RegistrationPage
from config import RESOURCES_DIR
import os


class TestRegistration:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def teardown_method(self):
        self.driver.quit()

    def test_student_registration(self):
        driver = self.driver
        driver.get("https://demoqa.com/automation-practice-form")

        registration_page = RegistrationPage(driver)
        image_path = os.path.join(RESOURCES_DIR, 'lcvVBfIX-fo.jpg')

        # Пример заполнения формы
        registration_page.fill_form(
            first_name="Иван",
            last_name="Иванов",
            email="ivan@test.com",
            gender="Male",
            phone_number="0123456789",
            # date_of_birth="01 Jan 2000",
            subjects="Maths",
            hobbies=["Reading", "Sports"],
            image_path=image_path,  
            current_address="123 Main St"
        )
