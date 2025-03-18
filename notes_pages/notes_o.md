## `objdump`

Disassemble a binary and show source

``` bash
objdump -d -S a.out | less
```

## `openssl`

SSL and TLS utilities

### Test connections

```bash
openssl s_client -connect server.name.com:993 -crlf  # IMAP
openssl s_client -connect server.name.com:443 -crlf  # HTTPS
```