import requests

# Put your TikTok CDN URL here
url = "https://v58.tiktokcdn.com/video/tos/useast2a/tos-useast2a-v-2370-euttp/...."

# Add headers so TikTok doesn’t block the request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36"
}

try:
    print("Downloading...")

    res = requests.get(url, headers=headers)

    # If CDN link expired or denied
    if res.status_code != 200:
        print("❌ Download failed. Status:", res.status_code)
        exit()

    # Save video
    with open("tiktok_video.mp4", "wb") as f:
        f.write(res.content)

    print("✅ Download complete: tiktok_video.mp4")

except Exception as e:
    print("❌ Error:", e)