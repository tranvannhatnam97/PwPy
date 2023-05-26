from testscript.account.test_login import test_go_home
from tools.json_reader import read_json_from_filepath
from playwright.async_api import Page, expect, BrowserContext, async_playwright

import pytest
datas = read_json_from_filepath('C:\\Users\\hi\\Documents\\Playwright-Python\\PwPy\\data\\account\\login.json')
testcases = datas['testcases']
# @pytest.mark.parametrize('data', testcases)
# async def test_runner(data):
#     await test_go_home(data)
