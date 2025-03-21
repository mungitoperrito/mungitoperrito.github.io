## `gcc`

### Compile flags for different C versions

``` bash
-ansi
-std=c89
-std=c99
```

### Compile without linking

``` bash
gcc -c source.c -o object.o
```

### Debug level

Compile with level 3 debug information that includes macros.

Debug level 2 is the default.

``` bash
gcc -g3 source.c
```

### Enable profiling

``` bash
gcc -a -g -c source.c -o object.o
```

### Generate assembly code

Generate assembly code, `asm.s`. The output is not linked.

``` bash
gcc -S source.c -o asm.s
```

### Libraries

- Compile with static libraries

    ``` bash
    gcc -static source.c
    ```

- Compile with dynamic libraries

    ``` bash
    gcc -dynamic source.c
    ```

### Optimize the executable

Compile for optimized output. Level 0 is unoptimized output.

``` bash
gcc -O2 source.c
```

### PATH

- Print search PATH information

    ``` bash
    gcc -print-search-dirs hello.c -o hello
   ```

- Print linker search PATH

    ``` bash
    echo $LD_LIBRARY_PATH
    ```


## `gdb`

### `catchpoints`

- Alert when exec calls happen
- Alert when library loads happen

### Debug binary execution

```bash
gdb FILENAME`
```

### `watchpoints`

- Check if an expression changes value.


## `ghc`

The Haskell compiler. If `ghc`and the other Haskell tools are installed under
`stack`, the command line calls are different.

```bash
stack ghc         # If installed via stack
ghc               # If installed standalone
```


## `ghci`

The Haskell interactive shell.

```bash
stack ghci         # If installed via stack
ghci               # If installed standalone
```

### Modules

- Load: `:module SomeModule`
- UNload: `:module -SomeModule`

### Multiline entry

Use `;` or colon-bracket syntax.

```haskell
:{
  polynomial :: Double -> Double
  polynomial x = x^2 -x -1
:}
```


## `git`

### Aliases

- alias `gac='git add . ; git commit -m' `        # Add to commit, needs message
- alias `gbr='git branch | grep -i '`             # Search for branchName
- alias `gcm='git checkout main'`                 # Switch to main branch
- alias `gst='git status'`                        # Current status
- alias `lsgit='git log --pretty=format:"%h %as %ae %s" | head -n 10'`  # History

### Compare two branches

```bash
git show-branch –sha1-name newFeature main
```

### `gitconfig`

- Use rebase rather than merge in all repos: `git config --global pull.rebase true`

### See commit history

- Author, relative time, subject: `git log --pretty=format:"%h  %an, %ar: %s"`
- Branch info, subject: `git log --decorate --pretty=format:"%h %s"`
- Commit graph, subject: `git log --graph --pretty=format:"%h %s"`
- Commit graph, author email, subject: `git log --graph --pretty=format:"%h %ae %s"`
- Last commit message`: `git log -1 -p`
- Last five commits: `git log -5 --oneline`

### Shortcuts

- Adds files to commit, adds comment: `git commit -a -m 'made some changes'`
- Create newBranch, check out: `git checkout -b newBranch`

### Use a different `ssh` key

It can be any git command.

```bash
 ssh-agent bash -c 'ssh-add ../other-id_rsa-key ; git push'
```


## GitHub

### Get git repos

```bash
curl -i -H 'Authorization: token <auth-token>' https://api.github.com/orgs/your-repo/repos | grep "html_url"
```

### Get last 100 commits

```bash
curl -i -H 'Authorization: token <auth-token>' https://api.github.com/repos/your-repo/application/commits?per_page=100
```

### Get commit activity

```bash
curl -i -H 'Authorization: token <auth-token>' https://api.github.com/repos/your-repo/application/stats/commit_activity
```

### Get commit stats

```bash
curl -i -H 'Authorization: token <auth-token>' https://api.github.com/repos/your-repo/application/stats/code_frequency
```

### Get a commit

```bash
curl -i -H 'Authorization: token <auth-token>' https://api.github.com/repos/your-repo/application/commits/<commit-id>
```


## Google search

### Change default results display from All to Web

Create a new search engine for the browser.

- Use web view
- Show 25 results per page. (This is inconsistent)

```
{google:baseURL}/search?num=25&udm=14&q=%s
```

Set the new search engine as the browser default

### Export search history

The history database file PATH is like one of these (Chrome):

```
~/Library/Application Support/Google/Chrome/Default\History

%LocalAppData%\Google\Chrome\User Data\Default\History

C:\Users\USERNAME\AppData\Local\Google\Chrome\User Data\Default
```

Extract the URLS to a text file.

``` bash
sqlite3 History "SELECT datetime(last_visit_time/1000000-11644473600,'unixepoch'), url FROM  urls ORDER BY last_visit_time desc" > history_urls.txt
```

### Search operators

- Search one site: `site:someSite.com`
- Logical operators: `"termOne" AND ("termTwo" OR "A specific phrase")`


## Groups

### Add user to a group

```bash
sudo usermod -a -G someGroup someUser
```
