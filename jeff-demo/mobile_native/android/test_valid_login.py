import time
def test_standard_user(android_rdc_driver): 
    android_rdc_driver.find_element(by="accessibility id", value="open menu").click()
    android_rdc_driver.find_element(by="accessibility id", value="menu item log in").click()
    android_rdc_driver.find_element(by="accessibility id", value="Username input field").send_keys("bob@example.com")
    android_rdc_driver.find_element(by="accessibility id", value="Password input field").send_keys("10203040")
    android_rdc_driver.find_element(by="accessibility id", value="Login button").click()
    time.sleep(5)
    android_rdc_driver.find_element(by="accessibility id", value="open menu").click()
    android_rdc_driver.find_element(by="accessibility id", value="menu item log in").click()
    
    assert android_rdc_driver.find_element(by="accessibility id", value="Go Shopping button").is_displayed()

    
