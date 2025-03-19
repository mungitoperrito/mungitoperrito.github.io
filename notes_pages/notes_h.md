## Haskell

If `ghc`and the other Haskell tools are installed under `stack`, the command
line calls are different.

### Configuration

The install bundle may not install a package that has valid upstream sources. To
update the global config source:

```bash
stack upgrade --force-download
```

### `ghc`

Haskell compiler

```bash
stack ghc         # If installed via stack
ghc               # If installed standalone
```


### `ghci`

Haskell interactive shell.

```bash
stack ghci         # If installed via stack
ghci               # If installed standalone
```

### `stack`

Get version.

- `stack`: `stack --version`             # `stack` version
- `stack`: `stack ghc -- --version`      # `ghc`version
- `stack`: `stack ghci`                  # `ghci`version in welcome message


## `hexdump`

### Search a file using hex values

```bash
hexdump -C screenshot.png | grep "ff 00"
```

### Print the first n characters of a file in human readable form

```bash
hexdump -C -n 20 filename
```

### Format the first 50 bytes of a file as 64 bit integers (in hex)

```bash
hexdump -n 50 -e '"0x%08x "' screenshot.png
```

### Search RAM in clear text

```bash
sudo hexdump -e '90/1 "%_p" "\n"' /dev/mem | less
```



## `history`

Set these environment variables in `~/.bashrc` or `~/.zshrc`.

### `bash`

- Last 10 commands: `history | tail `

### Environment variables

```bash
shopt -s histappend                  # Make bash append to disk
export HISTCONTROL=ignoreboth        # ignore dups & initial space lines
export HISTIGNORE="pwd:ls:ls -ltr:ll:exit:history"  # Ignore these commands
export HISTSIZE=10000                          # Number of lines to keep
export HISTFILESIZE=100000                     # Max file size
export HISTTIMEFORMAT="%h %d %H:%M:%S "        # Format times
export PROMPT_COMMAND="history -a"             # Save across sessions
export SAVEHIST=$HISTSIZE
```

### `zsh`

- Get all of history: `history 1`
- Last 10 commands: `history 1 | tail `


## `host`

Map a hostname to an IP address

```bash
host someDomain
host -v someDomain                # Verbose mode
```


## `hostname`

Get the machine name.

```bash
hostname                 # Machine name only
hostname -i              # IP address
hostname -d              # Domain name
```