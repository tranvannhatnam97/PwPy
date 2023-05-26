import sys
sys.path.insert(0, r'C:\\Users\\hi\\Documents\\Playwright-Python\\PwPy')

import re
from playwright.async_api import Page, expect, BrowserContext, async_playwright
from model.account.login import HomePage
from tools.json_reader import read_json_from_filepath
import pytest
print(__file__)
datas = read_json_from_filepath('C:\\Users\\hi\\Documents\\Playwright-Python\\PwPy\\data\\account\\login.json')
testcases = datas['testcases']
@pytest.mark.parametrize('testcase', testcases)
async def test_go_home(testcase):
    playwright = await async_playwright().start()
    browser = await playwright.webkit.launch(headless=False)
    context = await browser.new_context()
    await context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = await context.new_page()
    homePage = HomePage(page)
    await homePage.go_home()
    await homePage.fill_username(testcase['input']['username'])
    await homePage.fill_password(testcase['input']['password'])
    await homePage.click_login_button()
    await expect(homePage.page.get_by_text('Account Information')).to_have_count(1)
    await context.tracing.stop(path = 'tracedir/' + testcase['TC_id'] + ".zip")
    