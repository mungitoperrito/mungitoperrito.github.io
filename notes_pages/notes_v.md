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

## VMware

### Change to another virtual terminal (vt 1-6)

`chvt 1`

### Config file `machine.vmx`

- Add a cd image `ide1:0.fileName = "/data/isos/EssentiallyBlank.iso"`
- Add a cd image `ide1:0.deviceType = "cdrom-image"`
- Add a cdrom: `ide1:0.deviceType = "cdrom-raw"`
- Add a cdrom: `ide1:0.fileName = "/dev/hdc"`
- Boot order, disable anything other than cd: `bios.bootdeviceclasses = "deny: net hd fd usb"`
- Boot order, disable anything other than pxe: `bios.bootdeviceclasses = "deny: cd hd fd usb"`
- Boot order, force net: `bios.bootdeviceclasses = "allow:net"
- Boot order, force cd: `bios.bootdeviceclasses = "allow:cd"`
- Boot VM to BIOS:
  - `bios.bootDelay = "NUM_TICKS_TO_WAIT_AT_PRESS_F2_SCREEN"`
  - `bios.forceSetupOnce = "true"`
- Don't recreate swap on reboot: `sched.swap.persist = "TRUE"`

### Documentation

- Unofficial documentation of .vmx options: http://sanbarrow.com/vmx.html

### Guest OS specific tweaks

- Red Hat
  - Filesystem remounts as ro.
  - Increase `min_free_kbytes`: `echo "20000" > /proc/sys/vm/min_free_kbytes`

- Ubuntu
  - Turn off beep: Add `'blacklist pcspkr'` to `/etc/modprobe.d/blacklist`

### Headless VM:

- Add to `.vmx`
  - `remoteDisplay.vnc.enabled = TRUE`
  - `remoteDisplay.vnc.port = 5910`
- Start VM: `/usr/lib/vmware/bin/vmware-vmx -qx /path/to/vmxFile.vmx`

### Networking
- Setup network: create a switch -> esxcfg-vswitch -a vSwitch0
- Setup network: create a portgroup -> esxcfg-vswitch -p "Service Console" vSwitch0
- Setup network: assign a NIC -> esxcfg-vswitch -L vmnic0 vSwitch0
- Setup network: config a vswif -> esxcfg-vswif -a vswif0 -p "Service Console" -i 192.xxx.xxx.xxx -n 255.xxx.xxx.xxx
- Stop annoying beep: add 'mks.noBeep = "TRUE"' to .vmx file

### ThinESX

- Add to `dd` command: `conv=notrunc`
