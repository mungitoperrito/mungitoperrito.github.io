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

### `machine.vmx` config file

- Add a cdrom: `ide1:0.deviceType = "cdrom-raw"`
- Add a cdrom: `ide1:0.fileName = "/dev/hdc"`
- Add a cd image `ide1:0.fileName = "/data/isos/EssentiallyBlank.iso"`
- Add a cd image `ide1:0.deviceType = "cdrom-image"`
- Boot order, disable anything other than cd: `bios.bootdeviceclasses = "deny: net hd fd usb"`
- Boot order, disable anything other than pxe -> bios.bootdeviceclasses = "deny: cd hd fd usb"
vmware: Boot order, force just one ( net )-> bios.bootdeviceclasses = "allow:net"
vmware: Boot order, force just one ( cd ) -> bios.bootdeviceclasses = "allow:cd"
vmware: Boot VM to BIOS -> bios.bootDelay = "NUM_TICKS_TO_WAIT_AT_PRESS_F2_SCREEN"
vmware: Boot VM to BIOS -> bios.forceSetupOnce = "true"
vmware: Change to another virtual terminal: chvt 1 ( cmd line 1-6 ) ( X 7 )
vmware: Don't recreate swap each GOS reboot -> sched.swap.persist = "TRUE"
vmware: Headless VM boot 1, edit .vmx to include: remoteDisplay.vnc.enabled = TRUE vmware: vmware: vmware: Headless VM boot 2, edit .vmx to include: remoteDisplay.vnc.port = 5910
vmware: headless VM boot 3, start VM by:  /usr/lib/vmware/bin/vmware-vmx -qx /path/to/vmxFile.vmx
vmware: dd On ThinESX:  need to add  conv=notrunc
vmware: Install WS in VM on Windows -> HKEY_LOCAL_MACHINE\SOFTWARE\VMware, Inc.\Misc\InstallInVM = 0
vmware: RH filesystem remounts as ro: increase min_free_kbytes, echo "20000" > /proc/sys/vm/min_free_kbytes
vmware: Setup network: create a switch -> esxcfg-vswitch -a vSwitch0
vmware: Setup network: create a portgroup -> esxcfg-vswitch -p "Service Console" vSwitch0
vmware: Setup network: assign a NIC -> esxcfg-vswitch -L vmnic0 vSwitch0
vmware: Setup network: config a vswif -> esxcfg-vswif -a vswif0 -p "Service Console" -i 192.xxx.xxx.xxx -n 255.xxx.xxx.xxx
vmware: Stop annoying beep: add 'mks.noBeep = "TRUE"' to .vmx file
vmware: Stop annoying beep, Ubuntu server: add 'blacklist pcspkr' to /etc/modprobe.d/blacklist
vmware: Unofficial documentation of .vmx options -> http://sanbarrow.com/vmx.html