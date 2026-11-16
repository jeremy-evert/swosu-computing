#!/usr/bin/env python3
"""Check every http(s) link in a deck. Usage: python3 check_links.py path/to/index.html
Prints the status for each URL and exits 1 if any is not 200 (namespace URLs skipped)."""
import re, sys, urllib.request

SKIP = ("http://www.w3.org/",)

def status(url):
    req = urllib.request.Request(url, headers={"User-Agent": "deck-link-check"})
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            return r.status
    except Exception as e:
        return getattr(e, "code", 0)

def main(path):
    text = open(path, encoding="utf-8").read()
    urls = sorted({u.rstrip(".,)") for u in re.findall(r'https?://[^\s"<>\')]+', text) if not u.startswith(SKIP)})
    bad = 0
    for u in urls:
        s = status(u.split("#")[0])
        bad += s != 200
        print(s, u)
    print(f"{len(urls)} links, {bad} not 200")
    return 1 if bad else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
