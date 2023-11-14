from selenium.webdriver.common.by import By


def test_answer(browser):
    #link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-cathedral-the-bazaar_190/"
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    btn_flag = False
    try:
        but = browser.find_element(By.CLASS_NAME, "btn-primary.btn-add-to-basket")
        btn_flag = True
    finally:
        assert btn_flag, "button hadn't been found"
