## `vim`

### Block mode

- Enter block mode: `^v`

### Configuration

- Change color of line numbers: `:highlight LineNr ctermfg=grey`

### Delete

- Delete a regex `'?<tag>stuff</tag>`: `:1,$ s/?.*//`
- Up to but not including next 'Aa': `d/Aa`

### Enable features

- New features: Add `'set nocompatible'` to `.exrc`.
- Better blocks: Add `'set virtualedit=block'` to `.exrc`

### Execute command

- Command is in buffer x: `@x`
- Decrement a number, with cursor on the number: `^x`
- Increment, with cursor on the number: `^a`
- Record commands to register `a`: `qa [ type commands ] q`
- Remove extra white space: `:1,$s/[ ^I]*$//g`

### Find text

- Match parenthesis, put cursor on  `) ] }` and press `%`

### Movement

- Go to beginning end of the block: `o`

### Select text

- By characters, from current position to 'Aa': `v /Aa`
- By lines, from current pos to 'Aa': `V /Aa`

### Replace text

- From start to end of file: `:1,$s/find/replace/g`
- From to end of file: `:%s/find/replace/g`

### Yank text to and from buffers

- Yank all text up to `#` into buffer `a`: `"ayt#`
- Yank all text up to `#`, append into buffer `a`:  `"Ayt#`