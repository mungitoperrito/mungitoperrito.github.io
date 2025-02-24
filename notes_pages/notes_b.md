## Backtraces

### Get a backtrace for a segmentation fault on linux

``` bash
catchsegv  someBinaryThatSegFaults
```

## Build C programs

### Build and install a binary from source

``` bash
tar zxvf source.tgz
cd source
mkdir build
cd build
../configure
make
make check
make install
```
​