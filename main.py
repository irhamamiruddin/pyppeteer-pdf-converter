import asyncio
from pyppeteer import launch
import os


async def generate_pdf(page, file):
    # change the file extension from .html to .pdf
    path = file.replace('.html', '.pdf')
    await page.pdf({'path': path, 'format': 'A4'})


async def main():
    # Enter your html file path here
    file = "./example.html"
    file = os.path.abspath(file)
    print(file)

    browser = await launch()
    page = await browser.newPage()
    await page.goto(file)
    await generate_pdf(page, file)
    await browser.close()

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
