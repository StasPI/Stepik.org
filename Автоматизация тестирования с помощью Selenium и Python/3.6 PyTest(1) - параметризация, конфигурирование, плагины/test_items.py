import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_check_for_add_to_cart_button(browser):
    browser.get(link)
    time.sleep(30)
    button = len(
        browser.find_elements_by_css_selector(
            '#add_to_basket_form [type="submit"]'))
    assert button > 0, 'no button!'