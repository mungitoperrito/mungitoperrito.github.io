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

### Garbage collection

Add these switches

- Heap stats: `-XX:+PrintHeapAtGC`
- Tenuring stats: `-XX:+PrintTenuringDistribution`
  The memory size should decline quickly across ages.

### Memory usage

- Footprint `-verbosegc`
