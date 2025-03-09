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
