## Backtraces

### Get a backtrace for a segmentation fault on linux

``` bash
catchsegv  someBinaryThatSegFaults
```


## `base64`

### Encode

```bash
echo "hello world!" | base64
```

### Decode

```bash
echo aGVsbG8gd29ybGQh | base64 -d
```


## `.bashrc`

Config file settings. See [`aliases`](./notes_a.md#alias)

### Environment settings

```bash
export EDITOR=vi
export LANG=C
export LC_COLLATE=C                  # Ordering for sort and ls
export PS1="\u@\h \w> "              # Main prompt
export PS2=" ..> "                   # Additional prompt lines
```

### History

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

### Reread `.bashrc`

```bash
source ~/.bashrc
```


## Bash environment

### List shell variables

```bash
# Method one
printenv

# Method two
env

# Method three
export -p
```

### Show commands

- Enable: `set -x`
- Disable: `set +x`

### Warnings

- Enable: `set -u`
- Disable: `set +u`


## Bash scripting

### Create an infinite loop

```bash
# Method one
while [ 1 ] ; do someStuff ; done

# Method two
while : ; do someStuff ; done
```

### Evaluate an expresion

```bash
echo $(( 3 + 4 ))
```

### Initialize an array

```bash
letter_combos=({a..z}{a..z})
```

### Multiple files

Use pattern matching to select, copy & rename multiple files.

- `?` matches one character
- `[XYZ]` matches X or Y or Z
- `${var#pattern}` deletes the shortest length of `pattern` from the start of `var`
- `${var##pattern}` deletes the longest length of `pattern` from the start of `var`

The `for` section expands to file names. The copy section changes the
beginning of the file names.

```bash
# Change PXL_20241212_03.jpg to prefix.._20241212_03.jpg..postfix
for fn in P?[LM]* ; do cp $fn prefix..${fn#PXL_}..postfix ; done
```

### Read a file into a script

Source (execute) the file in a script

```bash
. fileName
```

### Read a file into a variable

```bash
varName=$(< /proc/fileName)
```

### Redirect stderr, stout, stdin

```bash
# Redirect stderr to stdout
cmd 2>&1

# Redirect stderr & stdout to file
cmd &> fileName

# Redirect stderr to stdout, and both to file
cmd > fileName 2>&1
```

### Special variables

- Current process id: `$$`
- Last return value: `$?`
- List the execution variables: `$-`
- List the shell arguments: `$*`
- Return the number of arguments: `$#`

```bash
echo $?
```

### Variable matching

```bash
# Keep everything up to first .
varName=${ varName%%.* }

# Drop everything up to last /
varName=${0##*/}
```


## `bc`

### Convert bases

```bash
echo 'obase=16; ibase=10; 255' | bc
```


## Binary analysis

- Check filetype: `file FILENAME`
- Debug binary execution: `dbg FILENAME`
- Disassemble: `readelf -a FILENAME`
- Disassemble an object file: `objdump -DaflSx FILENAME`
- Dynamic trace libs: `dtrace FILENAME`
- Get a hexdump: `od -Ax -tx1z -v FILENAME`
- Get object symbols: `nm FILENAME`
- Show shared libs: `lld FILENAME`
- Show strings: `strings FILENAME`


## BIOS

### Common memory locations

- HD BIOS usually at 0xC8000
- System BIOS usually at 0xFFFF0
- Video BIOS usually at 0xC000

### Startup order

1. `BIOS`
1. `start_kernel()`
1. `init()`
1. `[load kernel modules: kexec, ksplice]`


## Brew

Third party, community OSX package manager.

### Install a package

```bash
brew install somePackage
```

### Turn off analytics

```bash
brew analytics off
```


## Browsers

### Export search history

The history database file PATH is like one of these (Chrome):

```
~/Library/Application Support/Google/Chrome/Default\History

%LocalAppData%\Google\Chrome\User Data\Default\History

C:\Users\USERNAME\AppData\Local\Google\Chrome\User Data\Default
```

Extract the URLS to a text file.

``` bash
sqlite3 History "SELECT datetime(last_visit_time/1000000-11644473600,'unixepoch'), url FROM  urls ORDER BY last_visit_time desc" > history_urls.txt
```

## Build C programs

### Build and install a binary from source

As steps:

``` bash
tar zxvf source.tgz
cd source
mkdir build
cd build
../configure
make
make check
make install
```

As one line:

```bash
tar zxvf source.tgz ; cd source ; mkdir build ; cd build ; ../configure ; make ; make check ; make install
```