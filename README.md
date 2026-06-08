# minhhh.github.io

Personal blog built with [Hugo](https://gohugo.io/) and the [Stack](https://github.com/CaiJimmy/hugo-theme-stack) theme.

## Quick start

```bash
# Dev server (with drafts)
cd blog && hugo serve --buildDrafts --disableFastRender

# Production build
cd blog && hugo --minify
```

Open http://localhost:1313/ in the browser.

## Content conversion

To convert Pelican-format articles to Hugo:

```bash
# Convert a single article
python scripts/convert_pelican_to_hugo.py blog/content/2014-06-07-creating-this-blog.md

# Convert all articles
python scripts/convert_pelican_to_hugo.py blog/content/*.md

# Convert pages
python scripts/convert_pelican_to_hugo.py blog/content/pages/*.md

# Dry run (preview only)
python scripts/convert_pelican_to_hugo.py blog/content/*.md --dry-run
```

Output goes to `blog/content/post/` (articles) and `blog/content/page/` (pages as leaf bundles, e.g. `blog/content/page/about/index.md` and `blog/content/page/projects/index.md`).

## Social

- [LinkedIn](https://www.linkedin.com/in/huy-minh-ha)
- Email: ha.minh.minhhh@gmail.com
