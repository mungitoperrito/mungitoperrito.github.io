## Zeros

### Zero a file

```bash
cat > fileName <ctrl><c>           # Creates a 0 length file
cat /dev/zero > fileName           # Overwrites a file with 0s
```

## Zipped files

### Extract a file

```bash
zcat filename.gz | someUtil
```

### Get information

- Field and value information: `zipdetails -v`
- Get file contents without extracting: `zipinfo`

### Passwords

Brute-force a zip password: `fcrackzip`

### Read zip files

```bash
zless filename.gz
```

### Repair broken zip file

```bash

# Method one
zip -F input.zip --out output.zip

# Method two
zip -FF input.zip --out output.zip
```

### Uncompress

- `unzip`
