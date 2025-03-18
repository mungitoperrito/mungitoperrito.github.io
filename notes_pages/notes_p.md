## `PATH`

### Print linker search PATH

``` bash
echo $LD_LIBRARY_PATH
```


## Penetration testing

### Attack strings

- `<script>alert("XSS");</script>`
- `"searchTerm"><img src="x.x" onerror="alert('XSS')" />`


## Perl

### Documentation

- Manual page for a function: `perldoc -f functionName`


### Match pattern

```
$string =~ /match/    # TRUE if a match
$string !~ /match/    # TRUE if not a match
```


## Permissions

### Add user to a group

```bash
sudo usermod -a -G someGroup someUser
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


## Processes

### Get open files used by a process

```bash
lsof -p <procId>
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
