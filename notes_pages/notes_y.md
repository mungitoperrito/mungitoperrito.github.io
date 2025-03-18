## `yum`

### Delete packages post install

```bash
yum clean packages
```

### Upgrade Fedora major version

1. `yum clean all`
1. `rpm -Uhv
     http://download.fedora.redhat.com/pub/fedora/linux/core/6/i386/os/Fedora/RPMS/fedora-release-6-4.noarch.rpm
     http://download.fedora.redhat.com/pub/fedora/linux/core/6/i386/os/Fedora/RPMS/fedora-release-notes-6-3.noarch.rpm`
1. `yum -y update`