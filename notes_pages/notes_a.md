## `alias`

These go in `~/.bashrc` (Linux), `~/.zshrc` (Mac)

- `alias ..='cd ..'`                 # Switch one directory up
- `alias ds='date +%F-%H%M%S'`       # Data string for file extension
- `alias hexdump='od -Ax -tx1z -v'`  # Show file as hex and ascii
- `alias la='ls -al'`                # Long list all files, including hidden
- `alias ll='ls -l'`                 # Long list files
- `alias psg='ps -eaf | grep -i'`    # Grep for processName
- `alias tmpp='export PS1="\W> "'`          # Short prompt
- `alias realp='exportPS1="\u@\h \w> "'`    # Full prompt

### `bash` specific (Linux)

- `alias h='history | tail -n 20'`    # Show last 20 commands (bash)
- `alias hgr='history | grep '`      # Grep history for a string

### Build aliases

- `alias makech='make clean ; make html'`         # Build local site (`yarn`)

### Connections

- `alias rdtop='rdesktop -g 1270x1000 -a 16 -d someDir -u someUser 192.168.33.48 -r sound:remote'`

### `git` aliases

- alias `gac='git add . ; git commit -m' `        # Add to commit, needs message
- alias `gbr='git branch | grep -i '`             # Search for branchName
- alias `gcm='git checkout main'`                 # Switch to main branch
- alias `gst='git status'`                        # Current status
- alias `lsgit='git log --pretty=format:"%h %as %ae %s" | head -n 10'`  # History

### `zsh` specific (OSX)

- `alias h='history 1'`                        # Get all of history
- `alias hgr='history 1|grep'`                 # Grep history for a string


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