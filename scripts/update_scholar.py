import time
from datetime import datetime
from pathlib import Path

from playwright.sync_api import sync_playwright

# ===== 配置 =====
SCHOLAR_USER = "ZbaW22gAAAAJ"  # e.g. "AbCdEfGhIjK"
SCHOLAR_URL = f"https://scholar.google.com/citations?user={SCHOLAR_USER}&hl=en"
WAIT_SEC = 10
# =================

# 仓库根目录 (脚本所在位置的上一级目录)
REPO_ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = REPO_ROOT / "assets" / "images"
OUT_DIR.mkdir(parents=True, exist_ok=True)

OUT_PATH = OUT_DIR / "scholar.png"
OUT_TXT = OUT_DIR / "scholar.txt"


def accept_consent(page):
    """处理可能出现的同意/隐私页面"""
    try_texts = ["I agree", "Accept all", "Agree", "同意", "全部接受"]
    for txt in try_texts:
        btn = page.locator(f"button:has-text('{txt}')")
        if btn.count() > 0:
            btn.first.click()
            return True
    return False


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1280, "height": 2000})

        page.goto(SCHOLAR_URL, wait_until="networkidle", timeout=60000)
        accept_consent(page)

        # 尝试等待简介区，失败则直接截整页
        try:
            page.wait_for_selector("#gsc_prf_w", timeout=WAIT_SEC * 1000)
        except:
            print("⚠️ 没找到 #gsc_prf_w，直接截整页")

        # 截屏
        page.screenshot(path=str(OUT_PATH), full_page=True)

        # 写时间戳文件，保证每天都会变化
        with open(OUT_TXT, "w", encoding="utf-8") as f:
            f.write(datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC\n"))

        browser.close()

    print("✅ 文件保存位置:", OUT_PATH.resolve())
    print("✅ 输出目录内容:", list(OUT_DIR.glob("*")))


if __name__ == "__main__":
    main()
