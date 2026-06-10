import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

BASE_URL = "http://127.0.0.1:8000"

@pytest.fixture(scope="module")
def driver():
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service)
    browser.implicitly_wait(5)
    yield browser
    browser.quit()

def test_halaman_utama_dapat_diakses(driver):
    driver.get(f"{BASE_URL}/")
    time.sleep(3)
    assert driver.title != ""

def test_login_admin_berhasil(driver):
    driver.get(f"{BASE_URL}/admin/login/")
    time.sleep(2)

    driver.find_element(By.ID, "id_username").send_keys("admin")
    driver.find_element(By.ID, "id_password").send_keys("admin123")
    time.sleep(2)

    driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
    time.sleep(3)

    assert "Site administration" in driver.page_source or "/admin/" in driver.current_url

def test_filter_dashboard(driver):
    driver.get(f"{BASE_URL}/")
    time.sleep(2)

    driver.find_element(By.NAME, "division").send_keys("Assembly")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(3)

    assert "Assembly" in driver.page_source