# run_login.py
from kways_login import  login_to_kways
from create_driver import init_drive
from sign_up import check_sign_up_link
from sign_up import fill_sign_up_form
from sign_up import check_yopmail_for_signup_confirmation

if __name__ == "__main__":
    driver = init_drive()
    try:
        #Login
        # login_to_kways(driver, "autoyopmail1@yopmail.com", "123456aA@")
        email_user = 'thanhnguyen1@yopmail.com'
        #Register
        # check_sign_up_link(driver)
        # fill_sign_up_form(driver, email_user)
        check_yopmail_for_signup_confirmation(driver, email_user)
        input("Nhấn Enter để đóng trình duyệt...")
    finally:
        driver.quit()
