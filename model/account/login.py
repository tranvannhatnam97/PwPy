from playwright.sync_api import Page, expect, BrowserContext, sync_playwright

class HomePage:
    def __init__(self, page):
        self.page = page
        self.username = None
        self.password = None
        self.username_input = self.page.locator('#txt_email')
        self.password_input = self.page.locator('#input_password')
        self.login_button = self.page.locator('#btn_submit')
    async def go_home(self):
        await self.page.goto("https://test-org.ichiba.net/")
    async def fill_username(self, txt):
        await self.username_input.fill(txt)
    async def fill_password(self, txt):
        await self.password_input.fill(txt)
    async def click_login_button(self):
        await self.login_button.click()
        await self.page.wait_for_load_state('domcontentloaded')