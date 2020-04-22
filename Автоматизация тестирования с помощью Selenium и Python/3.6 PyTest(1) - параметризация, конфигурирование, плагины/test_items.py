import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_check_for_add_to_cart_button(browser):
    browser.get(link)
    time.sleep(3)
    assert browser.find_elements_by_css_selector(
        '#add_to_basket_form [type="submit"]'), '!!!no button!!!'
