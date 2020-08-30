from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    # 需要安装chrome driver, 和浏览器版本保持一致
    # http://chromedriver.storage.googleapis.com/index.html

    browser.get('https://shimo.im/welcome')
    time.sleep(1)

  #  browser.switch_to.frame(browser.find_elements_by_tag_name('iframe')[0])
  #  time.sleep(5)
    btm1 = browser.find_element_by_xpath('//*[@id="homepage-header"]/nav/div[3]/a[2]')

    btm1.click()
    print(btm1)
    time.sleep(5)

    browser.find_element_by_xpath('//div[@class="input"]/input[@type="text"]').send_keys('15055495@qq.com')
    browser.find_element_by_xpath('//div[@class="input"]/input[@name="password"]').send_keys('test123test456')
    #li/a[@class="text-link"]
    time.sleep(1)
    browser.find_element_by_xpath('//button[contains(@class,"sm-button submi")]').click()

    cookies = browser.get_cookies()  # 获取cookies
    print(cookies)
    time.sleep(3)

except Exception as e:
    print(e)
finally:
    browser.close()
