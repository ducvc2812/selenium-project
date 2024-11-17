# kways_login.py
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def login_to_kways(driver, email, password):
    try:
        # Mở trang đăng nhập
        driver.get("https://account-uat.kways.io")
        # Đợi cho trường email xuất hiện và nhập thông tin
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "email"))
        )
        email_input.send_keys(email)

        # Đợi cho trường mật khẩu xuất hiện và nhập thông tin
        password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "password"))
        )
        password_input.send_keys(password)

        # Nhấn nút Đăng nhập
        sign_in_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "primaryBtn"))
        )
        sign_in_button.click()

        # Đợi 5 giây
        time.sleep(5)
    except Exception as e:
        print(f"Lỗi xảy ra: {e}")
