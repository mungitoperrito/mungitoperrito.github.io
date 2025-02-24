## Linked libraries

List dynamically linked libraries

``` bash
ldd some_exe
```

## `ltrace`

Trace libraries, child processes, time stamps, and time diffs in a
binary.

``` bash
ltrace -S -tt -r -f ./a.out
```

