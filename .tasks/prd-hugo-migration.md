# Pelican-to-Hugo Migration — Stack Theme

---

## 1. Product Specification

### Feature Overview

Migrate the existing Pelican 3.4 blog at `minhhh.github.io` (frozen since July 2020) to Hugo with the [hugo-theme-stack](https://github.com/CaiJimmy/hugo-theme-stack) v4 theme. Preserve all 62 posts, 2 pages (About, Projects), existing URLs, Disqus comments, Google Analytics, and social links. Re-establish a clean branch workflow for future publishing.

### User Stories / Requirements

- **us-01**: As a visitor, all 62 existing articles and 2 pages must render correctly under the Stack theme with identical or improved readability.
- **us-02**: As a visitor, all existing URLs (`/posts/{slug}/`, `/pages/{slug}/`, `/tag/{tag}/`, `/category/{cat}/`, `/201X/` archives) must either persist or redirect to the new Hugo URL scheme.
- **us-03**: As a visitor, Disqus comments on old articles must remain visible (threads are keyed by URL).
- **us-04**: As the author, I can write a new Markdown post, run a single command, and deploy to GitHub Pages.
- **us-05**: As the author, the site must support dark mode, search, tags, categories, and RSS — all provided by Stack.
- **us-06**: As the author, Google Analytics (UA-50796592-2) must continue tracking.
- **us-07**: As the author, the GitHub Pages live branch (`master`) must serve the Hugo output, and source must live in a separate branch (`source`).

---

## 2. Active Dashboard

- [x] **task-05**: Create pages (About, Projects)
- [ ] **task-06**: Rearrange left menu in order: Home, About, Projects, Archives
- [ ] **task-07**: Configure site params (social, analytics, Disqus, sidebar, widgets, footer)
- [ ] **task-08**: Configure Hugo deployment & branch workflow
- [ ] **task-09**: Handle images, static assets, and external image references
- [ ] **task-10**: Build & verify site locally; fix rendering issues
- [ ] **task-11**: Clean up Pelican tooling from source branch, update README

---

## 3. Active Task Details

### task-05: Create pages (About, Projects)

- **Objective**: Convert the two pages (About, Projects) to Hugo format and place them under `blog/content/page/`.

- **Checklist**:
  - [x] Convert `pages/about.md` → `blog/content/page/about/index.md`
  - [x] Convert `pages/projects.md` → `blog/content/page/projects/index.md`
  - [x] Verify `blood-brothers.jpg` is placed at `blog/content/page/projects/images/` or `blog/static/img/`
  - [x] Verify pages render at `/about/` and `/projects/`
  - [x] Verify permalinks.toml `page = "/:slug/"` works
  - [x] Update README.md with pages info

- **Dependencies**: task-03 (script)

---

### task-06: Rearrange left menu in order: Home, About, Projects, Archives

- **Objective**: Rearrange the left navigation menu items so they appear in the specified order (Home, About, Projects, Archives).

- **Checklist**:
  - [ ] Add `weight` parameters to `[[main]]` menu items in `blog/config/_default/menu.toml` to enforce the order: Home (1), About (2), Projects (3), Archives (4)
  - [ ] Verify the menu displays in the correct order in local development

- **Dependencies**: task-02

---

### task-07: Configure site params (social, analytics, Disqus, sidebar, widgets, footer)

- **Objective**: Finalize all remaining Stack theme configuration for production.

- **Checklist**:
  - [ ] Replace `G-XXXXXXXX` in params.toml with actual GA4 measurement ID (migrated from UA-50796592-2)
  - [ ] Add Disqus shortname (`minhhh`) in config.toml
  - [ ] Configure sidebar: author name, avatar, subtitle, social links
  - [ ] Configure footer: copyright, since year (2014)
  - [ ] Configure widgets: search, archives, categories, tag cloud
  - [ ] Configure article: reading time, license (CC BY-NC-SA 4.0)
  - [ ] Create a simple avatar image (`blog/static/img/avatar.png`)
  - [ ] Create a favicon (`blog/static/img/favicon.png`) — reuse from current site
  - [ ] Set up Open Graph for Twitter (`@utsace`)
  - [ ] Set color scheme to `auto` with toggle enabled
  - [ ] Update README.md with site configuration details

- **Dependencies**: task-02

---

### task-08: Configure Hugo deployment & branch workflow

- **Objective**: Define the new git workflow and deployment mechanism. The Pelican flow used `source → make publish → gh-pages → merge master`. The Hugo flow should be simpler.

- **Checklist**:
  - [ ] Decide deployment method:
    - **Option A**: GitHub Actions — build Hugo on push to `source`, deploy to `master`
    - **Option B**: Manual — `hugo && ghp-import -p public/`
    - **Option C**: `hugo` output goes into `master` root directly
  - [ ] Write `blog/Makefile` with targets: `dev`, `build`, `publish`
  - [ ] Write root `Makefile` targets: `install`, `serve`, `publish` (replacing old Pelican one)
  - [ ] Create `.github/workflows/hugo.yml` for GitHub Actions auto-deploy (if Option A)
  - [ ] Add `.gitignore` entries for `blog/public/`, `blog/resources/`
  - [ ] Document the workflow: `source` → edit → `make publish` → pushes to `master`
  - [ ] Update README.md with deployment workflow

**Proposed workflow:**
```
source branch (write/edit) → hugo build → master branch (live)
```

**Root Makefile:**
```makefile
install:
    cd blog && npm install -g hugo-extended  # or brew

serve:
    cd blog && hugo serve

build:
    cd blog && hugo

publish: build
    cd blog && ghp-import -p -b master public/
```

Or use GitHub Actions:
```yaml
# .github/workflows/hugo.yml
name: Deploy Hugo
on:
  push:
    branches: [source]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: peaceiris/actions-hugo@v2
      - run: cd blog && hugo
      - uses: peaceiris/actions-gh-pages@v3
        with:
          publish_dir: ./blog/public
          publish_branch: master
          cname: minhhh.github.io
```

- **Dependencies**: task-02

---

### task-09: Handle images, static assets, and external image references

- **Objective**: Migrate local images and ensure external images still work. Handle the Pelican `{filename}` macro in article bodies.

- **Checklist**:
  - [ ] Copy `blog/content/images/blood-brothers.jpg` → `blog/content/page/projects/images/` or `blog/static/img/`
  - [ ] Find all `{filename}` references in articles via grep and replace with correct Hugo paths
  - [ ] Verify external image URLs (from raw.githubusercontent.com/minhhh/) are still live
  - [ ] Copy current site favicon if exists to `blog/static/img/favicon.png`
  - [ ] Create avatar image placeholder
  - [ ] Add `blog/static/` to Hugo config if needed (Hugo auto-detects `static/`)
  - [ ] Update README.md with static assets info

- **Dependencies**: task-03, task-04

---

### task-10: Build & verify site locally; fix rendering issues

- **Objective**: Run `hugo serve`, click through every page, and fix any rendering problems.

- **Checklist**:
  - [ ] Run `hugo serve` — no build errors
  - [ ] Check homepage: list of posts, pagination (10/page)
  - [ ] Check single post page: title, date, tags, body, TOC, reading time
  - [ ] Check code blocks have syntax highlighting
  - [ ] Check images render correctly
  - [ ] Check About and Projects pages
  - [ ] Check tag pages and category pages
  - [ ] Check RSS feed at `/feeds/all.atom.xml` (or default Hugo RSS)
  - [ ] Check Disqus comment section appears
  - [ ] Check dark mode toggle
  - [ ] Check mobile responsiveness
  - [ ] Check search widget works
  - [ ] Run `hugo --minify` — no errors
  - [ ] Update README.md with verification results

- **Dependencies**: task-04, task-05, task-06, task-07, task-09

---

### task-11: Clean up Pelican tooling from source branch, update README

- **Objective**: Remove old Pelican files from the `source` branch (the backup branch preserves them). Update README with the new Hugo workflow.

- **Checklist**:
  - [ ] Delete or move aside: `blog/Makefile` (Pelican), `blog/fabfile.py`, `blog/develop_server.sh`, `blog/pelicanconf.py`, `blog/publishconf.py`, `blog/pelican-themes/`
  - [ ] Remove root `Pipfile`, `Pipfile.lock`
  - [ ] Update root `Makefile` (already done in task-08)
  - [ ] Write `blog/README.md` explaining the Hugo workflow
  - [ ] Update root `README.md` with new tech stack and how-to-publish instructions

- **Dependencies**: task-08

---

## 4. Future Roadmap & Backlog

- [ ] **task-12**: Migrate Google Analytics from UA-50796592-2 to GA4 (generate new GA4 property, update params.toml)
- [ ] **task-13**: Add custom domain verification / CNAME if needed
- [ ] **task-14**: Add RSS link in sidebar or menu
- [ ] **task-15**: Custom homepage (not just post list) — Stack supports custom homepage
- [ ] **task-16**: Add table of contents to posts by default
- [ ] **task-17**: Add a sitemap for SEO

---

## 5. History / Archive

### task-01: Archive current Pelican setup as a backup branch and push

- **Objective**: Before any migration changes, snapshot the current `source` branch into a persistent backup branch so the old Pelican setup is never lost.

- **Checklist**:
  - [x] Ensure we are on the `source` branch with latest state
  - [x] Create a backup branch: `git branch archive/pelican-source`
  - [x] Push to origin: `git push origin archive/pelican-source`
  - [x] Set upstream: `git branch -u origin/archive/pelican-source archive/pelican-source`
  - [x] Verify backup exists: `git ls-remote --heads origin archive/pelican-source`
  - [x] Remain on `source` branch for the migration work

---

### task-02: Install Hugo and scaffold project with Stack theme

- **Objective**: Create a minimal Hugo site at `blog/` (replacing the Pelican structure) using the Stack theme via Hugo modules.

- **Checklist**:
  - [x] Install Hugo extended v0.163.0 via `go install -tags extended github.com/gohugoio/hugo@latest`
  - [x] Initialize Hugo module at `blog/`: `hugo mod init github.com/minhhh/minhhh.github.io`
  - [x] Add Stack theme as module dependency: `hugo mod get github.com/CaiJimmy/hugo-theme-stack/v4`
  - [x] Create `blog/config/_default/` with 6 config files (config, params, menu, markup, permalinks, module)
  - [x] Create `blog/content/` directory skeleton (`post/`, `page/`, `img/`)
  - [x] Create missing Stack icons (`brand-facebook.svg`, `code.svg`, `brand-linkedin.svg`, `email.svg`)
  - [x] Add social weights to fix alphabetical sort order in sidebar
  - [x] Create search & archives layout pages
  - [x] Verify: `hugo serve` starts and builds without errors
  - [x] Update README.md with Hugo run & build instructions

---

### task-03: Write Pelican-to-Hugo conversion script

- **Objective**: Create a Python script at `scripts/convert_pelican_to_hugo.py` that reads Pelican-format `.md` files and writes Hugo-compatible `.md` files (TOML frontmatter wrapped in `+++`).

- **Field mapping**:
  - `Title` → `title`, `Date` → `date` (ISO 8601), `Category` → `categories` (array), `Tags` → `tags` (array), `Summary` → `description`, `Slug` → `slug`

- **Body cleanup**: `{filename}/images/...` → `/img/...`, `[git:repo=X,file=Y]` → Markdown link

- **Checklist**:
  - [x] Create `scripts/convert_pelican_to_hugo.py`
  - [x] Script outputs to `blog/content/post/` (articles) or `blog/content/page/` (pages, as `index.md` in slug directories)
  - [x] Tested on all 65 files — 290 pages, 0 errors
  - [x] Update README.md with conversion script usage

---

### task-04: Convert all 62 articles (frontmatter + content cleanup)

- **Objective**: Batch-convert all 62 Pelican articles to Hugo format using the script from task-03.

- **Checklist**:
  - [x] Run conversion on all `blog/content/*.md` (65 files converted)
  - [x] Verify frontmatter correctness on 5+ random articles
  - [x] Verify `{filename}` and `[git:]` shortcodes cleaned from body
  - [x] Spot-check code blocks render with syntax highlighting (64 articles with code blocks, 0 errors)
  - [x] Check all categories and tags are preserved (6 categories, 65 tags — all match)
  - [x] Confirm article slug/URL matches old Pelican URL scheme (`/posts/{slug}/` — all 64 slugs verified)
  - [x] Commit converted files to `source` branch


