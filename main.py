from selenium import webdriver

#Keep browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.youtube.com/')