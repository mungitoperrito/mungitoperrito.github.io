## `diff`

### Show output side by side

``` bash
diff -y --width 60 hello.c hello.c~
```

## Disassemble a binary

### Disassemble a binary and show source

``` bash
objdump -d -S a.out | less
```

### List dynamically linked libraries

``` bash
ldd some_exe
```

### Show symbols in a binary and their line numbers

``` bash
nm -s libcommon.a -l
```

### Trace libraries

Trace the libraries, child processes, time stamps, and time diffs in a
binary.

``` bash
ltrace -S -tt -r -f ./a.out
```

## Display processes

### Display the process stack

``` bash
$pgrep -f program ; $sudocat/proc/<PROC ID>/stack
```

## Duolingo web site volume

Use dev-tools in the browser. Open the javascript console. Edit
`Howler.volume()`.

``` bash
# Get current volume level
Howler.volume();

# Change volume to 50%
Howler.volume(0.5);

# Mute volume
Howler.mute(true);
```
