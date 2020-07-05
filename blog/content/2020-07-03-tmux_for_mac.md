Title: Setup Tmux with Vim for Mac
Date: 2020-07-03 00:00
Author: Ha.Minh
Category: Productivity
Tags: tmux, macos, vim

## Why Tmux

When working on the Mac Terminal, I used to create multiple tabs. Then I can switch quickly between tabs using `Ctrl + Shift + [` and  `Ctrl + Shift + ]`. While this works smoothly, one annoying problem is all the tabs will lose their content after reboot. So I've been looking for a solution that supports:

* Multiple tabs. Easily switch between tabs
* Able to restore sessions

From my search, it's quite obvious that `tmux` is the solution to my problem. Another candidate is `screen`, which I used for running some scripts on servers, but `screen` is pretty much a dead project now and its functions are far inferior to `tmux`.


## My tmux settings

Tmux configuration is stored inside `~/.tmux.conf`. On startup, `tmux` will pick up the content on this file and run it. We will put our customization code in this file.

First, we will remap reload key to `r` so that we can reload `tmux.conf` quickly.

```
# Set reload key to r
bind r source-file ~/.tmux.conf
```

Now, when we press `<prefix> r`, `tmux.conf` will be reloaded to reflect our new settings. The current `<prefix>` is still `Ctrl B`.

### Remap prefix key

Prefix key is one of the most commonly used keys, so it's super important to map it to a single key instead of `Ctrl B` or `Ctrl A` as some people might prefer.

On Mac, one popular solution is to change the prefix to `Capslock` key because it's rarely used and very well positioned. We have 2 approaches to do this.

* Approach 1: Remap `Capslock` to `Esc` and remap tmux `<prefix>` to `Esc`
    * Go to System Preferences => Keyboard => Modifier keys to remap `Capslock` to `Esc`
    * One annoying problem is now we have to press `Esc` or `Capslock` twice in Vim. This is quite unacceptable as I use Vim a lot

* Approach 2: Remap `Capslock` to `Home` and remap tmux `<prefix>` to `Home`
    * Normally you don't have `Home` in Mac keyboard, but fortunately there is a software called [Karabiner-Elements](https://github.com/tekezo/Karabiner-Elements) that allows you to completely customize your Mac keyboard.
    * After that, remap tmux prefix key to `Home`:

            set -g prefix Home
            bind-key Home send-prefix
            unbind C-b

    * I learnt this from [https://blog.guilhermegarnier.com/2017/12/increasing-productivity-in-tmux-with-a-single-prefix-key/](https://blog.guilhermegarnier.com/2017/12/increasing-productivity-in-tmux-with-a-single-prefix-key/)

### Fast window switching

Windows in `tmux` are the same concept as tabs in Terminal. I want to be able to switch between windows quickly without having to lift up all fingers.

Fortunately, there's an easy way to do this by mapping `next-window` and `previous-window` commands to `Shift Right` and `Shift Left`

```
# Shift arrow to switch windows
bind-key -r -T root         S-Left            previous-window
bind-key -r -T root         S-Right           next-window
```

You just have to hold Shift and press Left or Right arrows accordingly, which makes switching very fast.

Next, we also want to be able to move a window to the left and right. We'll do this by mapping `<prefix> n` and `<prefix> p` to swapping a window with the one of the left or right

```
# Prefix n/p to move window to the left or right
bind-key -r -T prefix n { swap-window -t +1; next-window }
bind-key -r -T prefix p { swap-window -t -1; previous-window }
```

In effect, you will press `Capslock n` or `Capslock p`. However, unlike `Shift Left` key combination, you cannot hold `Capslock`. Instead, you will have to lift all your fingers and press 2 keys `Capslock` and `n` at the same time again. This is not a big problem since I'll don't usually move windows around a lot.

### Restore Tmux and Vim sessions

When it comes to restoring `tmux` environment after system restart, the best solution is no other than [tmux-resurrect](https://github.com/tmux-plugins/tmux-resurrect). The installation instruction in their website is rather easy to follow.

After installing `tmux-resurrect`, we can use `<prefix> Ctrl s` to save, and `<prefix> Ctrl r` to restore tmux sessions.

Next and equally important, we also need a way to restore Vim session. I found [vim-obsession](https://github.com/tpope/vim-obsession) works well with `tmux-resurrect`.

The part for tmux-resurrect in my `.tmux.conf` looks like this:

```
# tmux-resurrect
set -g @resurrect-processes '"~sudo pmset" "~Vim"'
set -g @resurrect-capture-pane-contents 'on'
set -g @resurrect-strategy-vim 'session'
```

Pay attention to the line `set -g @resurrect-processes '"~sudo pmset" "~Vim"'`. There are a number of default commands such as `vi vim nvim emacs man less more tail top htop irssi weechat mutt` that `tmux-resurrect` will automatically restore, but other commands outside of this list will not be restored automatically. So this line tells `tmux-resurrect` to restores extra commands if the command string match what is specified in the `@resurrect-processes` variable. In this case, since MacVim uses the command `Vim` and not `vim`, we have to specify `"~Vim"` so `tmux-resurrect` know that it should restore Vim window. Another command I use is `sudo pmset`, so I specify `"~sudo pmset"` here. For more details, read [https://github.com/tmux-plugins/tmux-resurrect/blob/master/docs/restoring_programs.md](https://github.com/tmux-plugins/tmux-resurrect/blob/master/docs/restoring_programs.md)

Finally, there are 2 problems when you restore tmux sessions. First, if you create temporary tmux session first, so that you can run the command `<prefix> Ctrl r` to restore previous sessions, you will have to kill the temporary session manually, which is annoying. Second, the restored windows will not have `automatic-rename` set to `on`, so their titles will not be updated automatically, which is equally annoying. To deal with these 2 problem, I use the following bash function:

```
mux() {
    tmux new -d -s delete-me && (tmux run-shell ~/.tmux/plugins/tmux-resurrect/scripts/restore.sh && tmux kill-session -t delete-me) &&\
    (for session_window in $(tmux list-windows -a -F '#{session_name}:#{window_index}'); do
        tmux set-window-option -t $session_window automatic-rename on
    done) &&\
    tmux attach || tmux attach
}
```

This function is modified from https://gist.github.com/rootulp/93f67511ae97c20c4d32b600a5ab6a8d. To use it, simply type `mux` in the terminal and it will restore previous session and reattach to it automatically. If there are multiple previous sessions, you can use `tmux a -t <name>` to attach to the session you want.

### Vim binding in copy mode

Similar to `screen`, `tmux` has a copy mode to let you scroll through the content of your window, and copy/paste the parts you like.

Below is the setting to make this easier

```
# Use vim bindings in copy mode too
set -g status-keys  vi    # in the status/command prompt
setw -g mode-keys vi

# Setup 'v' to begin selection as in Vim
bind-key -T copy-mode-vi v send-keys -X begin-selection
bind-key -T copy-mode-vi y send-keys -X copy-pipe-and-cancel "reattach-to-user-namespace pbcopy"
unbind -T copy-mode-vi Enter ; bind-key -T copy-mode-vi Enter send-keys -X copy-pipe-and-cancel "reattach-to-user-namespace pbcopy"
```

You can start the copy mode with `<prefix> [`.
Then you navigate the window content with Vim-mode keys `h j k l`. `v` to start selecting. `y` or `Enter` to copy.

### Customize Status bar

The default tmux status bar position is at the top, which is ideal for showing tab-like window titles. I want to maximize the space for showing window title, so I limit the left part and right part of the status bar to very basic information.

```
# Set Colors
set -g default-terminal "screen-256color"
setw -g window-status-style fg=colour254,bg=colour102
setw -g window-status-format '#I:#W '
setw -g window-status-current-style fg=colour254,bg=colour30,bright
setw -g window-status-current-format '#I:#W '

# Set status bar
set -g status-bg colour252
set -g status-fg black
set -g status-left-length 90
set -g status-right-length 60
set -g status-left "#[fg=green]#S "
set -g status-justify left
set -g status-right ' #[fg=green]%a %d %b %R'
```

The left part of status bar, specified by `status-left`, only shows session title. The right part shows current date and time. Other colors and background colors are customized based on personal preferences.

### Customize window title

For me, one important feature is a good window title, so that I can understand what's in a window just by glancing at the title. One format that works quite well for me has these features:

* Show full path of the current directory if possible. Replace home directory with `~` for brevity.
* Limit the length of the path to 20 characters so that the title is not too long
* But always try to show at least the full name of the current directory. This will deal with very long directory name that if truncated to 20 characters, will be hard to guess the full name.

The code to achieve these features is listed below. It uses `awk` because `awk` is best for one-liner kinds of programs.

```
# Set window title
set -g automatic-rename on
set -g automatic-rename-format "#(echo '#{pane_current_path}' | awk '{split($0, a, \"/\");basename=a[length(a)];cmd=\"pwd\"; cmd | getline homepath; close(cmd);baselength=length(basename);i=index($0,homepath);path=$0;if (i==1) { path=\"~\"substr(path,length(homepath)+1,length(path)); };maxlength=15; if (length(basename) > maxlength-3) { print \"../\"basename; } else if (length(path) > maxlength) {print \"..\"substr(path, length(path)-maxlength+3, length(path)) } else print path }') - #{pane_current_command}"
```

If you want to customize this code, you can change `maxlength=15` to whatever you like. If you want to customize further, then you need to get a bit more involved with `awk`

The result is pretty good as far as I'm concerned. Here are some examples:

* `~/work`: Shorter than 15 characters, so it shows full path
* `..rk/webarchive`: full path is `~/work/webarchive`, so it truncates to 13 characters and replaces the rest with `..`
* `../a-very-long-folder-name`: The folder name itself is longer than 15 characters, so it's kept in tact and then prefixed with `../`


## Conclusion

Those are my main points of customization of `tmux`. Granted there are other functions that can be customized such as pane splitting, pane switching, mouse mode, etc, but I don't use those functions much if at all in my every day activities.

My tmux settings can be found at https://github.com/minhhh/dotfiles/blob/master/tmux/.tmux.conf

