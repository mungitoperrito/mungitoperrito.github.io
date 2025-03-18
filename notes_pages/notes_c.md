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


### Compressed files

See `zip` and `tar` files.


### Uncompress .bz2 tarball

``` bash
tar -xjvf file.tar.bz2
```


## Convert bases

```bash
echo 'obase=16; ibase=10; 255' | bc
```


## Convert case

```bash
echo 'SoMe StRiNg' | tr '[:lower:]' '[:upper:]'
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