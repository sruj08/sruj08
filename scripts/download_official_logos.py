import os
import urllib.request

OFFICIAL_LOGOS = {
    "python": "https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/python.svg",
    "langchain": "https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/langchain.svg",
    "gemini": "https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/googlegemini.svg",
    "javascript": "https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/javascript.svg",
    "typescript": "https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/typescript.svg",
    "solidity": "https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/solidity.svg",
    "ethereum": "https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/ethereum.svg",
    "go": "https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/go.svg",
    "docker": "https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/docker.svg"
}

def download_logos():
    out_dir = "assets/logos"
    os.makedirs(out_dir, exist_ok=True)
    
    headers = {"User-Agent": "Mozilla/5.0"}
    for key, url in OFFICIAL_LOGOS.items():
        dest = os.path.join(out_dir, f"{key}.svg")
        try:
            req = urllib.request.Request(url, headers=headers)
            content = urllib.request.urlopen(req).read().decode("utf-8")
            with open(dest, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Downloaded official logo for {key} -> {dest}")
        except Exception as e:
            print(f"Failed to download {key} from {url}: {e}")

if __name__ == "__main__":
    download_logos()
