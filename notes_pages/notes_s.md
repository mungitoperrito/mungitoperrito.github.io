## Safari

### Turn on debug mode

1. Close safari
1. In terminal, enter:

   ```bash
   defaults write com.apple.Safari IncludeDebugMenu 1
   ```


## SAMBA  (SMB) shares

Mount Windows shared drives on Linux

### Find shares

```bash
# Method one
smbtree

# Method two
findsmb
```

### List shares

```bash
smbclient -L windowsBox
```

### Mount shares

`mount.cfs` is newer than `smb`.

```bash
# Example one
samba: mount -t smbfs -o fmask=666,username=dave //fromWindowsMachine/NameOfShare /local/mount/path/

# Example two
samba: mount -t smbfs -o username=WindowsUserName //192.168.1.18/NameOfShare /local/mount/path/   # Not on Fedora

# Example three
samba: mount -t cifs -o user=WindowsUserName,domain=domain_name.com //192.168.32.128/NameOfShare /local/mount/path/
```


## `screen`

### Run a persistent remote process

You can close the terminal locally and restart it later

```bash
screen
run_some_command
```

Disconnect:

- ctrl+a ctrl+d
- <logout>

Reconnect:

```bash
screen -r
```

## `sdiff`

Interactively compare and merge two files.

 `-w` controls the width of the line
 `-l` only shows the left hand file when the lines are the same
 `-s` only shows lines that are different

``` bash
sdiff -w Number -l file1 file2:
```


## Secure log files

Send log files securely over IP

```bash
# Example one
 tail -f /var/log/some_log_file | nc remote_ip remote_port

# Example two
tail -f /home/user/.history | nc remote_ip remote_port

# Example three
tail -f /home/user/.bash_history | nc remote_ip remote_port
```


## Send messages

### Send a message to all users logged into a machine

```bash
wall "some text"
```

### Send a file to another console

```bash
cat some_file > /dev/pts/2
```

### Send a message to another console

```bash
echo "message" > /dev/pts/2
```


## SMTP server

Mail servers

### Test connection

1. Connect to the server: `telnet somemailserver.domain 25`
1. After the banner type: `HELO yourdomain`
1. Check other commands: MAIL, RCPT, DATA, QUIT


## `source`

### Reread config file

```bash
source ~/.bashrc
```


## `ssh`

Secure shell

### Configure direct root access

1. Edit: `vi /etc/ssh/sshd_config`
1. Change: `'#PermitRootLogin yes'` to `'PermitRootLogin no'`

### Connect to remote without login

1. Create key pair on local machine, `a@A`: ssh-keygen -t rsa
1. Create a remote directory: `ssh b@B mkdir -p .ssh`
1. Copy the public key to remote cat:
   `.ssh/id_rsa.pub | ssh b@B 'cat >> .ssh/authorized_keys'`

### Create an ssh tunnel

Tunnel from  port 80 on the local box to port 443 on the remote box.

```bash
ssh -g -L 80:remote.machine:443 user@remote.machine
```


## SSL

Server certificates

### Read a certificate

```bash
openssl x509 -in hostedcc.crt -text
```

### Test connections

```bash
openssl s_client -connect server.name.com:993 -crlf  # IMAP
openssl s_client -connect server.name.com:443 -crlf  # HTTPS
```


## `stack`

Haskell package manager and environment. If `ghc`and the other Haskell tools are
installed under `stack` the command line calls are different.

### Configuration

The install bundle may not install a package that has valid upstream sources. To
update the global config source:

```bash
stack upgrade --force-download
```

### Utilities

**`stack`**

- Version: `stack --version`

**`ghc`**

- Haskell compiler: `stack ghc`
- Version:: `stack ghc -- --version`

**`ghci`**
- repl: `stack ghci`
- repl: `stack repl`
- Quit repl: `:quit`


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


## `strace`

### Save `strace` output from a command

```bash
strace -o output.file <command>
```

### Summarize system calls

```bash
strace -c -p PID
```

### Trace execution in a running process.

```bash
starce -p PID
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

### Connect to a remote repo

```bash
svn co -N  svn+ssh://username@svn.some_company.com/svn/trunk
```


## System information

Gather system information

### Read the `proc` filesystem

- CPU: `/proc/cpuinfo
- Memory usage: `/proc/meminfo
- OS version: `proc/version`
- Partition tables: `/proc/partions`
- Swap system: `/proc/swaps`

### Top 10 processes, memory

```bash
ps aux | sort -n -k4 | cut -c -95 | tail -10
```

### Top 10 processes, cpu

```bash
ps aux | sort -n -k3 | cut -c -95 | tail -10
```
