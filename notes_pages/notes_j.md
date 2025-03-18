## Jira

### Search for inactive Users who are assigned to bugs

```
assignee in membersOf("Inactive Users") AND project = App AND type = bug and status != Closed ORDER BY createdDate DESC
```

### Search for inactive Users who are assigned to stories

```
assignee in membersOf("Inactive Users") AND project = App AND type = Story and status != Closed ORDER BY createdDate DESC
```

## `jvm`

For garbage collection, heap stats: `-XX:+PrintHeapAtGC`

For garbage collection tenuring stats: `-XX:+PrintTenuringDistribution`
The memory size should decline quickly across ages.

For the memory footprint use: `-verbosegc`
Check the values reported

```bash
[Full GC $before->$after($total), $time secs]
```