## Backtraces

### Get a backtrace for a segmentation fault on linux

``` bash
catchsegv  someBinaryThatSegFaults
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

Enable: `set -x`
Disable: `set +x`

### Warnings

Enable: `set -u`
Disable: `set +u`


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


## `.bashrc`

### Reread config file

```bash
source ~/.bashrc
```


## `bc`

### Convert bases

```bash
echo 'obase=16; ibase=10; 255' | bc
```


## Build C programs

### Build and install a binary from source

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
