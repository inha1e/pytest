from selenium.webdriver.common.by import By

link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_find_item(browser):
    browser.get(link)
    add_button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert add_button
    
    