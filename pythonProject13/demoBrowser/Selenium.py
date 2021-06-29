from selenium import webdriver


#Every browser exposes an executable file. Selenium invoke a browser(executable file) in an automated mode
driver=webdriver.Chrome(executable_path="C:/Users/e_man/OneDrive/Desktop/python_selenium_practice/chromedriver.exe")
#can be done on Internet Exploreer

#get the website
driver.get("https://rahulshettyacademy.com/angularpractice")
#get the website by name and send the keys

driver.find_element_by_name("name").send_keys("Emanuel Thomas")

#get the website ID and click on it
driver.find_element_by_id("exampleCheck1").click()

#name
driver.find_element_by_name("name").send_keys("Anirudh")

#CSS selector
driver.find_element_by_css_selector("Input[name='name']").send_keys("Emanuel")


driver.find_element_by_css_selector("Input[class='form-control ng-untouched ng-pristine ng-invalid']").send_keys("lodu")



##Xpath is same css Selector
driver.find_element_by_css_selector("Input[name='name']").send_keys("Emanuel")

#X-Path
driver.find_element_by_xpath("//Input[@name='name']").send_keys(" Thomas")

driver.find_element_by_xpath("//input[@type='submit']").click()




print(driver.title)
print(driver.current_url)
#driver.close closes only the current window while driver. quit closes all the windows

#driver.quit() is used for quitting all the windows while driver.close() is used for closing only the current window
#driver.maximize_window()
#driver.refresh()
#driver.minimize_window()
