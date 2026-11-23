#!/usr/bin/env python3
"""產生 圖層/index.json：列出圖層資料夾中的 .geojson / .json / .tile.json 檔案。

網站（GitHub Pages、Netlify 等靜態網站）無法直接列出資料夾內容，
地圖會讀取這份清單來知道有哪些圖層。
使用 GitHub Actions 發佈時會自動執行；手動上傳到其他網站前，請先執行：
    python3 tools/update_layer_index.py
"""
import json
from pathlib import Path

layers_dir = Path(__file__).resolve().parent.parent / "圖層"
files = sorted(
    p.name for p in layers_dir.iterdir()
    if p.is_file()
    and not p.name.startswith(".")
    and p.name.lower() != "index.json"
    and p.suffix.lower() in (".geojson", ".json")
)
(layers_dir / "index.json").write_text(
    json.dumps({"files": files}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
)
print(f"已更新 圖層/index.json，共 {len(files)} 個圖層檔：")
for f in files:
    print("  -", f)
