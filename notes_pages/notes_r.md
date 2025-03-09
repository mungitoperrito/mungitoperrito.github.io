## RAM disks

Create a virtual drive in RAM memory to speed operations.

### Create and mount a RAM disk

```bash
mkdir -p /ramdisk
mkfs -b 1024 -0 Linux -L RAMDisk -T ext2 /dev/ram0 65536
mount /dev/ram0 /ramdisk
```

### Create and mount a zeroed RAM disk

This method creates a disk that is all 0s.

```bash
# Create a node
mknod -m 660 /dev/ram b 1 1

# Create a zeroed disk
dd if=/dev/zero of=/dev/ram bs=1024 count=4000

# Create a mount point and mount the RAM disk
mkdir /mnt/ramdisk
mount -t ext2 /dev/ram /mnt/ramdisk
```

### Mount a RAM disk

Mount an existing RAM disk.

```bash
mkdir -p /ramdisk
mount -t ramdisk none /ramdisk -o maxsize=65536
chmod 7777 /ramdisk
```


## rdesktop

Use `rdesktop` on Linux to connect to Windows machines.

```bash
# Screen size, color depth, directory, user, remote IP, where to paly sound
rdesktop -g 1152x921 -a 16 -d DIRECTORY -u USER_LOGIN 192.168.33.48 -r sound:remote
```


## RDP

Use Remote Desktop Protocol to connect Windows machines.

### Send <ctrl><alt><del>

```
<ctrl><alt><end>
```

### Test connection

1. Connect to RDP on `10.0.0.1`: `telnet 10.0.0.1 3389`
1. Get telnet command prompt: `<ctrl><]>`
1. Disconnect: `close`


## Redhat configuration

### Edit firewall, SELinux settings

```bash
system-config-securitylevel
```


## Regular expressions

### Double letters

```
(.)\l
```


## Rename files

### Shorten file name

```bash
for fn in `ls` ; do new="$( echo $fn | cut -c 5- )" ; mv $fn $new ; done
```

### bash: rename files

```bash
for fn in $(ls) ; do  mv "${fn}" "${fn/patternToMatch/replacementPattern}" ; done
```

## RPM

Old Redhat package manager. `yum` is newer.


### Install the Redhat signature file

```bash
rpm --import /usr/share/rhn/RPM-GPG-KEY
```

### List changes to files

```bash
rpm -Va > changes.date  ( diff files periodically to find changes )
```

### List package info

```bash
rpm -qip newPackage.rpm
```

### Unpack without installing

```bash
rpm2cpio newpackage-1-51.rpm | cpio -i --make-directories
```

## Run levels

`update-rc` replaces `chkconfig` on Ubuntu.

### Check services

```bash
chkconfig --list some_service_name
```

### Enable service

```bash
chkconfig --level 35 some_service_name on
```