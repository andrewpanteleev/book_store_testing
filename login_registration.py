# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get("http://practice.automationtesting.in/")
# driver.implicitly_wait(5)
# driver.maximize_window()
#
# account_btn = driver.find_element_by_id("menu-item-50")
# account_btn.click()
# reg_email = driver.find_element_by_id("reg_email")
# reg_email.send_keys("andruha1994@mail.ru")
# reg_password = driver.find_element_by_id("reg_password")
# reg_password.send_keys("Panteleev1994!")
# register_btn = driver.find_element_by_name("register")
# register_btn.click()
#
# driver.quit()

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(5)
driver.maximize_window()


account_btn = driver.find_element_by_id("menu-item-50")
account_btn.click()
username_login = driver.find_element_by_id("username")
username_login.send_keys("andruha1994@mail.ru")
password_login = driver.find_element_by_id("password")
password_login.send_keys("Panteleev1994!")
login_btn = driver.find_element_by_name("login")
login_btn.click()
logout = driver.find_element_by_link_text("Logout")

driver.quit()