from selenium import webdriver

driver=webdriver.Chrome("C:\\Users\\CHINNU FINCY\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.set_page_load_timeout(30)
driver.get("https://www.facebook.com/")
assert "Facebook" in driver.title
#driver.maximize_window()
driver.get_screenshot_as_file("./screenshots/fb1.png")
driver.find_element_by_id("email").send_keys("hi")
driver.find_element_by_id("loginbutton").click()
driver.implicitly_wait(20)

driver.quit()