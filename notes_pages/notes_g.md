## `gcc`

### Compile flags for different C versions

``` bash
-ansi, -std=c89, -std=c99
```

### Debug level

Compile with level 3 debug information that includes macros. Debug level
2 is the default.

``` bash
gcc -g3 source.c
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

### Linking

Compile without linking

``` bash
gcc -c source.c -o object.o
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

### Enable profiling

``` bash
gcc -a -g -c source.c -o object.o
```


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

The history database file is likely to be soemwhere like this (Chrome):

```
~/Library/Application Support/Google/Chrome/Default\History
%LocalAppData%\Google\Chrome\User Data\Default\History
C:\Users\USERNAME\AppData\Local\Google\Chrome\User Data\Default
```

Extract the URLS to a text file.

``` bash
sqlite3 History "SELECT datetime(last_visit_time/1000000-11644473600,'unixepoch'), url FROM  urls ORDER BY last_visit_time desc" > history_urls.txt
```