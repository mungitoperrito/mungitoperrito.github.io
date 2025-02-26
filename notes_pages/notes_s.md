## `sdiff`

Interactively compare and merge two files.

 `-w` controls the width of the line
 `-l` only shows the left hand file when the lines are the same
 `-s` only shows lines that are different

``` bash
sdiff -w Number -l file1 file2:
```


## `source`

### Reread config file

```bash
source ~/.bashrc
```

## `stderr`, `stout`, `stdin`

### Redirects

```bash
# Redirect stderr to stdout
cmd 2>&1

# Redirect stderr & stdout to file
cmd &> fileName

# Redirect stderr to stdout, and both to file
cmd > fileName 2>&1
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


## `svn`

### Check in a single file

```bash
svn commit -m "Some comments" master.cfg
```

### Check out a single file

```bash
svn co svn+ssh://svn/svn/branches/svn2git/buildbot --depth empty
cd buildbot
svn up master.cfg
```