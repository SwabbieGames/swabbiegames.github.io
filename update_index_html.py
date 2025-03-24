import os

BOT_FOLDER = 'discord_posts'
HTML_FILE = 'index.html'

def read_post(filename):
    path = os.path.join(BOT_FOLDER, filename)
    return open(path, 'r', encoding='utf-8').read() if os.path.exists(path) else ''

with open(HTML_FILE, 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('{{ latest_update }}', read_post('updates'))
html = html.replace('{{ latest_patch_notes }}', read_post('patch_notes'))
html = html.replace('{{ latest_roadmap }}', read_post('roadmap'))

with open(HTML_FILE, 'w', encoding='utf-8') as f:
    f.write(html)
