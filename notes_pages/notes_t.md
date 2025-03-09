## `tc`

Local network traffic controller

### Add qdisc to slow traffic

```bash
tc qdisc add dev eth0 root netem delay 100ms 10ms
```

### Change qdisc to stop traffic

```bash
tc qdisc change dev eth0 root netem loss 99%
```

### Delete qdisc to restore eth0

```bash
tc qdisc delete dev eth0 root netem
```


## `tee`

### Split process outputs

Send `ls` output to screen and to someFile

```bash
ls -aS | tee -a someFile
```


## `telnet`

Plain text connection utility


### Test RDP

1. Connect to RDP on `10.0.0.1`: `telnet 10.0.0.1 3389`
1. Get telnet command prompt: `<ctrl><]>`
1. Disconnect: `close`


## Terminal

### Reset the screen

Reset if the display is confused after runing `cat someBinary`

```bash
# method one
reset

# Method two
echo <ctrl><v> <esc><c> <enter>
```

## `time`

Time execution time for a process.

### Windows equivalent

```bash
powershell Measure-Command {<command>}
```

## Time zones

### Get zone info

```bash
tzselect
```

### Get the current time

```bash
TZ='Place/locale' date      # Europe/London   America/Mexico_City  Pacific/Auckland
```


## `top`

Monitor system and running processes

### Track a process over time

```bash
for i in `seq 1 10` ; do top -b -n 1 | grep proc_name ; echo ; sleep 1 ; done
```


## `touch`

### Change file creation date

```bash
touch -t 200612100606.06 /tmp/someFile
```


## Trace system events

### Library calls

```bash
ltrace -p process-id
```

### Summarize system calls

```bash
strace -c -p process-id
```

### System calls

```bash
strace -p process-id
```


## `tree`

Tree version of `ls`

### Show all

```bash
tree
```

### Show directories only

```bash
tree -d
```
