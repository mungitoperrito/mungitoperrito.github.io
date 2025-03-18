## Mail servers

SMTP, IMAP servers

### Test connection

1. Connect to the server: `telnet somemailserver.domain 25`
1. After the banner type: `HELO yourdomain`
1. Check other commands: MAIL, RCPT, DATA, QUIT


## Math

### Convert bases

```bash
echo 'obase=16; ibase=10; 255' | bc
```

### Evaluate an expresion

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

### Get open files used by a process

```bash
lsof -p <procId>
```

### List currently mounted filesystems

```bash
cat /etc/mtab
```

### Watch command output

- Highlight diffs: `watch -d command`
- Keep diffs: `watch -d --cumulative command`