from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(5)
driver.maximize_window()

driver.execute_script("window.scrollBy(0, 600);")
selenium_book = driver.find_element_by_id("text-22-sub_row_1-0-2-0-0")
selenium_book.click()
reviews_btn = driver.find_element_by_class_name("reviews_tab")
reviews_btn.click()
stars5 = driver.find_element_by_class_name("star-5")
stars5.click()
comment = driver.find_element_by_id("comment")
comment.send_keys("Nice book!")
author = driver.find_element_by_id("author")
author.send_keys("Andrei")
email = driver.find_element_by_id("email")
email.send_keys("andruha1994@mail.ru")
submit_btn = driver.find_element_by_id("submit")
submit_btn.send_keys("Nice book!")

driver.quit()