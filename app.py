from selenium import webdriver
from flask import Flask, render_template
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

app = Flask(__name__)

@app.route('/')
def connect():
    return render_template('home.html')

@app.route('/addtocart', methods=['GET','POST'])
def my_form_post():
    options = Options()
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("enable-automation")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.amazon.in/")
    element_search = driver.find_elements_by_xpath('//*[@id="twotabsearchtextbox"]')[0]
    time.sleep(1)
    element_search.send_keys("redmi mobiles 9")
    driver.find_elements_by_xpath('//*[@id="nav-search-submit-button"]')[0].click()
    time.sleep(1)
    cart_item = driver.find_elements_by_xpath('//*[@id="search"]/div[1]/div/div[1]/div/span[3]/div[2]/div[4]/div/span/div/div/div[2]/div[1]/div/div/span/a')[0]
    action = ActionChains(driver)
    time.sleep(1)
    action.key_down(Keys.CONTROL).click(cart_item).key_up(Keys.CONTROL).perform()
    driver.switch_to_window(driver.window_handles[1])
    driver.find_element_by_id('add-to-cart-button').click()
    time.sleep(3)
    driver.find_elements_by_xpath('//*[@id="attach-sidesheet-view-cart-button"]/span/input')[0].click()
    return 'success'
if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')