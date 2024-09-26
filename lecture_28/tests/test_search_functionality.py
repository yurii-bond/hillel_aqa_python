from time import sleep


def test_google_search_with_cookies(driver, open_start_page, accept_google_cookies, search_and_submit, check_that_search_has_done):
    open_start_page()
    accept_google_cookies()
    search_and_submit("python")
    assert check_that_search_has_done(), "No search results found"