import time

from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def cookie_down(driver_):
    btn_cookie_agreement = driver_.find_element(By.CSS_SELECTOR,
                                               "div[class$='summary-buttons'] button[size='large']:last-child")
    btn_cookie_agreement.click()


trip_type = 'roundtrip'
search_airport_type = 'ap'
search_airport_type_arr = 'mp'

departure = 'krk'
arrival = 'lon'

departure_date = '2022-02-26'
arrival_date = '2022-02-28'

flight_standard = 'economy'

pax_adult = '1'
pax_young = '0'
pax_children = '0'
pax_infant = '0'

url = f'https://www.esky.pl/flights/select/{trip_type}/{search_airport_type}/{departure}/{search_airport_type_arr}/' \
    f'{arrival}?departureDate={departure_date}&returnDate={arrival_date}&pa={pax_adult}&py={pax_young}&pc={pax_children}&pi={pax_infant}&sc={flight_standard}'

# driver = webdriver.Chrome('./drivers/chromedriver')
# driver.get(url)

service = Service('./drivers/chromedriver')
service.start()
driver = webdriver.Remote(service.service_url)
driver.get(url)
wait = WebDriverWait(driver, 10)

# btn_cookie_agreement = driver.find_element(By.CSS_SELECTOR, "div[class$='summary-buttons'] button[size='large']:last-child")
# btn_cookie_agreement.click()

# time.sleep(15)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.badge .content')))
cookie_down(driver)


# def select_progress_bar(driver_):
#     progress = driver_.find_element(
#         by=By.CSS_SELECTOR,
#         value="div progress-bar esky-headline-slider"
#     )
#     return bool(progress)
#
#
# wait.until(select_progress_bar)

amounts = []
flights = driver.find_elements(By.CLASS_NAME, 'flight-content')
for flight in flights:
    amounts.append(flight.find_element(By.CLASS_NAME, 'amount').text)

print(amounts, len(amounts))

# departure = driver.find_element(By.ID, 'departureRoundtrip0')
# departure.send_keys("Kraków, Balice, małopolskie, Polska (KRK)")
#
# arrival = driver.find_element(By.ID, 'arrivalRoundtrip0')
# arrival.send_keys("Malaga, Pablo Ruiz Picasso, Andaluzja, Hiszpania (AGP)")
#
# departure_date = driver.find_element(By.ID, 'departureDateRoundtrip0')
# departure_date.send_keys("2022-02-16")

# arrival_date = driver.find_element(By.ID, 'arrivalDateRoundtrip1')
# arrival_date.send_keys("2022-02-19")

# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()
