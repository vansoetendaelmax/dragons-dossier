"""Turn a published dossier artifact (full HTML) into a page for the GitHub site.

Usage: python3 tools/site_page.py <artifact.html> <out/index.html>
Adds noindex/no-referrer meta tags and a link back to the site's start page.
"""
import sys, re
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
meta = ('<meta name="robots" content="noindex,nofollow,noarchive">'
        '<meta name="referrer" content="no-referrer">')
if 'name="robots"' not in s:
    s = re.sub(r'(<meta name=viewport[^>]*>|<meta name="viewport"[^>]*>)', r'\1' + meta, s, count=1)
open(dst, 'w', encoding='utf-8').write(s)
print('wrote', dst, len(s))
