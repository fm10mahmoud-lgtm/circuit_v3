#!/usr/bin/env python3
"""ينزّل مكتبات الواجهة (Tailwind / FontAwesome / Tone.js / خط Cairo) داخل assets/vendor
ليعمل التطبيق بالكامل بدون إنترنت. شغّله مرة واحدة قبل البناء:  python3 scripts/fetch_vendor.py
"""
import os, re, urllib.request

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'app', 'src', 'main', 'assets', 'vendor')
UA_MODERN = 'Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36 Chrome/120 Mobile Safari/537.36'

def get(url, ua=None):
    req = urllib.request.Request(url, headers={'User-Agent': ua or 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()

def save(rel, data):
    path = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, 'wb').write(data)
    print('  ✓', rel, f'({len(data)//1024} KB)')

print('Tailwind / Tone.js')
save('tailwind.js', get('https://cdn.tailwindcss.com/3.4.17'))
save('Tone.js', get('https://cdnjs.cloudflare.com/ajax/libs/tone/14.8.49/Tone.js'))

print('FontAwesome 6.4.0')
base = 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/'
css = get(base + 'css/all.min.css').decode()
save('fa/css/all.min.css', css.encode())
for f in sorted(set(re.findall(r'\.\./webfonts/([\w\-.]+?\.woff2)', css))):
    save('fa/webfonts/' + f, get(base + 'webfonts/' + f))

print('Cairo (Google Fonts)')
gcss = get('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800;900&display=swap', UA_MODERN).decode()
n = 0
def repl(m):
    global n
    n += 1
    name = f'cairo-{n}.woff2'
    save('cairo/' + name, get(m.group(1)))
    return f'url({name})'
save('cairo/cairo.css', re.sub(r'url\((https://[^)]+)\)', repl, gcss).encode())
print('تم. الآن ابنِ التطبيق:  gradle assembleDebug')
