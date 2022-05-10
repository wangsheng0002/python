'''同步API'''
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # 可以选择chromium、firefox和webkit
    browser_type = p.chromium
    # 运行chrome浏览器，executablePath指定本地chrome安装路径
    # browser = browser_type.launch(headless=False,slowMo=50,executablePath=r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
    browser = browser_type.launch(headless=False)
    page = browser.new_page()
    page.goto('https://www.baidu.com/')
    page.screenshot(path=f'example-{browser_type.name}.png')
    browser.close()

'''异步步API'''
import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser_type = p.chromium
        browser = await browser_type.launch(headless=False)
        page = await browser.new_page()
        await page.goto('https://www.baidu.com/')
        await page.screenshot(path=f'example-{browser_type.name}.png')
        await browser.close()
asyncio.get_event_loop().run_until_complete(main())



'''模拟手机模式'''
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    iphone_11 = p.devices['iPhone 11 Pro']
    browser = p.webkit.launch(headless=False)
    context = browser.new_context(
        **iphone_11,
        locale='zh-CN'
    )
    page = context.new_page()
    page.goto('https://www.baidu.com/')
    page.click('#logo')
    page.screenshot(path='colosseum-iphone.png')
    browser.close()



'''浏览器中运行JS'''
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.firefox.launch(headless=False, slow_mo=1000)
    page = browser.new_page()
    page.goto('https://www.baidu.com/')
    dimensions = page.evaluate('''() => {
      return {
        width: document.documentElement.clientWidth,
        height: document.documentElement.clientHeight,
        deviceScaleFactor: window.devicePixelRatio
      }
    }''')
    print(dimensions)
    browser.close()


'''录制生成代码'''
'''python -m playwright codegen ，添加--help 查看参数 python -m playwright codegen -h
# -o, --output <file name>  保存脚本到该文件
# --target <language> 指定生成语言 javascript, python, python-async, csharp;默认是python
# -h, --help  查看帮助命令
-b 是指定浏览器，查看其他参数：python -m playwright -h
示例
python -m playwright -b chromium codegen https://www.baidu.com/ -o test.py --target python
'''