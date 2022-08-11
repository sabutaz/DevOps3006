from selenium import webdriver
my_driver = webdriver.Chrome(executable_path="/Users/sabybehar/Downloads/chromedriver")
my_driver.get("file:///Users/sabybehar/PycharmProjects/Tip_calc/index.html")
billamt = my_driver.find_element(by="id", value="billamt")
billamt.send_keys("100")
my_driver.find_element(by="xpath", value='//*[@id="serviceQual"]/option[4]').click()
my_driver.find_element(by="id", value="peopleamt").send_keys("3")
my_driver.find_element(by="id", value="musicamt").send_keys("5")
my_driver.find_element(by="id", value="calculate").click()
expected = "10.00"
actual = my_driver.find_element(by="id", value="tip").text










