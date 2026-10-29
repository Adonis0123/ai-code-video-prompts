"""Subset Noto Sans SC (OFL, variable wght) to the glyphs index.html uses.

Run: uv run --with fonttools python scripts/subset-font.py <NotoSansSC[wght].ttf>
Source: https://github.com/google/fonts/tree/main/ofl/notosanssc
Re-run after changing any on-screen text.
"""
import sys
from pathlib import Path
from fontTools import subset

root = Path(__file__).resolve().parent.parent
text = (root / "index.html").read_text(encoding="utf-8")
chars = {c for c in text if ord(c) > 0x7F} | {chr(c) for c in range(0x20, 0x7F)} | set("…「」【】，：！（）0123456789%")
opts = subset.Options()
opts.layout_features = ["*"]
font = subset.load_font(sys.argv[1], opts)
s = subset.Subsetter(opts)
s.populate(text="".join(sorted(chars)))
s.subset(font)
out = root / "assets" / "fonts" / "NotoSansSC-subset.ttf"
subset.save_font(font, str(out), opts)
print(out, out.stat().st_size, "bytes,", len(chars), "chars")
