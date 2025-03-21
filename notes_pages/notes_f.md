## Files


### Check filetype

```bash
file FILENAME
```

### Get a file location

```bash
whereis fileName
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

### Rename files

**Change to lower case**

```bash
for i in $(ls) ; do  mv $i $(echo $i | tr [:upper:] [:lower:]) ; done
```

**Change .#. to .0#.**

```bash
for i in $(seq 1 5) ; do rename .${i}. .0${i}. *.jpg ; done
```

**Match pattern**

```bash
for fn in $(ls) ; do  mv "${fn}" "${fn/patternToMatch/replacementPattern}" ; done
```

**Select, copy & rename multiple files**

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

**Shorten file name**

```bash
for fn in `ls` ; do new="$( echo $fn | cut -c 5- )" ; mv $fn $new ; done
```

**Use `rename` script**

```bash
rename ".."  "..1962-00-00.." *.jpg
```


## File systems

### Force buffers to write to disk

```bash
sync
```

### List currently mounted filesystems

```bash
cat /etc/mtab
```

### List locked files

```bash
ls /var/lock/*
```

### Toggle swap

```bash
swapon                         # Turn on
swapoff                        # Turn off
```

## Floppy disks

### Create image file from floppy

```bash
dd if=/dev/fd of=floppyImage
```


## Forensics

### Dump a dodgy website safely

```bash
curl -s http://someWebSite.com | hexdump -C|less
```


## `free`

Get memory information

```bash
free
```