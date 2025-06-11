import os, hashlib
from datetime import datetime

BASE_URL = "https://games.mahalohana-bruce.com"
SITEMAP_FILE = "sitemap.xml"

def find_html_files(directory="."):
    html_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".html"):
                full_path = os.path.join(root, file).replace("\\", "/")
                if ".git" in full_path or "node_modules" in full_path:
                    continue
                url = BASE_URL + "/" + full_path.lstrip("./")
                html_files.append(url)
    return html_files

def generate_sitemap():
    urls = find_html_files()
    now = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    sitemap = ['<?xml version="1.0" encoding="UTF-8"?>',
               '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for url in urls:
        sitemap.append("  <url>")
        sitemap.append(f"    <loc>{url}</loc>")
        sitemap.append(f"    <lastmod>{now}</lastmod>")
        sitemap.append("    <changefreq>daily</changefreq>")
        sitemap.append("    <priority>0.8</priority>")
        sitemap.append("  </url>")
    sitemap.append("</urlset>")

    new_content = "\n".join(sitemap)

    if os.path.exists(SITEMAP_FILE):
        with open(SITEMAP_FILE, "r", encoding="utf-8") as f:
            old_content = f.read()
        if hashlib.md5(old_content.encode()).hexdigest() == hashlib.md5(new_content.encode()).hexdigest():
            print("✅ No changes detected in sitemap.xml. Skipping write.")
            return

    with open(SITEMAP_FILE, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("✅ sitemap.xml updated.")

if __name__ == "__main__":
    generate_sitemap()
