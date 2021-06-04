import pytokapi

info = pytokapi.TikTok().getInfo("https://www.tiktok.com/@..................../video/....................")
print(info['version'])
