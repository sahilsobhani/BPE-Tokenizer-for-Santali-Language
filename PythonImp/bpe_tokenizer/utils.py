def load_corpus(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read().strip()
