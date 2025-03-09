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


## `ps`

Process information

### Top 10 processes, memory

```bash
ps aux | sort -n -k4 | cut -c -95 | tail -10
```

### Top 10 processes, cpu

```bash
ps aux | sort -n -k3 | cut -c -95 | tail -10
```
