#!/usr/bin/env python3
"""Check every http(s) link in the files you name and write a click list.

Usage: python3 tools/link_report.py [-o report.md] FILE_OR_PATTERN [...]
       python3 tools/link_report.py -o link_report.md "show-your-work/open-source-education/*" "show-your-work/open-source-education/field-guide/*"

Quote patterns (the script expands them itself, so it works the same in PowerShell, bash and cmd).
With -o the report is written as UTF-8 to that file; without it, to the screen.

Some sites answer scripts with 403 even when a browser works. Those go under "Click these yourself", not "Broken".
Exit code 1 only when something is truly broken (404, 5xx, no connection).
"""
import glob, io, os, re, sys, urllib.request, urllib.error

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

def expand(args):
    paths = []
    for a in args:
        hits = sorted(glob.glob(a)) or [a]
        paths += [h for h in hits if not os.path.isdir(h)]
    return paths

def collect(paths):
    found = {}
    for p in paths:
        try:
            text = open(p, encoding="utf-8").read()
        except (OSError, UnicodeDecodeError):
            print(f"skipped (not a readable text file): {p}", file=sys.stderr)
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
    args = sys.argv[1:]
    out = None
    if args[:1] == ["-o"] and len(args) > 2:
        out, args = args[1], args[2:]
    if not args:
        sys.exit(__doc__)
    paths = expand(args)
    if out:
        buf = io.StringIO()
        real, sys.stdout = sys.stdout, buf
        code = main(paths)
        sys.stdout = real
        with open(out, "w", encoding="utf-8") as f:
            f.write(buf.getvalue())
        print(buf.getvalue().splitlines()[2], f"(report: {out})")
    else:
        code = main(paths)
    sys.exit(code)
