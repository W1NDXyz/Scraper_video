from TikTokApi import TikTokApi

video_url = "https://www.tiktok.com/@janice_yoong/video/7557009491569691911"

# 1️⃣ 创建 session
with TikTokApi() as api:  # 这里自动创建会话

    # 2️⃣ 获取视频对象
    video = api.video(url=video_url)

    # 3️⃣ 下载视频二进制内容
    video_bytes = video.bytes()

    # 4️⃣ 保存到本地
    with open("tiktok_video.mp4", "wb") as f:
        f.write(video_bytes)

print("✅ 下载完成：tiktok_video.mp4")
