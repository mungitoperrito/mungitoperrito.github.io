## `ldd`

List dynamically linked libraries

``` bash
ldd some_exe
```


## Linked libraries

### List dynamically linked libraries

``` bash
ldd some_exe
```


## Linux

### Boot in single user mode

Enter `single` at boot prompt.


## `ltrace`

Trace library calls

### Trace process library calls

- Trace libraries
- Child processes
- Time stamps
- Time diffs

``` bash
ltrace -S -tt -r -f  some_binary_file
```

### Trace system library calls

```bash
ltrace -p PID
```


## `lsof`

### Get open files

```bash
lsof
```

### Get open files used by a process

```bash
lsof -p <procId>
```

