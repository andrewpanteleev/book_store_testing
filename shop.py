# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Chrome()
# driver.get("http://practice.automationtesting.in/")
# driver.implicitly_wait(5)
# driver.maximize_window()
#
# account_btn = driver.find_element_by_id("menu-item-50")
# account_btn.click()
# username_login = driver.find_element_by_id("username")
# username_login.send_keys("andruha1994@mail.ru")
# password_login = driver.find_element_by_id("password")
# password_login.send_keys("Panteleev1994!")
# login_btn = driver.find_element_by_name("login")
# login_btn.click()
# shop_btn = driver.find_element_by_id("menu-item-40")
# shop_btn.click()
# html_5_forms = driver.find_element_by_css_selector(".post-181 > a > h3")
# html_5_forms.click()
# book_title = WebDriverWait(driver, 10).until(
#   EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".product_title"), 'HTML5 Forms'))
#
# driver.quit()

# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get("http://practice.automationtesting.in/")
# driver.implicitly_wait(5)
# driver.maximize_window()
#
# account_btn = driver.find_element_by_id("menu-item-50")
# account_btn.click()
# username_login = driver.find_element_by_id("username")
# username_login.send_keys("andruha1994@mail.ru")
# password_login = driver.find_element_by_id("password")
# password_login.send_keys("Panteleev1994!")
# login_btn = driver.find_element_by_name("login")
# login_btn.click()
# shop_btn = driver.find_element_by_id("menu-item-40")
# shop_btn.click()
# html_ctg = driver.find_element_by_link_text("HTML")
# html_ctg.click()
# items_count = driver.find_elements_by_css_selector("a > h3")
# if len(items_count) == 3:
#     print("3 товара")
# else:
#     print("Ошибка" )
#
# driver.quit()

# from selenium import webdriver
# from selenium.webdriver.support.select import Select
#
# driver = webdriver.Chrome()
# driver.get("http://practice.automationtesting.in/")
# driver.implicitly_wait(5)
# driver.maximize_window()
#
# account_btn = driver.find_element_by_id("menu-item-50")
# account_btn.click()
# username_login = driver.find_element_by_id("username")
# username_login.send_keys("andruha1994@mail.ru")
# password_login = driver.find_element_by_id("password")
# password_login.send_keys("Panteleev1994!")
# login_btn = driver.find_element_by_name("login")
# login_btn.click()
# shop_btn = driver.find_element_by_id("menu-item-40")
# shop_btn.click()
# selector = driver.find_element_by_name("orderby")
# selector_default = selector.get_attribute("value")
# if selector_default == "menu_order":
#     print("По умолчанию")
# else:
#     print("Другая")
# select = Select(selector)
# select.select_by_value("price-desc")
# selector = driver.find_element_by_name("orderby")
# selector_default = selector.get_attribute("value")
# if selector_default == "price-desc":
#     print("По убыванию")
# else:
#     print("Другая")
#
# driver.quit()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Chrome()
# driver.get("http://practice.automationtesting.in/")
# driver.implicitly_wait(5)
# driver.maximize_window()
#
# account_btn = driver.find_element_by_id("menu-item-50")
# account_btn.click()
# username_login = driver.find_element_by_id("username")
# username_login.send_keys("andruha1994@mail.ru")
# password_login = driver.find_element_by_id("password")
# password_login.send_keys("Panteleev1994!")
# login_btn = driver.find_element_by_name("login")
# login_btn.click()
# shop_btn = driver.find_element_by_id("menu-item-40")
# shop_btn.click()
# android_book = driver.find_element_by_css_selector(".post-169 > a > h3")
# android_book.click()
# old_price = driver.find_element_by_css_selector(".price > del > span")
# old_price_text = old_price.text
# assert "₹600.00" in old_price_text
# new_price = driver.find_element_by_css_selector(".price > ins > span")
# new_price_text = new_price.text
# assert "₹450.00" in new_price_text
# book_open = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, ".images > a")))
# book_open.click()
# book_close = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.CLASS_NAME, "pp_close")))
# book_close.click()
#
# driver.quit()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
#
# driver = webdriver.Chrome()
# driver.get("http://practice.automationtesting.in/")
# driver.implicitly_wait(5)
# driver.maximize_window()
#
# shop_btn = driver.find_element_by_id("menu-item-40")
# shop_btn.click()
# html5_webapp = driver.find_element_by_css_selector(".post-182 .add_to_cart_button")
# html5_webapp.click()
# time.sleep(3)
# basket_item = driver.find_element_by_css_selector(".wpmenucart-contents .cartcontents")
# basket_item_text = basket_item.text
# assert "1 Item" in basket_item_text
# basket_price = driver.find_element_by_css_selector(".wpmenucart-contents .amount")
# basket_price_text = basket_price.text
# assert "₹180.00" in basket_price_text
# basket_btn = driver.find_element_by_class_name("wpmenucart-contents")
# basket_btn.click()
# subtotal = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".cart-subtotal .woocommerce-Price-amount"), "₹180.00"))
# total = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".order-total .woocommerce-Price-amount"), "₹189.00"))
#
# driver.quit()

# from selenium import webdriver
# import time
#
# driver = webdriver.Chrome()
# driver.get("http://practice.automationtesting.in/")
# driver.implicitly_wait(5)
# driver.maximize_window()
#
# shop_btn = driver.find_element_by_id("menu-item-40")
# shop_btn.click()
# driver.execute_script("window.scrollBy(0, 300);")
# html5_webapp = driver.find_element_by_css_selector(".post-182 .add_to_cart_button")
# html5_webapp.click()
# time.sleep(3)
# js_data = driver.find_element_by_css_selector(".post-180 .add_to_cart_button")
# js_data.click()
# time.sleep(3)
# basket_btn = driver.find_element_by_class_name("wpmenucart-contents")
# basket_btn.click()
# time.sleep(3)
# remove_btn = driver.find_element_by_class_name("remove")
# remove_btn.click()
# undo_btn = driver.find_element_by_link_text("Undo?")
# undo_btn.click()
# quantity_field = driver.find_element_by_css_selector("tbody > tr:nth-child(1) .product-quantity input")
# quantity_field.clear()
# quantity_field.send_keys("3")
# update_basket = driver.find_element_by_name("update_cart")
# update_basket.click()
# quantity_field_value = quantity_field.get_attribute("value")
# assert "3" in quantity_field_value
# time.sleep(5)
# apply_coupon = driver.find_element_by_name("apply_coupon")
# apply_coupon.click()
# error_message = driver.find_element_by_class_name("woocommerce-error")
# error_message_text = error_message.text
# assert "Please enter a coupon code." in error_message_text
#
# driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(5)
driver.maximize_window()

shop_btn = driver.find_element_by_id("menu-item-40")
shop_btn.click()
driver.execute_script("window.scrollBy(0, 300);")
html5_webapp = driver.find_element_by_css_selector(".post-182 .add_to_cart_button")
html5_webapp.click()
time.sleep(3)
basket_btn = driver.find_element_by_class_name("wpmenucart-contents")
basket_btn.click()
checkout_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "checkout-button")))
checkout_btn.click()
# Чекаут
first_name = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "billing_first_name")))
first_name.send_keys("Andrei")
last_name = driver.find_element_by_id("billing_last_name")
last_name.send_keys("Panteleev")
email = driver.find_element_by_id("billing_email")
email.send_keys("andruha1994@mail.ru")
phone = driver.find_element_by_id("billing_phone")
phone.send_keys("89999999999")
country = driver.find_element_by_id("s2id_billing_country")
country.click()
country_search = driver.find_element_by_id("s2id_autogen1_search")
country_search.send_keys("Russia")
country_select = driver.find_element_by_class_name("select2-match")
country_select.click()
address = driver.find_element_by_id("billing_address_1")
address.send_keys("Street")
city = driver.find_element_by_id("billing_city")
city.send_keys("Moscow")
state = driver.find_element_by_id("billing_state")
state.send_keys("Moscow")
postcode = driver.find_element_by_id("billing_postcode")
postcode.send_keys("111111")
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(3)
# Выберите способ оплаты "Check Payments"
check_payment = driver.find_element_by_id("payment_method_cheque")
check_payment.click()
place_order = driver.find_element_by_id("place_order")
place_order.click()
message = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-thankyou-order-received"),
"Thank you. Your order has been received."))
payment_method = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tfoot > tr:nth-child(3) > td"), "Check Payments"))

driver.quit()