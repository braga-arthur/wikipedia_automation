from src.driver_factory import create_driver
from src.pages.home_page import HomePage
from src import config
import time

driver = create_driver(headless=False)

wiki = HomePage(driver)
wiki.open(config.BASE_URL)
time.sleep(2)

wiki.search("Carmen Lúcia")
time.sleep(3)

alma_mater = wiki.get_alma_mater()
print("Alma mater:", alma_mater)

driver.quit()
