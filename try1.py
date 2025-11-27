#今日笔记
# 1. pycharm下载
# 2. 数字与string
# 3. comment 注释 (#)
# 4. 符号 -- 英文
#  5. variable 变量
#  6. diaplay -- print（variable）


# social media > 右上角3点 > more tools > develop tools > network > media > url link



#这里你定义了一个变量 url，用来存放你想下载的视频的网址（链接）。
url ="https://v2.kwaicdn.com/ksc2/cc0gWGWoydU3INjKeLae-Bi4fyEqHewDSJeHBq6nzF5WHYJVdsLR3IkkqMGTxCVR27zFc-wF_L_fvh-pdMPWyoVY_eyWeHQTHfGYYoVbNL15e5DObEPaT3gT7YiRaCn0D9kD8RuNaRVka6G5pCBK2x3nHrii0qkMFeizMt-G4Tu2YMO16_JRkDI0ebKG21ji.mp4?pkey=AAWEaxnMnk7WHQgiMLBA_7nlH_gSWTI2zyp7JqVv72DfJh4xloLVHVBdCAfg78J4aD1PyJ3_29p9BbNfe3wzJCtRdC6bd5QYOik9s83paPZGbHe1x2nWBQBWnnFjxx638UM&tag=1-1764167901-unknown-0-qpvqicwzji-62f4a7924fd61ab4&clientCacheKey=3x3x8bm7d5cvz5q_b.mp4&di=b44beff3&bp=10004&kwai-not-alloc=35&tt=b&ss=vps" 


#是一个用来发送 HTTP 请求的库
import requests


#就是服务器返回的响应对象。
#发送 HTTP GET 请求到你指定的 url。
#如果 URL 已经过期、被封禁或需要 headers，这里会报 403 或 404。
res = requests.get(url)


#二进制写入模式 打开文件 video.mp4，如果文件不存在会自动创建。
open('video3.mp4', 'wb').write(res.content)