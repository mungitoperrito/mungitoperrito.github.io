## Backtraces

### Get a backtrace for a segmentation fault on linux

``` bash
catchsegv  someBinaryThatSegFaults
```

## Bash scripting

### Create an infinite loop

```bash
while :
```

### Initialize an array

```bash
letter_combos=({a..z}{a..z})
```

### Evaluate an expresion

```bash
echo $(( 3 + 4 ))
```

### Variable matching

```bash
# Keep everything up to first .
varName=${ varName%%.* }

# Drop everything up to last /
varName=${0##*/}
```

bash: read a file into a script ( source file in script )  -> . fileName
bash: read a file to variable -> varName=$(< /proc/fileName)
bash: redirect stderr to stdout -> cmd 2>&1
bash: redirect stderr & stdout to file -> cmd &> fileName
bash: redirect stderr to stdout and both to file -> cmd > fileName 2>&1
bash: reread .bashrc -> source ~/.bashrc
bash: rename files -> for fn in `ls` ; do new="$( echo $fn | cut -c 5- )" ; mv $fn $new ; done
bash: rename files -> for d in $(ls) ; do  mv "${d}" "${d/..20/..xxx..20}" ; done
bash: reset screen after binary cat -> reset
bash: reset screen after binary cat -> echo <ctrl><v> <esc><c> <enter>
bash: select, copy & rename multiple files -> for i in aaa?[XY]?? ; do cp $i bbb${i#aaa} ; done
bash: variables -> current process id num -> $$
bash: variables -> last return value -> $?
bash: variables -> list of execution vars -> $-
bash: variables -> list of shell args -> $*
bash: variables -> list shell variables -> printenv ( export for currently exported variables )
bash: variables -> number of arguments -> $#
bash: variables, enable warnings -> set -u
bash: variables, disable warnings -> set +u
bash: while loop on command line -> while [ 1 ] ; do someStuff ; done
bash: work in a subshell, switch dir, do stuff, come back to orig dir: ( cd /tmp && doSomething )


## `bc`

### Convert bases

```bash
echo 'obase=16; ibase=10; 255' | bc
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