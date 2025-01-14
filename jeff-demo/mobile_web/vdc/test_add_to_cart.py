from selenium.webdriver.common.by import By

def test_add_to_cart(mobile_web_driver):
    mobile_web_driver.get('https://www.saucedemo.com/v1/inventory.html')
    mobile_web_driver.find_element(By.CLASS_NAME, 'btn_primary').click()

    assert mobile_web_driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text == '1'

    mobile_web_driver.get('https://www.saucedemo.com/v1/cart.html')
    expected = mobile_web_driver.find_elements(By.CLASS_NAME, 'inventory_item_name')
    assert len(expected) == 1

def test_add_two_to_cart(mobile_web_driver):
    mobile_web_driver.get('https://www.saucedemo.com/v1/inventory.html')
    mobile_web_driver.find_element(By.CLASS_NAME, 'btn_primary').click()
    mobile_web_driver.find_element(By.CLASS_NAME, 'btn_primary').click()

    assert mobile_web_driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text == '2'

    mobile_web_driver.get('https://www.saucedemo.com/v1/cart.html')
    expected = mobile_web_driver.find_elements(By.CLASS_NAME, 'inventory_item_name')
    assert len(expected) == 2
