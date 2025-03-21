## `cat`

### Add line numbers to the output

```bash
cat –n someFile.c
```


## `catchsegv`

### Get a backtrace for a segmentation fault on linux

``` bash
catchsegv  someBinaryThatSegFaults
```


## Change file creation date

```bash
touch -t 200612100606.06 /tmp/someFile
```


## Clean machines

### Cache - set clearing priority

The default is 100.

```bash
echo 1000 >  /proc/sys/vm/vfs_cache_pressure
```
### Cache - clear page cache

Caution: This *may* be problematic for running processes

```bash
sync
echo 1 > /proc/sys/vm/drop_caches
```

## Clear `dentries`, `inodes`

```bash
sync
echo 2 > /proc/sys/vm/drop_caches
```

### Docker Clean UP

1. Remove old containers

   ```bash
   docker rm $(docker ps -qa --no-trunc --filter "status=exited")
   ```

1. Remove orphaned images

   ```bash
   docker image ls --all | wc -l         # Count images before
   docker rmi $(docker images --filter "dangling=true" -q --no-trunc)
   docker image ls --all | wc -l         # Count images after
   ```

### Find largest files

```bash
du -a /var | sort -n -r | head -n 10
```


## Compressed files

See `zip` and `tar` files.


## Convert bases

```bash
echo 'obase=16; ibase=10; 255' | bc
```


## Convert case

```bash
echo 'SoMe StRiNg' | tr '[:lower:]' '[:upper:]'
```


## Crontab

### Display `crontab`

```bash
crontab -l
```

### Edit `crontab`

```bash
crontab -e
```

### Find and remove old Docker images

- 0 minutes
- 23 hours
- Any day
- Any month
- On Sunday (0)

```bash
00 23 * * 0 docker system prune -f && docker system prune -f
```

### Find and remove temporary files

- 18 minutes
- 3 hours
- Any day
- Any month
- Any day of the week

```bash
18 3 * * * find /tmp \( -name "tmp*" -or -name "pytest*" \) -mtime +8 -exec rm -rf {} \;
```


## `curl`

### Dump a dodgy website safely

```bash
curl -s http://someWebSite.com | hexdump -C|less
```


## `cygwin`

### Proxies

Configure proxy:

```bash
export http_proxy="http://proxy.vmware.com:3128"
export ftp_proxy="http://proxy.vmware.com:3128"
```

Use `wget`:

```bash
wget --proxy-user "Wwall\JohnDoe" --proxy-passwd "SomePWD" http://someSite.net/someFile
```

### Show Windows PATH

```bash
cypath -m /path/to/some/file
```