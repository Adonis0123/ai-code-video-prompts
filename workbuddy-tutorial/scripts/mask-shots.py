"""Mask private areas in the raw WorkBuddy screenshots (shots/ -> assets/).

Maintainer tool: shots/ holds the unmasked originals and is not published;
the repo ships only the masked assets/wb-0*.jpg.

Run: uv run --with pillow python scripts/mask-shots.py
Coordinates are in the original 2048x1285 pixels.
- sidebar task list + avatar/nickname: x 0-377, y >= 450 -> sidebar grey
- 01/02 hover card ("调整配色以去除 AI 感"): replaced by the same area of
  00-clean-patch.jpg (an earlier shot with no card, laid out 6px lower)
- 02 workspace menu folder rows: white, only 新建工作空间 / 打开本地文件夹 stay
"""
from pathlib import Path
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parent.parent
SHOTS, OUT = ROOT / "shots", ROOT / "assets"
SIDEBAR = (247, 247, 247)
WHITE = (255, 255, 255)

clean = Image.open(SHOTS / "00-clean-patch.jpg").convert("RGB")

def mask(name, out, card=False, menu=False):
    im = Image.open(SHOTS / name).convert("RGB")
    d = ImageDraw.Draw(im)
    if card:
        # card spans ~x358-735, y930-1092; take the matching area from the clean shot
        box = (377, 915, 760, 1120)
        patch = clean.crop((box[0], box[1] + 6, box[2], box[3] + 6))
        im.paste(patch, box[:2])
    d.rectangle((0, 450, 377, im.height), fill=SIDEBAR)
    if menu:
        d.rectangle((688, 272, 1002, 546), fill=WHITE)
    im.save(OUT / out, quality=92)

mask("01-new-task.jpg", "wb-01-new-task.jpg", card=True)
mask("02-workspace-menu.jpg", "wb-02-workspace-menu.jpg", card=True, menu=True)
mask("03-prompt-typed.jpg", "wb-03-prompt-typed.jpg")
print("ok")
