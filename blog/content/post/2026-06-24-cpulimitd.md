+++
title = "cpulimitd"
date = "2026-06-24T00:00:00+07:00"
author = "Ha.Minh"
description = "A thin cpulimit wrapper daemon that throttles resource-intensive processes by name."
slug = "cpulimitd"
categories = ["Programming"]
tags = ["cpulimit", "python", "cli", "macos", "tooling"]
+++

Recently Firefox, Chrome, and Edge use too much CPU and it's annoying that my fan is going full speed for an extended period. After looking around I found that `cpulimit` exists on macOS and Linux to clamp a process to a given CPU percentage, but it works per-PID and doesn't track respawns.

So naturally I wrote `cpulimitd` to wrap it. Give it a TOML config:

```toml
[processes."firefox"]
limit = 40
include-children = true
```

It scans running processes every N seconds, matches names against patterns, spawns `cpulimit` for each PID, and re-limits if a process dies and respawns. Config reloads every cycle — no restart needed.

It has two commands:
- `cpulimitd` — daemon mode. Runs until killed.
- `cpulimitd list 10` — shows top N CPU processes. The `NAME` column is what you put in config.

Code: [github.com/minhhh/cpulimitd](https://github.com/minhhh/cpulimitd)
