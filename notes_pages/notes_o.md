## `objdump`

### Disassemble a binary and show source

``` bash
objdump -d -S a.out | less           # Method one
objdump -DaflSx a.out                # Method two
```


## `openssl`

SSL and TLS utilities

### Test connections

```bash
openssl s_client -connect server.name.com:993 -crlf  # IMAP
openssl s_client -connect server.name.com:443 -crlf  # HTTPS
```

## OSX

### Screen shots

Change where screen shots are saved.

```bash
defaults write com.apple.screencapture location /Users/yourHomedirectory/some/path/captures
```