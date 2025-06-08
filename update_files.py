from datetime import datetime

# 1. robots.txt
robots_txt = """User-agent: *
Allow: /

Sitemap: https://www.mahalohana-bruce.com/sitemap.xml

#DaumWebMasterTool:160f060c046ce0629c1cd68a964c2d8f836de4219c3d362711b8bb43b5b92e42:NnJbOlYdct0Jzm/G1OzHmA==
"""

with open("robots.txt", "w", encoding="utf-8") as f:
    f.write(robots_txt)

# 2. ads.txt
ads_txt = """google.com, pub-5508768187151867, DIRECT, f08c47fec0942fa0
# Last updated: {}
""".format(datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC'))

with open("ads.txt", "w", encoding="utf-8") as f:
    f.write(ads_txt)
