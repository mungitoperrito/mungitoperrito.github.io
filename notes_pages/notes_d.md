## `dd`

### Create image of floppy

```bash
dd if=/dev/fd of=floppyImage
```


## Device files

- Stream random numbers: `/dev/random`
- Stream zeros: `/dev/zero`


## `diff`

### Show output side by side

``` bash
diff -y --width 60 hello.c hello.c~
```


## Disassemble a binary

See also binary analysis.

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


## Docker

### Clean up

1. Remove old containers

   ```bash
   docker rm $(docker ps -qa --no-trunc --filter "status=exited")
   ```

1. Remove orphaned images

   ```bash
   docker image ls --all | wc -l         # Count images
   docker rmi $(docker images --filter "dangling=true" -q --no-trunc)
   docker image ls --all | wc -l         # Count images
   ```

### Get shell stdin, stdio from log file

```bash
docker logs CONTID
```

### List all containers, running and stopped

```bash
docker ps --all
```

### Open a shell inside a container

```bash
docker exec -it CONTID /bin/bash
```

### Remove a container

```bash
docker rm CONTID
```

### Run a single command in a container and exit

```bash
docker exec CONTID ls -l
```

### Run multiple commands in a container and exit

```bash
docker exec CONTID sh -c "cd X ; ls -l"
```

### Run a python script

```bash
docker run -it --rm --name my-script -v "$PWD":/usr/src/myapp -w /usr/src/myapp python:3 python the-script.py
```

### Start a container

```bash
docker start CONTID
```

### Stop a container

```bash
docker stop CONTID
```


## `dtrace`

### Dynamically trace libraries

```bash
dtrace FILENAME`
```


## `du`

Disk usage

### Exclude directories

Gather top level usage. Go down one directory. Skip `mnt`, `proc`, `sys`, `run`.

```bash
du -d1 -h --exclude={./mnt,proc,sys,run}
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
