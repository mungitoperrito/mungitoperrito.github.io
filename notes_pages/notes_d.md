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