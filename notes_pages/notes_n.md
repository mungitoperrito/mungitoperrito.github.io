##  Netcat `nc`

Send files over a network connection.

### Send log files securely

```bash
# Example one
 tail -f /var/log/some_log_file | nc remote_ip remote_port

# Example two
tail -f /home/user/.history | nc remote_ip remote_port

# Example three
tail -f /home/user/.bash_history | nc remote_ip remote_port
```


 ## `nm`

Show symbols in a binary and their line numbers

``` bash
nm -s libcommon.a -l
```