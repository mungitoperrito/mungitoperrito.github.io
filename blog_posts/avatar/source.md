# Avatar: Data mining Skype
<br>
<p  align="center"><kbd><img src="img/hero..01.jpg" alt="Abstract image"></kbd></p>
<br>


Your Skype profile stores a lot of useful information. All it takes is a little
data mining to find the gems. Read on for an introduction to what's there.

This post shows you how to manipulate the database behind your profile so you
can collect pictures of the people in your Skype contact list.

## Architecture

Skype uses [SQLite](https://www.sqlite.org/) databases as a local storage
backend. Your profile has a few different files. Fortunately, the files are all
in the same directory. On Windows the default path is like this:

`C:\Users\USERNAME\AppData\Roaming\Skype\SKYPE_NAME`

Replace USERNAME and SKYPE_NAME with your username and Skype handle.

SQLite stores each database in a single file. The database file that has the
contact information is called `main.db`.

## Explore `main.db`

To review the tables and database structure, use the SQLite commandline tool,
[`sqlite3`](https://docs.python.org/3/library/sqlite3.html), to open `main.db`

```bash
sqlite3 main.db
```

SQLite uses standard SQL for queries. To get a list of the tables in `main.db`,
query the database meta-data.

```sql
SELECT name
FROM sqlite_master
WHERE
    type='table';
```

The query returns a list like this:

```
DbMeta
AppSchemaVersion
Contacts
<Many more tables not listed here>
```

Look at the `Contacts` table. This table has information on the avatars your
connections use.

SQLite uses dot commands to change formats and to execute utility commands. To
list the fields in the `Contacts` table, use the `.schema` dot command.

```bash
.schema contacts
```

This is a snippet from the command output. The actual output is much longer.

```sql
CREATE TABLE Contacts (
    id INTEGER NOT NULL PRIMARY KEY,
    is_permanent INTEGER,

    <many more columns>

    avatar_url TEXT,
    avatar_url_new TEXT,
    avatar_hiresurl TEXT,
    avatar_hiresurl_new TEXT,

    <many more columns>);
```

## Get the Avatar URL list

The `avatar_url` field contains pointers to your contacts' avatars. To see the
values, run a standard SQL query:

```sql
SELECT avatar_url
FROM contacts
WHERE avatar_url != 'None';
```

Depending on your contact list, there could be a lot of urls.

To output to a file, use the `.output` dot command then rerun the query. The
`.mode` command tell SQLite to create a csv file.

This  example creates an comma separated output file called `url_list`.

```sql
.mode csv
.output url_list

SELECT avatar_url
FROM contacts
WHERE avatar_url != 'None';
```

## Fetch the avatar files

Create a directory to hold the avatars. Change into the new directory and run
`wget` to retrieve the avatar files.

```bash
wget -i url_list
```

## Clean up the file names

The avatar filenames fall into two categories.

One set has names that look like this:

```bash
a_skype_name@auth_key=22222222
another_skype_name@auth_key=12345678
yet_another_skype_name@auth_key=234567890
```

The other filenames follow this pattern:

```bash
public
public.1
```

The `public` style names need file extensions. To add the `.jpg` extension, run
these `bash` commands:

```bash
for f in $(ls pub*) ; do mv ${f} ${f}.jpg ; done
```

To clean up the `auth_key` files, remove `@auth_key=` and then add the `jpg`
extension

```bash
for f in $(ls *@*) ; do mv ${f} $(ls ${f}|cut -d'@' -f1).jpg ; done
```

## Conclusion

And that's it! Have a look at the avatars and save the ones you like.

If there are images you don't recognize, you can use the filenames to query the `Contacts`
database for the `skypename` or `fullname` fields to find the owner.

Of course, you may want other details too, have fun exploring!

Originally posted to [Medium](https://medium.com/) on January 19, 2019.
Updated December, 15 2024.