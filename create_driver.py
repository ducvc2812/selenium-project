from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

def init_drive():
    # Khởi tạo đối tượng Options
    chrome_options = Options()
    chrome_options.add_argument("--no-cache")
    chrome_options.add_argument("--disable-application-cache")
    chrome_options.add_argument("--incognito")  # Khởi động ở chế độ ẩn danh
    chrome_options.add_argument("--disable-extensions")  # Tắt các tiện ích mở rộng
    chrome_options.add_argument("--disable-plugins")  # Tắt các plugin

    # Cấu hình đường dẫn đến Chrome
    chrome_options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

    # Cấu hình WebDriver
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), 
        options=chrome_options
    )

    return driver
