## Artifactory

### Installation notes
Install on Ubuntu 18.04 (bionic). There was no bionic repository
available. Modify the
[installation instructions](https://www.jfrog.com/confluence/display/RTF/Installing+on+Linux+Solaris+or+Mac+OS#InstallingonLinuxSolarisorMacOS-RPMorDebianInstallation) to use a
xenial repository instead of bionic.

``` bash
# echo "deb https://jfrog.bintray.com/artifactory-debs {distribution} {components}" | sudo tee -a /etc/apt/sources.list
echo "deb https://jfrog.bintray.com/artifactory-debs xenial main" | sudo tee -a /etc/apt/sources.list
```

Install the repo key

``` bash
curl https://bintray.com/user/downloadSubjectPublicKey?username=jfrog | sudo apt-key add -
```

Update the repos and install the artifactory package

``` bash
apt-get update
apt-get install jfrog-artifactory-oss
```

### Operation notes

Ubuntu 18 uses systemd. Modify instructions to use systemctl

``` bash
# Activate artifactory
systemctl start artifactory.service

# Check status
$> systemctl status artifactory.service
```

Find and make a note of: `${ARTIFACTORY_HOME}`

``` bash
for i in $(ps -efl |grep artif) ; do echo $i ; done  |grep home
```

Set the value: `-Dartifactory.home=/var/opt/jfrog/artifactory`

Check log file locations:

``` bash
ls /var/opt/jfrog/artifactory/logs/       # Better
ls /opt/jfrog/artifactory/tomcat/logs
```

Login to check the site (browser based).

```bash
http://npm:8081/artifactory/webapp/#/home
```

## `as`

### Assemble an executable

``` bash
as asm_source.s
```