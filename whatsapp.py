# import web driver from selenium for automate the WhatsApp message
from selenium import webdriver

# creating an obect to open chrome
driver = webdriver.Chrome('/Users/rauna/Downloads/chromedriver')

# passing the url
driver.get('https://web.whatsapp.com/')

# getting data from user
name = input('enter the name of user')
msg = input('enter your message')
count = int(input("enter the count"))
input('enter anything after scanning QR code')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))

user.click()

msg_box = driver.find_element_by_class_name('_13mgZ')

for i in range(count):
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name('_3M-N-')
    button.click()
