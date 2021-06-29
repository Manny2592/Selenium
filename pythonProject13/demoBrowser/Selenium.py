from selenium import webdriver


#Every browser exposes an executable file. Selenium invoke a browser(executable file) in an automated mode
driver=webdriver.Chrome(executable_path="C:/Users/e_man/OneDrive/Desktop/python_selenium_practice/chromedriver.exe")
#can be done on Internet Exploreer

#get the website
driver.get("https://rahulshettyacademy.com/angularpractice")
#get the website by name and send the keys

driver.find_element_by_name("name").send_keys("Sameer Chandravanshi")

#get the website ID and click on it
driver.find_element_by_id("exampleCheck1").click()

#name
driver.find_element_by_name("name").send_keys("Anirudh")

#CSS selector
driver.find_element_by_css_selector("Input[name='name']").send_keys("Emanuel")


driver.find_element_by_css_selector("Input[class='form-control ng-untouched ng-pristine ng-invalid']").send_keys("lodu")

#driver.find_element_by_css_selector("input[type='submit']").click()

#========================================================================================================
#Finding an element by utlizing all the classes from css selector
#print(driver.find_element_by_css_selector("div[class='alert alert-success alert-dismissible']").text)
#========================================================================================================

################################VALIDATION ASSERTION########Finding an element using a class######################

#Finding an element by utlizing a single class from css selector
#print(driver.find_element_by_css_selector("div[class*='alert']").text)

#print(driver.find_element_by_class_name("alert-success").text)

##Xpath is same css Selector
driver.find_element_by_css_selector("Input[name='name']").send_keys("Emanuel")




#========================================================================================================
#X-Path
driver.find_element_by_xpath("//Input[@name='name']").send_keys(" Thomas")

#driver.find_element_by_xpath("//input[@type='submit']").click()

#driver.find_element_by_xpath("//input[@type='submit']").click()

driver.find_element_by_xpath("//input[@type='submit']").click()

#FInding the by text by all the classes mentioned in it
print(driver.find_element_by_xpath("//div[@class='alert alert-success alert-dismissible']").text)

#======================================================================================
#X-Path contains by any one class
print(driver.find_element_by_xpath("//div[contains(@class,'alert-success')]").text)
#//div[contains(@class,'alert')]
#======================================================================================

input#username


print(driver.find_element_by_xpath("//div[contains(@class,'alert-success')]"))

print(driver.find_element_by_xpath("//div[contains(@class,'alert')]"))

print(driver.title)
print(driver.current_url)
#driver.close closes only the current window while driver. quit closes all the windows

#driver.quit() is used for quitting all the windows while driver.close() is used for closing only the current window
#driver.maximize_window()
#driver.refresh()
#driver.minimize_window()
