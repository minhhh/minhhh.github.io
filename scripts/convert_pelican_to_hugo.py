#!/usr/bin/env python3
"""Convert Pelican Markdown files to Hugo format.

Usage: python scripts/convert_pelican_to_hugo.py <source_dir> [--dry-run]

Reads all .md files from source_dir, parses Pelican frontmatter (plain
key:value lines before first blank line), and writes Hugo TOML frontmatter
(wrapped in +++) to blog/content/post/ (articles) or blog/content/page/ (pages).
"""

import os
import re
import sys
from datetime import datetime


PELICAN_TO_HUGO = {
    "Title": "title",
    "Date": "date",
    "Author": "author",
    "Category": "categories",
    "Tags": "tags",
    "Summary": "description",
    "Slug": "slug",
}

SOURCE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_BASE = os.path.join(SOURCE_DIR, "blog", "content")


def parse_pelican_frontmatter(text):
    lines = text.splitlines()
    frontmatter = {}
    body_start = 0
    for i, line in enumerate(lines):
        if not line.strip():
            body_start = i + 1
            break
        if ":" in line:
            key, _, value = line.partition(":")
            key = key.strip()
            value = value.strip()
            if key in PELICAN_TO_HUGO:
                frontmatter[key] = value
    body = "\n".join(lines[body_start:]).strip()
    return frontmatter, body


def convert_date(date_str):
    try:
        dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
        return dt.strftime("%Y-%m-%dT%H:%M:%S+07:00")
    except ValueError:
        try:
            dt = datetime.strptime(date_str, "%Y-%m-%d")
            return dt.strftime("%Y-%m-%dT00:00:00+07:00")
        except ValueError:
            return date_str


def clean_body(body):
    body = re.sub(r"\{filename\}/images/([^}]+)", r"/img/\1", body)
    body = re.sub(r"\{filename\}/posts/([^}]+)", r"\1", body)
    body = re.sub(r"\[git:repo=([^,]+),file=([^\]]+)\]", r"[\1/\2](https://github.com/\1)", body)
    return body


def toml_value(value):
    value = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{value}"'


def write_frontmatter(frontmatter, body, f):
    f.write("+++\n")
    for pel_key, hugo_key in PELICAN_TO_HUGO.items():
        if pel_key not in frontmatter:
            continue
        val = frontmatter[pel_key]
        if pel_key == "Date":
            f.write(f'{hugo_key} = {toml_value(convert_date(val))}\n')
        elif pel_key in ("Category",):
            f.write(f'{hugo_key} = [{toml_value(val)}]\n')
        elif pel_key == "Tags":
            tags = [t.strip() for t in val.split(",") if t.strip()]
            f.write(f'{hugo_key} = [{", ".join(toml_value(t) for t in tags)}]\n')
        else:
            f.write(f'{hugo_key} = {toml_value(val)}\n')
    f.write("+++\n\n")
    f.write(body)
    if not body.endswith("\n"):
        f.write("\n")


def convert_file(src_path, dry_run=False):
    with open(src_path, "r", encoding="utf-8") as f:
        text = f.read()

    frontmatter, body = parse_pelican_frontmatter(text)
    body = clean_body(body)

    basename = os.path.basename(src_path)
    stem = os.path.splitext(basename)[0]

    is_page = "pages" in src_path.replace("\\", "/").split("/")
    slug = stem
    date_match = re.match(r"(\d{4}-\d{2}-\d{2})-(.+)", stem)
    if date_match and not is_page:
        slug = date_match.group(2)

    if is_page:
        out_dir = os.path.join(OUTPUT_BASE, "page", slug)
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "index.md")
    else:
        out_dir = os.path.join(OUTPUT_BASE, "post")
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, f"{slug}.md")

    if dry_run:
        print(f"[DRY RUN] {src_path} -> {out_path}")
        return

    with open(out_path, "w", encoding="utf-8") as f:
        write_frontmatter(frontmatter, body, f)

    print(f"  -> {out_path}")


def main():
    dry_run = "--dry-run" in sys.argv
    sources = [a for a in sys.argv[1:] if not a.startswith("--")]

    if not sources:
        src = os.path.join(SOURCE_DIR, "blog", "content", "*.md")
        print(f"Usage: python {sys.argv[0]} <source.md>... [--dry-run]")
        print(f"       python {sys.argv[0]} {src}")
        sys.exit(1)

    for src in sources:
        convert_file(src, dry_run=dry_run)


if __name__ == "__main__":
    main()
