import os, sys, time
from datetime import datetime
from pathlib import Path

from playwright.sync_api import sync_playwright

from pathlib import Path

# 仓库根目录
REPO_ROOT = Path(__file__).resolve().parents[1]

# 正确的保存路径（在仓库里）
OUT_PATH = REPO_ROOT / "assets" / "images" / "scholar.png"

# ===== 配置区（只改 SCHOLAR_USER 即可） =====
SCHOLAR_USER = "ZbaW22gAAAAJ"  # 例如：SCHOLAR_USER = "AbCdEfGhIjK"
SCHOLAR_URL = f"https://scholar.google.com/citations?user={SCHOLAR_USER}&hl=en"
VIEWPORT_W, VIEWPORT_H = 1280, 2000            # 视窗大小，可按需调整
WAIT_SEC = 10                                  # 最长等待时间（秒）
# ==========================================

def ensure_dirs():
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)

def accept_consent(page):
    # 有时会出现“Before you continue”/同意隐私弹窗，这里尝试点掉
    try_texts = [
        "I agree", "Accept all", "Agree", "同意", "全部接受"
    ]
    for txt in try_texts:
        btn = page.locator(f"button:has-text('{txt}')")
        if btn.count() > 0:
            btn.first.click()
            return True
    return False

def main():
    ensure_dirs()
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            locale="en-US",
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            ),
            viewport={"width": VIEWPORT_W, "height": VIEWPORT_H},
        )
        page = context.new_page()

        page.goto(SCHOLAR_URL, wait_until="domcontentloaded", timeout=60000)

        # 可能遇到隐私/同意页
        accept_consent(page)

        try:
            page.wait_for_selector("#gsc_prf_w", timeout=30000)
        except:
            print("⚠️ 没找到 #gsc_prf_w，直接截图整个页面以调试")
        
        page.screenshot(path=str(OUT_PATH), full_page=True)

        # 也顺手写一个时间戳，便于你在页面上显示“更新于”
        with open(OUT_PATH.with_suffix(".txt"), "w", encoding="utf-8") as f:
            f.write(datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC"))

        browser.close()

if __name__ == "__main__":
    main()
