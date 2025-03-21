## Mail servers

`SMTP`, `IMAP` servers

### Test connection

1. Connect to the server: `telnet somemailserver.domain 25`
1. After the banner type: `HELO yourdomain`
1. Check other commands: `MAIL`, `RCPT`, `DATA`
1. Exit: `QUIT`


## Math

### Convert bases

```bash
echo 'obase=16; ibase=10; 255' | bc
```

### Evaluate an expression

```bash
echo $(( 3 + 4 ))
```


## Memory

### Get memory usage information

- Show in mebibytes: `m`
- Show total usage: `t`

```bash
free -m -t
```

### Get slab memory usage

```bash
slabtop --once
```

### Search RAM in clear text

```bash
sudo hexdump -e '90/1 "%_p" "\n"' /dev/mem | less
```


## Monitoring

See memory above.

### Display the process stack

``` bash
$pgrep -f program ; $sudocat/proc/<PROC ID>/stack
```

### Get CPU loads, disk activity

```bash
iostat -x
```

### Get CPU stats

```bash
mpstat
```

### Get CPU stats for multiple CPUs

```bash
mpstat -P ALL
```

### Get memory usage for a process.

```bash
pmap -X PID
```

### Get open files

```bash
lsof                            # All open files
lsof -p <procId>                # Files used by procId
```

### Get socket level statistics.

```bash
ss
```

### Get system information repeatedly: `vmstat`

- Wide format: `-w`
- One header row: `-n`
- Active and inactive memory: `-a`
- Delay two seconds
- Repeat three times

```bash
 vmstat  -w -n -a 2 3
 ```

### Get system information repeatedly: `dstat`

- Memory: `-m`
- Disk: `-d`
- CPU: `-c`

```bash
dstat -mdc
```

### Get threads per user

```bash
for USR in $(ps aux | awk '{print substr($1, 1, length($1)-1)}' | sort -u) ; do echo -n "${USR}  " ; ps -efT |grep "^${USR}" |wc -l ; done
```

### Get total number of process threads

```bash
ps -eo nlwp | tail -n +2 | awk '{ num_threads += $1 } END { print num_threads }'
```

### List currently mounted filesystems

```bash
cat /etc/mtab
```

### Watch command output

- Highlight diffs: `watch -d command`
- Keep diffs: `watch -d --cumulative command`


## `mpstat`

### Get CPU stats

- One CPU: `mpstat`
- Multiple CPUs: `mpstat -P ALL`