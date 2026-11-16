#!/usr/bin/env python3
"""Check every http(s) link in the files you name and write a click list.

Usage: python3 tools/link_report.py FILE [FILE ...] > link_report.md
       python3 tools/link_report.py show-your-work/open-source-education/*.html show-your-work/open-source-education/field-guide/*

Some sites answer scripts with 403 even when a browser works. Those go under "Click these yourself", not "Broken".
Exit code 1 only when something is truly broken (404, 5xx, no connection).
"""
import re, sys, urllib.request, urllib.error

UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
SKIP = ("http://www.w3.org/", "https://example.com")
BLOCKED = {401, 403, 429, 999}

def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "text/html,*/*"})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.status, r.geturl()
    except urllib.error.HTTPError as e:
        return e.code, url
    except Exception as e:
        return 0, str(e)[:60]

def collect(paths):
    found = {}
    for p in paths:
        try:
            text = open(p, encoding="utf-8").read()
        except (OSError, UnicodeDecodeError):
            continue
        for u in re.findall(r'https?://[^\s"<>\')\]]+', text):
            u = u.rstrip(".,;:")
            if not u.startswith(SKIP):
                found.setdefault(u, set()).add(p)
    return found

def main(paths):
    ok, moved, blocked, broken = [], [], [], []
    for url, files in sorted(collect(paths).items()):
        status, final = fetch(url.split("#")[0])
        row = (url, status, final, sorted(files))
        if status == 200 and final.rstrip("/") == url.split("#")[0].rstrip("/"):
            ok.append(row)
        elif status == 200:
            moved.append(row)
        elif status in BLOCKED:
            blocked.append(row)
        else:
            broken.append(row)
    print("# Link report\n")
    print(f"{len(ok)} fine, {len(moved)} redirected, {len(blocked)} to click yourself, {len(broken)} broken.\n")
    def section(title, rows, note=""):
        print(f"## {title} ({len(rows)})\n{note}")
        for url, status, final, files in rows:
            extra = f" -> {final}" if final != url and status == 200 else ""
            print(f"- [ ] <{url}> status {status}{extra}  \n  in: {', '.join(files)}")
        print()
    section("Broken: fix these", broken, "Not found, server error, or no connection.\n")
    section("Click these yourself", blocked, "The site refused a script. Open each in a browser; if it loads, it is fine.\n")
    section("Redirected: consider updating", moved, "Works, but the address changed.\n")
    section("Fine", ok)
    return 1 if broken else 0

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    sys.exit(main(sys.argv[1:]))
