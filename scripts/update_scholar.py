import time, random
from datetime import datetime
from pathlib import Path
from playwright.sync_api import sync_playwright

# ===== 配置 =====
SCHOLAR_USER = "ZbaW22gAAAAJ"  # e.g. "AbCdEfGhIjK"
SCHOLAR_URL = f"https://scholar.google.com/citations?user={SCHOLAR_USER}&hl=en"
WAIT_SEC = 15
# =================

# 仓库根目录 (脚本所在位置的上一级目录)
REPO_ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = REPO_ROOT / "assets" / "images"
OUT_DIR.mkdir(parents=True, exist_ok=True)

OUT_PATH = OUT_DIR / "scholar.png"
OUT_TXT = OUT_DIR / "scholar.txt"


def human_like_actions(page):
    # 随机滚动、鼠标移动来模拟真实用户
    w, h = 1200, 1800
    page.mouse.move(100, 100)
    time.sleep(random.uniform(0.3, 0.8))
    for y in range(100, min(h, 1000), 200):
        page.mouse.wheel(0, 300)
        time.sleep(random.uniform(0.6, 1.2))
    # 随机点击页面任意不重要处以模拟活动
    page.mouse.click(50, 50)
    time.sleep(random.uniform(0.5, 1.0))


def make_stealth_scripts():
    # 这段 JS 注入到页面，覆盖一些自动化检测字段
    return """
    // navigator.webdriver = false
    Object.defineProperty(navigator, 'webdriver', {get: () => false});
    // languages
    Object.defineProperty(navigator, 'languages', {get: () => ['en-US', 'en']});
    // plugins
    Object.defineProperty(navigator, 'plugins', {get: () => [1,2,3,4,5]});
    // chrome object
    window.chrome = { runtime: {} };
    // permissions query overwrite (some checks)
    const originalQuery = window.navigator.permissions.query;
    window.navigator.permissions.__proto__.query = function(parameters) {
      if (parameters && parameters.name === 'notifications') {
        return Promise.resolve({ state: Notification.permission });
      }
      return originalQuery(parameters);
    };
    // webdriver in document
    Object.defineProperty(document, 'hidden', {get: () => false});
    """

def accept_consent(page):
    try_texts = ["I agree", "Accept all", "Agree", "同意", "全部接受"]
    for txt in try_texts:
        try:
            btn = page.locator(f"button:has-text('{txt}')")
            if btn.count() > 0:
                btn.first.click()
                time.sleep(1)
                return True
        except Exception:
            pass
    return False

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, args=[
            "--no-sandbox",
            "--disable-setuid-sandbox",
            "--disable-dev-shm-usage",
            "--disable-blink-features=AutomationControlled"
        ])
        context = browser.new_context(
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            ),
            viewport={"width": 1200, "height": 1800},
            locale="en-US",
            java_script_enabled=True,
            extra_http_headers={
                "Accept-Language": "en-US,en;q=0.9"
            }
        )

        # 注入 stealth JS（在每个新页面创建时运行）
        context.add_init_script(make_stealth_scripts())

        page = context.new_page()

        # 轻微随机等待，模拟真实用户打开浏览器的延迟
        time.sleep(random.uniform(0.5, 2.0))

        try:
            page.goto(SCHOLAR_URL, wait_until="networkidle", timeout=60000)
        except Exception as e:
            print("⚠️ goto 出错:", e)

        # 可能出现隐私同意/阻断页，尝试点击
        accept_consent(page)

        # 再随机等待，等页面渲染
        time.sleep(random.uniform(1.0, 3.0))

        # 做一些人类行为模拟
        try:
            human_like_actions(page)
        except Exception:
            pass

        # 尝试等待主 profile 区域，超时则继续并截图整页（兜底）
        try:
            page.wait_for_selector("#gsc_prf_w", timeout=WAIT_SEC * 1000)
            print("找到 #gsc_prf_w")
        except Exception:
            print("⚠️ 没找到 #gsc_prf_w，直接截整页用于调试")

        # 最后再稍等，确保外部资源加载
        time.sleep(random.uniform(1.0, 2.5))

        # 截图并保存
        page.screenshot(path=str(OUT_PATH), full_page=True)

        # 写时间戳文件，保证每天都有变化
        with open(OUT_TXT, "w", encoding="utf-8") as f:
            f.write(datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC\n"))

        browser.close()

    print("✅ 文件保存位置:", OUT_PATH.resolve())
    print("✅ 输出目录内容:", list(OUT_DIR.glob("*")))


if __name__ == "__main__":
    main()
