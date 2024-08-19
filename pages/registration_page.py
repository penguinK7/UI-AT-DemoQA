from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import expected_conditions as EC


class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def fill_form(self, first_name, last_name, email, gender, phone_number, subjects, hobbies, image_path, current_address):
        self.driver.find_element(By.XPATH, '//input[@id="firstName"]').send_keys(first_name)
        self.driver.find_element(By.XPATH, '//input[@id="lastName"]').send_keys(last_name)
        self.driver.find_element(By.XPATH, '//input[@id="userEmail"]').send_keys(email)

        gender_xpath = {
            "Male": '//*[@id="genterWrapper"]/div[2]/div[1]',
            "Female": '//*[@id="genterWrapper"]/div[2]/div[2]',
            "Other": '//*[@id="genterWrapper"]/div[2]/div[3]',
        }
        self.driver.find_element(By.XPATH, gender_xpath[gender]).click()
        
        self.driver.find_element(By.XPATH, '//input[@id="userNumber"]').send_keys(phone_number)
        
        # # Выбор даты рождения из календаря
        # date_parts = date_of_birth.split(" ")
        # day = date_parts[0]
        # month = date_parts[1]
        # year = date_parts[2]

        # date_field = self.driver.find_element(By.ID, "dateOfBirthInput")
        # date_field.click()

        # # Выбор года
        # year_select = WebDriverWait(self.driver, 10).until(
        #     EC.element_to_be_clickable((By.CLASS_NAME, "react-datepicker__year-select"))
        # )
        # year_select.click()
        # self.driver.find_element(By.XPATH, f'//select[@class="react-datepicker__year-select"]//option[text()="{year}"]').click()

        # # Выбор месяца
        # month_map = {
        #     "Jan": "0",
        #     "Feb": "1",
        #     "Mar": "2",
        #     "Apr": "3",
        #     "May": "4",
        #     "Jun": "5",
        #     "Jul": "6",
        #     "Aug": "7",
        #     "Sep": "8",
        #     "Oct": "9",
        #     "Nov": "10",
        #     "Dec": "11"
        # }
        # month_index = month_map[month]
        # month_select = WebDriverWait(self.driver, 10).until(
        #     EC.element_to_be_clickable((By.CLASS_NAME, "react-datepicker__month-select"))
        # )
        # month_select.click()
        # self.driver.find_element(By.XPATH, f'//select[@class="react-datepicker__month-select"]//option[@value="{month_index}"]').click()

        # # Выбор дня
        # day_element = WebDriverWait(self.driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, f'//div[contains(@class, "react-datepicker__day") and text()="{int(day):02d}"]'))
        # )
        # day_element.click()


        # Ожидание и выбор предмета
        subject_input = self.wait.until(EC.element_to_be_clickable((By.ID, 'subjectsInput')))
        subject_input.send_keys(subjects)
        subject_input.send_keys(Keys.RETURN)  # Нажатие Enter, чтобы выбрать предмет

        # Клик на хобби
        for hobby in hobbies:
            hobby_xpath = {
                "Sports": '//*[@id="hobbiesWrapper"]/div[2]/div[1]/label',
                "Reading": '//*[@id="hobbiesWrapper"]/div[2]/div[2]/label',
                "Music": '//*[@id="hobbiesWrapper"]/div[2]/div[3]/label',
            }
            hobby_element = self.driver.find_element(By.XPATH, hobby_xpath[hobby])
            
            # Прокрутка для гарантированного клика
            self.driver.execute_script("arguments[0].scrollIntoView();", hobby_element)
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, hobby_xpath[hobby]))).click()

        self.driver.find_element(By.ID, 'uploadPicture').send_keys(image_path)

        # time.sleep(30)
        
        self.driver.find_element(By.XPATH, '//textarea[@id="currentAddress"]').send_keys(current_address)

        # выбрать страну и город
    
    def submit_form(self):
        # time.sleep(30)
        self.driver.find_element(By.XPATH, '//button[@id="submit"]').click()