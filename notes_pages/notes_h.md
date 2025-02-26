## `hexdump`

### Search a file using hex values

```bash
hexdump -C screenshot.png | grep "ff 00"
```

### Print the first n characters of a file in human readable form

```bash
hexdump -C -n 20 filename
```

### Format the first 50 bytes of a file as 64 bit integers (in hex)

```bash
hexdump -n 50 -e '"0x%08x "' screenshot.png
```

### Search RAM in clear text

```bash
sudo hexdump -e '90/1 "%_p" "\n"' /dev/mem | less
```
