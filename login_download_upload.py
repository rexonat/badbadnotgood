import os
import time
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright
from gdrive_upload import upload_to_drive

load_dotenv()

DOWNLOAD_DIR = "/app/downloads"

os.makedirs(DOWNLOAD_DIR, exist_ok=True)

def automate_download():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(accept_downloads=True)
        page = context.new_page()

        # Example login
        page.goto("https://example.com/login")
        page.fill('input[name="username"]', 'my_username')
        page.fill('input[name="password"]', 'my_password')
        page.click('button[type="submit"]')
        page.wait_for_load_state("networkidle")

        # Go to download page
        page.goto("https://example.com/dashboard/download")
        with page.expect_download() as download_info:
            page.click("text='Download CSV'")
        download = download_info.value
        file_path = os.path.join(DOWNLOAD_DIR, download.suggested_filename)
        download.save_as(file_path)
        print(f"Downloaded to: {file_path}")

        browser.close()
        return file_path

if __name__ == "__main__":
    downloaded_file = automate_download()
    upload_to_drive(downloaded_file)
