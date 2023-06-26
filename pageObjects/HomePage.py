# Objects located on www.southwest.com home page

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.southwest.com/")

driver.implicitly_wait(2)

class HomePageObjects:

    def CheckInBtn(self):
        return driver.find_element(By.CSS_SELECTOR, "button[id='TabbedArea_4-tab-4'] span[class='transition-content'] span span[class='actionable-tab--content']")

    def ConfirmationNumBox(self):
        return driver.find_element(By.ID, "LandingAirReservationSearchForm_confirmationNumber_check-in")

    def FirstNameBox(self):
        return driver.find_element(By.ID, "LandingAirReservationSearchForm_passengerFirstName_check-in")

    def LastNameBox(self):
        return driver.find_element(By.ID, "LandingAirReservationSearchForm_passengerLastName_check-in")

    def CheckInSubmit(self):
        return driver.find_element(By.ID, "LandingAirReservationSearchForm_submit-button_check-in")