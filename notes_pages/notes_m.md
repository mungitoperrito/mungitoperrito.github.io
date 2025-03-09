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

```bash
free
```

### Search RAM in clear text

```bash
sudo hexdump -e '90/1 "%_p" "\n"' /dev/mem | less
```
