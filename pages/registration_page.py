from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage  


class RegistrationPage(BasePage):

    def fill_form(self, first_name, last_name, email, gender, phone_number, subjects, hobbies, image_path, current_address, state, city):
        self.driver.find_element(By.XPATH, '//input[@id="firstName"]').send_keys(first_name)
        self.driver.find_element(By.XPATH, '//input[@id="lastName"]').send_keys(last_name)
        self.driver.find_element(By.XPATH, '//input[@id="userEmail"]').send_keys(email)

        gender_xpath = {
            "Male": '//label[@for="gender-radio-1"]',
            "Female": '//label[@for="gender-radio-2"]',
            "Other": '//label[@for="gender-radio-3"]'
        }
        self.driver.find_element(By.XPATH, gender_xpath[gender]).click()

        self.driver.find_element(By.XPATH, '//input[@id="userNumber"]').send_keys(phone_number)

        # day, month, year = date_of_birth.split()
        # self.driver.find_element(By.ID, "dateOfBirthInput").click()
        
        # # Выбираем год
        # year_selector = self.driver.find_element(By.CSS_SELECTOR, ".react-datepicker__year-select")
        # year_selector.click()
        # year_option = self.driver.find_element(By.XPATH, f'//select[@class="react-datepicker__year-select"]/option[text()="{year}"]')
        # year_option.click()
        
        # # Выбираем месяц
        # month_selector = self.driver.find_element(By.CSS_SELECTOR, ".react-datepicker__month-select")
        # month_selector.click()
        # month_dict = {
        #     "January": "0", "Jan": "0", 
        #     "February": "1", "Feb": "1", 
        #     "March": "2", "Mar": "2", 
        #     "April": "3", "Apr": "3",
        #     "May": "4",
        #     "June": "5", "Jun": "5", 
        #     "July": "6", "Jul": "6", 
        #     "August": "7", "Aug": "7",
        #     "September": "8", "Sep": "8", 
        #     "October": "9", "Oct": "9", 
        #     "November": "10", "Nov": "10", 
        #     "December": "11", "Dec": "11"
        # }
        # month_value = month_dict[month]
        # month_option = self.driver.find_element(By.XPATH, f'//select[@class="react-datepicker__month-select"]/option[@value="{month_value}"]')
        # month_option.click()
        
        # # Выбираем день
        # day_elements = self.driver.find_elements(By.XPATH, f'//div[@class="react-datepicker__day react-datepicker__day--0{int(day):02d}"]')
        # for day_element in day_elements:
        #     if day_element.is_displayed():
        #         day_element.click()
        #         break
        # не получилось никак справиться с календарем

       

        # Выбор предметов
        subject_input = self.driver.find_element(By.ID, 'subjectsInput')
        subject_input.send_keys(subjects)
        subject_input.send_keys(Keys.RETURN)

        # Выбор хобби
        for hobby in hobbies:
            self.click((By.XPATH, f'//label[text()="{hobby}"]'))

        self.send_keys((By.ID, 'uploadPicture'), image_path)
        self.send_keys((By.XPATH, '//textarea[@id="currentAddress"]'), current_address)

        # Выбор штата и города
        self.click((By.XPATH, '//div[@id="state"]'))
        self.click((By.XPATH, f'//div[contains(text(), "{state}")]'))
        
        self.click((By.XPATH, '//div[@id="city"]'))
        self.click((By.XPATH, f'//div[contains(text(), "{city}")]'))

        
    def submit_form(self):
        self.driver.find_element(By.XPATH, '//button[@id="submit"]').click()
