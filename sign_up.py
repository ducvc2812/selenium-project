from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
def check_sign_up_link(driver):
    """Kiểm tra và click vào link Đăng ký ngay."""
    try:
        # Mở trang web
        driver.get("https://account-uat.kways.io")

        # Chờ cho link xuất hiện và click vào nó
        sign_up_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/sign-up"]'))
        )
        sign_up_link.click()

        # In ra thông tin nếu tìm thấy và click
        print("Tìm thấy liên kết Đăng ký ngay!")
        print("Đã click vào liên kết.")
    except Exception as e:
        print(f"Lỗi khi tìm link Đăng ký ngay: {e}")



def fill_sign_up_form(driver, user_email):

    """Điền thông tin vào form đăng ký và click nút Đăng ký."""
    try:
        # Đợi và điền thông tin các trường bắt buộc
        first_name_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "firstName"))
        )
        first_name_input.send_keys("Nguyễn Văn A")

        last_name_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "lastName"))
        )
        last_name_input.send_keys("B")

        phone_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "phone"))
        )
        phone_input.send_keys("0912345678")

        email_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "email"))
        )
        email_input.send_keys(user_email)

        # Đợi và tìm nút "Đăng ký" bằng XPath 
        sign_up_button = WebDriverWait(driver, 20).until(
           EC.element_to_be_clickable((By.CLASS_NAME, "primaryBtn"))
        )

        # Cuộn đến nút Đăng ký nếu nó bị che khuất
        driver.execute_script("arguments[0].scrollIntoView();", sign_up_button)

        # Kiểm tra nếu nút có thể click và thực hiện click
        if sign_up_button.is_displayed() and sign_up_button.is_enabled():
            ActionChains(driver).move_to_element(sign_up_button).click().perform()
            print("Đã nhấn nút Đăng ký.")
        else:
            print("Nút Đăng ký không thể click được.")
    except Exception as e:
        print(f"Lỗi khi điền form đăng ký: {e}")

def check_yopmail_for_signup_confirmation(driver, user_email):
    """Mở YopMail, tìm và mở email vừa đăng ký."""
    try:
        # Mở tab mới với YopMail
        driver.execute_script("window.open('https://yopmail.com', '_blank');")
        driver.switch_to.window(driver.window_handles[1])  # Chuyển sang tab YopMail

        # Tìm kiếm và nhập địa chỉ email vào trường tìm kiếm
        email_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "login"))  # Trường tìm kiếm email
        )
        email_field.clear()
        email_field.send_keys(user_email)

        # Nhấn Enter để tìm hộp thư đến
        email_field.send_keys(Keys.RETURN)

        # Đợi cho đến khi các email hiển thị
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.m"))
        )

        # Kiểm tra xem có ít nhất một email nào trong hộp thư đến không
        email_elements = driver.find_elements(By.CSS_SELECTOR, "div.m")
        if email_elements:
            # Click vào email đầu tiên
            email_elements[0].click()
            print("Đã mở email xác nhận đăng ký.")
        else:
            print("Không tìm thấy email xác nhận.")

        # Chuyển qua iframe của email
        # iframe = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.ID, "ifmail"))
        # )
        # driver.switch_to.frame(iframe)

        # Tìm button xác nhận và click
        confirm_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Xác nhận')]"))
        )
        confirm_button.click()
        print("Đã nhấn nút xác nhận.")

        # Đợi vài giây để quá trình hoàn tất (có thể thêm xác thực sau khi nhấn)
        time.sleep(3)

    except Exception as e:
        print(f"Lỗi khi tìm kiếm email: {e}")
