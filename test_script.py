import sys
import subprocess

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "playwright"])
    subprocess.check_call([sys.executable, "-m", "playwright", "install", "chromium"])
    from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        print("Navigating to http://127.0.0.1:2000/")
        page.goto("http://127.0.0.1:2000/")
        
        page.wait_for_load_state("networkidle")
        page.wait_for_timeout(2000) # extra wait for rendering
        
        content = page.content()
        if "Resolved" in content:
            print("Page contains 'Resolved'")
        
        bell = page.locator("svg.lucide-bell")
        if bell.count() > 0:
            print("Notification bell icon found.")
            # Trying to find a badge near the bell. Often it's a span with bg-red-500 or similar
            parent = bell.locator("..")
            # Get text of parent just in case badge has number
            print(f"Bell parent text: '{parent.inner_text()}'")
            print(f"Bell parent HTML: {parent.inner_html()}")
            
            try:
                parent.click()
                print("Clicked notification bell (or its parent).")
            except Exception as e:
                print(f"Could not click bell: {e}")
        else:
            print("Notification bell icon NOT found.")
            
        # find resolved count
        resolved = page.get_by_text("Resolved", exact=True)
        if resolved.count() > 0:
            for i in range(resolved.count()):
                parent = resolved.nth(i).locator("..")
                print(f"Resolved panel text: {parent.inner_text()}")
        else:
            print("'Resolved' exactly not found, trying partial")
            resolved = page.get_by_text("Resolved")
            for i in range(resolved.count()):
                parent = resolved.nth(i).locator("..")
                print(f"Resolved panel text: {parent.inner_text()}")
            
        browser.close()

if __name__ == "__main__":
    run()
