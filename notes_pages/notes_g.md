## `gcc`

### Compile flags for different C versions

``` bash
-ansi, -std=c89, -std=c99
```

### Debug level

Compile with level 3 debug information that includes macros. Debug level
2 is the default.

``` bash
gcc -g3 source.c
```

### Generate assembly code

Generate assembly code, `asm.s`. The output is not linked.

``` bash
gcc -S source.c -o asm.s
```

### Libraries

- Compile with static libraries

    ``` bash
    gcc -static source.c
    ```

- Compile with dynamic libraries

    ``` bash
    gcc -dynamic source.c
    ```

### Linking

Compile without linking

``` bash
gcc -c source.c -o object.o
```

### Optimize the executable

Compile for optimized output. Level 0 is unoptimized output.

``` bash
gcc -O2 source.c
```

### PATH

- Print search PATH information

    ``` bash
    gcc -print-search-dirs hello.c -o hello
   ```

- Print linker search PATH

    ``` bash
    echo $LD_LIBRARY_PATH
    ```

### Profiling

Enable profiling

``` bash
gcc -a -g -c source.c -o object.o
```