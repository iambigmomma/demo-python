def test_standard_user(ios_rdc_driver):
    
    ios_rdc_driver.find_element(by="accessibility id", value="tab bar option menu").click()
    ios_rdc_driver.find_element(by="accessibility id", value="menu item log in").click()
    ios_rdc_driver.find_element(by="accessibility id", value="Username input field").send_keys("bob@example.com")
    ios_rdc_driver.find_element(by="accessibility id", value="Password input field").send_keys("10203040")
    ios_rdc_driver.find_element(by="accessibility id", value="Login button").click()
    ios_rdc_driver.find_element(by="accessibility id", value="tab bar option menu").click()
    ios_rdc_driver.find_element(by="accessibility id", value="menu item log in").click()

    assert ios_rdc_driver.find_element(by="accessibility id", value="Go Shopping button").is_displayed()

