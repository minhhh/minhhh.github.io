+++
title = "Initial thoughts on my experience with Antigravity CLI"
date = "2026-06-22T00:00:00+07:00"
author = "Ha.Minh"
description = "Some initial thoughts about my experience with using the Antigravity CLI, comparing it to the older Gemini CLI"
slug = "initial-thoughts-on-antigravity-cli"
categories = ["Programming"]
tags = ["antigravity", "cli", "gemini-cli", "developer-experience", "AI", "productivity"]
+++
I recently transitioned to using the new **Antigravity CLI** (`agy`), which has officially replaced the older **Gemini CLI** as the main terminal interface for agentic coding workflows. Here are some of my initial thoughts on my experience using it.

## The Good Bits

* **Performance**: It's generally faster and much more responsive than the old Gemini CLI. Command execution and responses feel near-instant.
* **Context breakdown**: The `/context` command displays a clean breakdown of loaded files and symbols, making it easy to track what is currently in the agent's context window.
* **Conversation resets**: The `/clear` (or `/new`) command resets the conversation history without requiring you to quit and restart the CLI session.
* **Sub-agents**: Spawning sub-agents to handle background research or run A/B tests (like comparing two different implementations) is extremely easy and doesn't interrupt the main thread.


## Context Bloat & The Missing `/compress` Command

In sequential coding workflows, context windows bloat rapidly as tool execution outputs and file reads are appended to history, causing latency and token waste. A big multi-file refactoring session can run out of tokens quickly because of the lack of a compression command. The older Gemini CLI resolved this with the `/compress` command, which replaced the chat context with a high-level summary of the conversation. Similar developer interfaces (like OpenCode with `/compact`) implement a matching pattern to keep reasoning loops tight.

Another problem is that `agy` can often mess up the application of moderate-to-large diffs; it sometimes removes more lines than expected, or adds extra lines that result in syntax errors.

### The Current Workaround in `agy`

Currently, `agy` supports `/rewind` (to undo the session to a previous checkpoint) but has no native `/compact` or `/compress` command. The current workaround requires manually managing state:

1. Keeping a tracking file like `todo.md`.
2. Having the agent update it after each task.
3. Clearing the session history via `/new`.
4. Reading `todo.md` in the new session to resume.

This workaround works, but having to manually cycle through session restarts feels unnecessarily clunky. Context hygiene should be a native feature of the harness.
