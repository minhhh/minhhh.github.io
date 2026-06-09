# minhhh.github.io

Personal blog built with [Hugo](https://gohugo.io/) and the [Stack](https://github.com/CaiJimmy/hugo-theme-stack) theme.

## Quick start

```bash
cd blog && hugo serve --buildDrafts --disableFastRender  # dev server
cd blog && hugo --minify                                   # production build
```

Open http://localhost:1313/.

## Deployment

Push to `source` — GitHub Actions builds and deploys to `main`.

## Configuration

Key site config lives in `blog/config/_default/`:

| File | Purpose |
|---|---|
| `config.toml` | Base URL, title, locale, Disqus, pagination |
| `params.toml` | Sidebar, footer, widgets, GA, Open Graph, color scheme |
| `menu.toml` | Navigation & social menu items |
| `permalinks.toml` | URL scheme |
| `markup.toml` | Syntax highlighting |
| `module.toml` | Hugo module imports (Stack theme) |

## Social

- [LinkedIn](https://www.linkedin.com/in/huy-minh-ha)
- Email: ha.minh.minhhh@gmail.com
