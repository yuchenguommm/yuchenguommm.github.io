from playwright.sync_api import sync_playwright
from pathlib import Path

# ========= 配置部分 =========
# 替换成你自己的 Scholar 主页 (user=XXXX)
SCHOLAR_URL = "https://scholar.google.com/citations?user=ZbaW22gAAAAJ"

# 保存截图的路径
OUT_DIR = Path("images")
OUT_DIR.mkdir(parents=True, exist_ok=True)
OUT_PATH = OUT_DIR / "scholar.png"

# Windows 下 Chrome 用户数据目录
# ⚠️ 把 <你的用户名> 换成实际用户名，例如 C:\Users\yuchen\AppData\Local\Google\Chrome\User Data
CHROME_USER_DATA = r"C:\Users\<你的用户名>\AppData\Local\Google\Chrome\User Data"

# ========= 主函数 =========
def main():
    with sync_playwright() as p:
        print(">>> 启动本机 Chrome ...")
        # 使用本机 Chrome，并复用你平时的配置（避免验证码）
        browser = p.chromium.launch_persistent_context(
            user_data_dir=r"C:\Temp\playwright_profile", 
            headless=False,
            channel="chrome"
        )

        page = browser.new_page()
        print(f">>> 打开 {SCHOLAR_URL}")
        page.goto(SCHOLAR_URL, timeout=60000)

        # 等待 Scholar 页面加载（比如 h-index 的元素）
        page.wait_for_selector("#gsc_prf_in", timeout=15000)

        # 保存整页截图
        page.screenshot(path=str(OUT_PATH), full_page=True)
        print(f"✅ 已保存截图到 {OUT_PATH.resolve()}")

        browser.close()

if __name__ == "__main__":
    main()
