## `sdiff`

Interactively compare and merge two files.

 `-w` controls the width of the line
 `-l` only shows the left hand file when the lines are the same
 `-s` only shows lines that are different

``` bash
sdiff -w Number -l file1 file2:
```

## `strings`

Show all the strings and file locations in a binary file.

``` bash
strings -a -f someExe
```

## `strip`

Remove unnecessary bytes from an executable.

``` bash
strip someExe
```
