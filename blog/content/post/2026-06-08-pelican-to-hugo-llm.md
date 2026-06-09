+++
title = "Migrating Pelican to Hugo with an AI Agent"
date = "2026-06-08T00:00:00+07:00"
author = "Ha.Minh"
description = "How I used an AI agent (opencode) to migrate this blog from Pelican 3.4 to Hugo with the Stack theme."
slug = "pelican-to-hugo-llm"
categories = ["Programming"]
tags = ["hugo", "pelican", "LLM", "Agent", "blogging"]
+++

I've been running this blog on Pelican 3.4 since 2014. It worked, but the tooling was showing its age. I wanted to switch to Hugo — faster builds, simpler dependency story, and the Stack theme looked great out of the box.

Rather than doing the migration manually, I used an AI agent (opencode) to walk through it step by step.

## What the AI agent handled

- **Conversion script**: Wrote a Python script to convert 65 Pelican-format articles to Hugo frontmatter, handling field mapping, `{filename}` cleanup, and URL preservation.
- **Config scaffolding**: Set up Hugo modules, the Stack theme, and all 6 config files (`config.toml`, `params.toml`, `menu.toml`, `permalinks.toml`, `markup.toml`, `module.toml`).
- **Deployment**: Created a GitHub Actions workflow with hash-pinned actions for supply-chain security.
- **Asset migration**: Moved avatar, favicon, and static images; verified all external image URLs.
- **Site verification**: Ran through every page type, RSS, Disqus, syntax highlighting, dark mode, and search — all confirmed working.
- **Cleanup**: Removed Pelican tooling (`fabfile.py`, `develop_server.sh`, `pelicanconf.py`, old themes, `Pipfile`), updated `Makefile` and README.

## What I did

- Made decisions on menu order, category merges (Web Development → Programming), and deployment strategy (GitHub Actions vs. manual).
- Replaced the placeholder avatar with my actual photo.
- Reviewed and approved each step.

## Result

65 posts converted, 6 config files scaffolded, all old URLs preserved, publishing reduced to a single push:

```bash
git push origin source
```

## Conclusion

Using an AI agent for structured migration work is surprisingly effective. The heavy lifting — script generation, config wiring, verification — maps well to what agents handle best. Validation is inherent to the tools themselves: `hugo` returns build errors, `git diff` shows exactly what changed, and preview servers confirm layout. Each step self-validates, letting the agent progress without needing manual checkpoints.
