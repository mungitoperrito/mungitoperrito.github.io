## `w`

### Show who is logged in and what they are doing

```bash
w
```


## `wall`

Send a message to all users logged into a machine

```bash
wall "some text"
```


## `watch`

Watch command output repeatedly

- Highlight diffs: `watch -d command`
- Keep diffs: `watch -d --cumulative command`


## Web servers

- Test https connection: `openssl s_client -connect www.example.com:443`
- Test http connection: `telnet www.example.com 80`


## `where`

Get a file location

```bash
whereis fileName
```


## `who`

### Show who is logged in

```bash
who
```


## `whois`

### Domain lookup

Return WHOIS directory information

```bash
whois 8.8.8.8                 # Search by IP
whois someDomain.com          # Search by domain name
```


## Windows

### Get MAC address

```bash
ipconfig /all | find \I "physical"
```

### Run command as another user

- Admin user: `runas /user:administrator cmd.exe `
- Another domain: `runas /user:user@domain.microsoft.com "notepad someFile.txt"`

### Restart the network

```bash
ipconfig /release
ipconfig /renew
```

### Restart the machine

```bash
shutdown -r -t now
```

### Shortcuts

`Command.exe` with admin privileges

1. Right-click to create regular short cut.
1. Edit the command line: `runas /user:machine name\administrator cmd`

### Shutdown

```bash
shutdown -s -t 01
```

### Windows XP

- Disable last access writes: `FSUTIL behavior set disablelastaccess 1`  then reboot
- Disable 8.3 filename compatibility if no 16bit apps: `fsutil behavior set disable8dot3 1`


## WSL Windows Subsystem for Linux

### Current directory

Get the current directory relative to windows.

```bash
explorer.exe .
```

### Mount usb drive

```bash
sudo mkdir /mnt/e                # Once. Create a mount point
sudo mount -t drvfs e: /mnt/e    # Each time
```

### Turn off `bash` bell

1. `sudo vi /etc/inputrc`
1. Uncomment: `set bell-style none`

### Turn off `vim` bell

1. `vi ~/.vimrc`
1. Add: `set visualbell`