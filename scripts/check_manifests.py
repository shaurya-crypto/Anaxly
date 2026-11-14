import json

for ch in range(9, 14):
    m_path = f"public/extracted_diagrams/ch{ch}/manifest.json"
    with open(m_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    print(f"\n================ CHAPTER {ch} ({len(data)} figures) ================")
    for i, fig in enumerate(data):
        print(f"[{i+1}] {fig.get('filename')} (p.{fig.get('page')}) -> {fig.get('caption', '')[:100]}")
