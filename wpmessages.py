from selenium import webdriver
 
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")

name = input ("Enter the user name")
user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()
count =100
for i in range (count):
    msg = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
    msg.send_keys("This is a quick test to spam gurchet have fun boii")
    send= driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button")
    send.click()