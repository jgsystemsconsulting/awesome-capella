# Copyright (c) 2026 JG Systems Consulting Ltd. See LICENSE.
# SPDX-License-Identifier: CC0-1.0
import re
import sys
from urllib.parse import urlsplit

readme = open("README.md", encoding="utf-8").read()
LANG = {"Capella", "UAF", "SysML-general"}
TYPE = {"tutorial", "course", "book", "paper", "blog", "video", "tool", "plugin", "docs", "case-study"}
BANNED_SUBSTR = (
    "arcadia-method.com",
    "polarsys",
    "projects.eclipse.org/projects/modeling.capella",
)
# Host-path bans: match netloc+path, not raw substring (download.eclipse.org/capella is allowed)
BANNED_HOST_PATH = (
    ("eclipse.org", "/capella"),
    ("www.eclipse.org", "/capella"),
    ("eclipse.dev", "/capella"),
)
entry = re.compile(r"^- \[([^\]]+)\]\((https?://[^)\s]+)\) - (.*)$")
errors, canonical, n = [], {}, 0
for ln, line in enumerate(readme.splitlines(), 1):
    if not line.startswith("- ["):
        continue
    m = entry.match(line)
    if not m:
        if "](#" not in line:  # Contents lines link to in-page anchors, skip them
            errors.append(f"{ln}: malformed entry line")
        continue
    name, url, rest = m.groups()
    n += 1
    parts = urlsplit(url)
    host = (parts.hostname or "").lower()
    path = parts.path or ""
    for tok in BANNED_SUBSTR:
        if tok in url:
            errors.append(f"{name}: banned host token {tok}")
    for bh, bp in BANNED_HOST_PATH:
        # Exact host match only: download.eclipse.org/capella is allowed (publis/samples)
        if host == bh:
            if path == bp or path.startswith(bp + "/"):
                errors.append(f"{name}: banned host path {bh}{bp}")
    key = (parts.scheme, parts.netloc.lower(), parts.path.rstrip("/"))
    if key in canonical:
        errors.append(f"{ln}: canonical duplicate of line {canonical[key]}: {url}")
    canonical[key] = ln
    if not rest.endswith(")."):
        errors.append(f"{ln}: must end with '(YYYY).'")
        continue
    body, year = rest[:-2].rsplit("(", 1)
    if not re.fullmatch(r"\d{4}", year):
        errors.append(f"{ln}: year token not YYYY: ({year})")
    tags = re.findall(r"`([^`]+)`", body)
    desc = re.sub(r"`[^`]+`", "", body).strip()
    if len(desc) > 140:
        errors.append(f"{ln}: description {len(desc)} chars (> 140)")
    if not tags or tags[0] not in LANG:
        errors.append(f"{ln}: first tag must be a language from {sorted(LANG)}, got {tags[:1]}")
    if len([t for t in tags if t in LANG]) != 1:
        errors.append(f"{ln}: language cardinality must be exactly 1")
    type_tags = [t for t in tags if t in TYPE]
    if len(type_tags) != 1:
        errors.append(f"{ln}: type cardinality must be exactly 1, got {type_tags}")
    if any(re.fullmatch(r"\d{4}", t) for t in tags):
        errors.append(f"{ln}: year must be the parenthetical token, not a backtick tag")
print(f"entries: {n}")
print("\n".join(errors) if errors else "format: OK")
sys.exit(1 if errors else 0)
