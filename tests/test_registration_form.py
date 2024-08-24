import os
from selenium import webdriver
from pages.registration_page import RegistrationPage
from config import RESOURCES_DIR
from pages.modal_page import ModalPage


def test_registration_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/automation-practice-form")

    registration_page = RegistrationPage(driver)
    modal_page = ModalPage(driver)

    first_name = "Иван"
    last_name = "Иванов"
    email = "ivan@gmail.com"
    gender = "Male"
    phone_number = "1234567890"
    # date_of_birth = "24 June 2000" # не удалось справиться с календарем
    subjects = "Maths"
    hobbies = ["Reading", "Sports"]
    image_path = os.path.join(RESOURCES_DIR, 'lcvVBfIX-fo.jpg')
    current_address = "123 Ленина"
    state = "NCR"
    city = "Delhi"

    registration_page.fill_form(first_name, last_name, email, gender, phone_number, subjects, hobbies, image_path, current_address, state, city)
    registration_page.submit_form()

    expected_data = {
        "Student Name": f"{first_name} {last_name}",
        "Student Email": email,
        "Gender": gender,
        "Mobile": phone_number,
        # "Date of Birth": "24 June,2000", # не удалось справиться с календарем
        "Subjects": subjects,
        "Hobbies": ', '.join(hobbies),
        "Picture": os.path.basename(image_path),
        "Address": current_address,
        "State and City": f"{state} {city}",
    }

    modal_page.verify_modal_data(expected_data)
    driver.quit()
