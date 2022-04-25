def test_block_user(android_rdc_driver): 
    BLOCKED_MESSAGE = 'Sorry, this user has been locked out.'

    android_rdc_driver.find_element(by="accessibility id", value="open menu").click()
    android_rdc_driver.find_element(by="accessibility id", value="menu item log in").click()
    android_rdc_driver.find_element(by="accessibility id", value="Username input field").send_keys("alice@example.com")
    android_rdc_driver.find_element(by="accessibility id", value="Password input field").send_keys("10203040")
    android_rdc_driver.find_element(by="accessibility id", value="Login button").click()
    
    assert android_rdc_driver.find_element_by_xpath('//android.view.ViewGroup[@content-desc="generic-error-message"]/android.widget.TextView').text == BLOCKED_MESSAGE
    
