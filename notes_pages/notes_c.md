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

## Convert bases

```bash
echo 'obase=16; ibase=10; 255' | bc
```