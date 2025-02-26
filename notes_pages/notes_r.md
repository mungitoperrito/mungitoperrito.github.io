## Rename files

### Shorten file name

```bash
for fn in `ls` ; do new="$( echo $fn | cut -c 5- )" ; mv $fn $new ; done
```

### bash: rename files

```bash
for fn in $(ls) ; do  mv "${fn}" "${fn/patternToMatch/replacementPattern}" ; done
```