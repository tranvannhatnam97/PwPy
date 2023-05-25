import re
from playwright.async_api import Page, expect, BrowserContext, async_playwright
# import playwright
# from pytest import 

def test_go_home(page: Page):
    playwright = async_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    page.goto("https://test-org.ichiba.net/")
    page.locator('#txt_email').fill('mongtoria1@gmail.com')
    page.wait_for_timeout(1000)
    page.locator('#input_password').fill('Cr@zyloop1')
    page.wait_for_timeout(1000)
    page.locator('#btn_submit').click()
    page.wait_for_load_state('domcontentloaded')
    # page.wait_for_timeout(10000)
    expect(page.locator('//h2[contains(text(),"Account Information")]')).to_have_count(1)
    page.wait_for_timeout(5000)
    context.tracing.stop(path = "trace.zip")