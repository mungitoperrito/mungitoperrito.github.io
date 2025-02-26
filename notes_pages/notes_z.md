## Zipped files

### Get information

- Field and value information: `zipdetails -v`
- Get file contents without extracting: `zipinfo`

### Passwords

Brute-force a zip password: `fcrackzip`

### Repair broken zip file

```bash

# Method one
zip -F input.zip --out output.zip

# Method two
zip -FF input.zip --out output.zip
```

### Uncompress

- `unzip`
