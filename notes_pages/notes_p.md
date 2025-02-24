## `PATH`

### Print linker search PATH

``` bash
echo $LD_LIBRARY_PATH
```

## `pgrep`

### Display the process stack

``` bash
$pgrep -f program ; $sudocat/proc/<PROC ID>/stack
```

## Proc file system

Display open file descriptors

``` bash
cat /proc/self
```