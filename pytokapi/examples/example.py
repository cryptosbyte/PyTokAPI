import pytokapi

info = pytokapi.TikTok().getInfo("https://www.tiktok.com/@emily.dobson/video/6957418361617681669")
print(info['version'])