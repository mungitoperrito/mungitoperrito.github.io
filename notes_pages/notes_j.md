## `jvm`

For garbage collection, heap stats: `-XX:+PrintHeapAtGC`

For garbage collection tenuring stats: `-XX:+PrintTenuringDistribution`
The memory size should decline quickly across ages.

For the memory footprint use: `-verbosegc`
Check the values reported

```bash
[Full GC $before->$after($total), $time secs]
```