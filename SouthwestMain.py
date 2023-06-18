# Script that checks in to Southwest automatically.  Requires 3 arguments: Confirmation Number, First Name, Last Name
# Example: SouthwestMain.py 3HJD78 David Chau

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import sys

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.southwest.com/")

driver.implicitly_wait(2)

# Takes command line arguments for text fields
#confirmationNumber = "3HJD78"
confirmationNumber = sys.argv[1]
firstName = sys.argv[2]
lastName = sys.argv[3]

# Clicks on Check In Button
driver.find_element(By.CSS_SELECTOR, "button[id='TabbedArea_4-tab-4'] span[class='transition-content'] span span[class='actionable-tab--content']").click()

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.ID, "LandingAirReservationSearchForm_confirmationNumber_check-in")))

# Turning Confirmation Number into a list because website won't take a string
listConfNumber = []
for letter in confirmationNumber:
    listConfNumber.append(letter)
print(listConfNumber)

# Clicks on Confirmation Number box and iterates through list to type in Confirmation Number
for a in listConfNumber:
    driver.find_element(By.ID, "LandingAirReservationSearchForm_confirmationNumber_check-in").send_keys(a)

# Clicks on First Name box and types in First Name
driver.find_element(By.ID, "LandingAirReservationSearchForm_passengerFirstName_check-in").send_keys(firstName)

# Clicks on Last Name box and types in Last Name
driver.find_element(By.ID, "LandingAirReservationSearchForm_passengerLastName_check-in").send_keys(lastName)

# Clicks on Check in button
driver.find_element(By.ID, "LandingAirReservationSearchForm_submit-button_check-in").click()

if driver.find_element(By.CSS_SELECTOR, ".page-error").is_displayed():
    raise AssertionError("Check in was not successful.  Check for errors and try again.")

