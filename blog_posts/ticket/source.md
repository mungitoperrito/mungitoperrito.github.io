# Ticket to Ride

<p align="center"><kbd><img src="./img/hero.jpg" border="5" width="800"
alt="An open highway and a lego figure."></kbd></p>

It's the end of the month and I have a long drive ahead of me. Will the police
out in force trying to meet monthly ticket quotas?

Do the police really have ticket quotas? They say they don't. Most people don't
believe them.

Luckily, there’s some data. The state Maryland has contributed a collection of
traffic violation data to [data.gov](https://data.gov/). It’s one of 300,000
data sets that you can explore for free.

Follow along and explore Maryland's Traffic Data.

## Getting Started

A good study needs a hypothesis.

**Hypothesis**: The police issue more tickets at the end of the month because
they are trying to meet quotas.

One way to check this hypothesis is to check the ticket-issue rate over several
months. Data.gov has searchable metadata for the data sets in its collection.
The metadata for the [Traffic
Violations](https://catalog.data.gov/dataset/traffic-violations) dataset says it
is a csv file from Montgomery County that "contains traffic violation
information from all electronic traffic violations issued in the County".

<p align="center"><kbd><img src="./img/csv_web_page.jpg" border="5" width="800"
alt="Dataset description page."></kbd></p>

## Prepare the data

Download the [csv
file](https://data.montgomerycountymd.gov/api/views/4mse-ku6q/rows.csv?accessType=DOWNLOAD).

The next step, a key step in every data analysis, is to validate the data. The
traffic ticket data is stored in a giant csv table. To make working with the
data easier, create an SQLite database and import the data from the file.

### Inspect the file

The csv file is about 375MB in size has just under 1.1 million rows.

- Use the `head` command to see the first few rows.

```bash
head Traffic_Violations.csv
```

The output looks like this:

<p align="center"><kbd><img src="./img/first-few-rows.jpg" border="5" width="800"
alt="Head command output"></kbd></p>

To spot check the data consistency, run some checks with your system utilities
before you attempt to import the file. For example:

- Check the number of lines in the file

  ```bash
  wc -l Traffic_Violations.csv
  ```    `grep`.

- Check for the range of years. The second field is `Date of Stop`. This check
  was supposed to find the range of years in the file. Instead, it showed a large
  number of bad data entries.

  ```bash
  cut -f 2 -d"," < Traffic_Violations.csv | cut -f3 -d'/' | sort -u
  ```

You could try to fix bad fields, you can drop those rows entirely, or you can
code around the problems later. For this study, I added `WHERE` clauses to my
SQL queries when I knew there were data problems.

### File format issues

The input file is a csv file. That could mean 'character separated values' or
'comma separated values'.

In this file, commas supposed to be reserved characters that separate the fields
in each row. That didn’t happen. Commas are used within fields as normal
punctuation and as field separators. Even worse, the use of commas within fields
is inconsistent.

That makes parsing the file tricky. For example, in some rows the subagency
(usually a geographic designation) sometimes has a comma in its name.
Geographic coordinates are sometimes reported as "(latitude, longitude)".

There are other problems too. Many rows are too sparse, missing values in lots
of their fields. Instead of guess what should be there, I dropped rows that are
too sparse.

This is the [Python script](./fix-and-load.py) that cleans the data and uploads
it to the SQLite database. Cleanup drops about 1800 rows, a little less than 1%
of the total.


## Explore the data, set a date range

The data cleaning step shows problem with the date field. Dates are an important
element of this study, so it is important to handle the date field carefully.

**NOTE**: There is a new csv file now, unfortunately it has new problems. The
discussion here follows the data in the old file.

### Set bounds

What should the upper and lower bounds be for the date field?

The last data update is in 2015. That sets an upper bound for the dates.

To find the lower bound, run a `SELECT` query to check the possible values, then
choose a year that has a significant number of tickets to avoid noise.

At the lower end of the range, the number of rows per year drops off sharply
before 1994. There are still significant numbers in the early 1990s. I set an
arbitrary cut off at 1990. The study period runs from 1990 to 2015.

```sql
SELECT year, count(year) FROM alldata GROUP BY year;
```

The output looks like this:

```
0 809
4 3
5 1
6 3

<--SNIP-->

1990 3005
1991 3659
1992 5651
1993 6881
1994 12017
1995 16694

<--SNIP-->

2015 29480
2016 14522
2017 2022
2018 4

<--SNIP-->

9563 1
9867 1
9999 29
```

### Parse the date field into subfields

In the csv file the date is a single field that has the format `mm/dd/yyyy`.
That format is too course for the hypothesis. Add columns for the `year`,
`month` and `day`. Alternatively, use a database that has a `date` datatype.
(SQLite doesn't have a `date` type)

```python
def parse_date(date_of_stop_field):
    month, day, year = date_of_stop_field.split('/')
    day_of_week = datetime.date(int(year), int(month), int(day)).weekday()

    return "," + year + "," + month + "," + day + "," + str(day_of_week)
```

(See [the full source](fix-and-load.py).)

## Visualize the data

A plot of tickets by day should show ticketing trends over months. Here is a
first attempt at plotting the data.

<p align="center"><kbd><img src="./img/viz_01.jpg" border="5" width="800"
alt="Tickets by day, version one"></kbd></p>

Well! There is a serious downward trend at the end of the month.

It the hypothesis is correct, tickets should trend upwards at the end of the
month.

What’s going on?

Months don't have uniform length. All months are 28 days long, not all months
are 31 days long. This view adjusts the graph to account for the different
month lengths. It shows the number of tickets per `month-day`.

<p align="center"><kbd><img src="./img/viz_02.jpg" border="5" width="800"
alt="Tickets by month-day, version two"></kbd></p>


The second graph is more balanced in terms of tickets per day. Men
hover around 76.5 citations per day over the 15 years from 1990 to
2015. Women average slightly more than half that figure, just 37.9
citations per day. Both averages are pretty consistent throughout the
month, however, even with this frequency weighted view, the number
of citations per day drops off towards the end of the month. That result
is the opposite of popular opinion and supports the oft repeated
statement from law enforcement that there are no quotas. “But”, asks
the skeptic in the room, “perhaps there is a yearly quota?”
“Or a weekly one?”
The data doesn’t support either of those suggestions. In all cases: day of
the month, day of the week, and month of the year, there are more
citations given out toward the beginning of the period rather than
towards the end. Given these figures it is hard to conclude that there is
a last minute drive to meet a quota each month.
That settles the argument then. The data doesn’t lie. Or does it? It turns
out there are some difficulties with the data set.
Difficulties with the data
Even a cursory look at these numbers show men consistently getting
twice as many citations as women over the entire 15 year period which
is a surprising result. People may debate just how surprising it is that
men get more tickets than women, but it is at least a little surprising
that men would be cited twice as often as women. The US Census
website reports that Maryland has a slightly large proportion of females
(51.5%) than males (48.5%).
With roughly equal numbers of men and women, it seems reasonable to
assume roughly equal numbers of male and female drivers. Perhaps
there was an unreported selection process that skewed the data set. A
few more queries and a closer look at the data indicate that there was,
in fact, an additional selection criterion. All of the citations in the data
set are related to traffic accidents.
It is certainly interesting to see that men are ticketed in accidents twice
as often as women, and that accident rates appear to be skewed
towards the early parts of each week and month. Unfortunately since
this data set only lists citations related to accidents and is silent on nonaccident ticket rates, it means that this data set, as attractive as it may
be, is insufficient to answer the original question. Additional data on
non-accident related tickets is required to see if non-accident related
citations are also issued at the same rate as accident related tickets.
Sadly, we don’t have that data.
Unanswered questions
So we don’t have much insight into the original question, “are there
ticket quotas”. On the other hand we now have a few more topics for
investigation. Do men really have twice as many accidents as women or
do they just get ticketed twice as much for accidents they are involved
in? Why are there spikes in the accident rate at the beginning of the
week? Is there a significant number of accidents where tickets aren’t
issued? Is there a way to determine how many people and or vehicles
were involved in a given accident? And perhaps the biggest question for
this audience—where can researchers find the data needed to answer
these questions?
Conclusion
The Maryland data set is rich and can provide many interesting avenues
of research. Unfortunately it only contains a subset of all citations
issued and so it is insufficient to answer the question about quotas.
However, working with this dataset has been a useful exercise, and it
was especially valuable as an illustration of why it is critical to check
data integrity, to clean incoming data, and to validate assumptions
about the dataset before drawing conclusions from it.
Additional notes and details
For those curious about some of the more mechanical details of this
investigation, the next sections discuss one or two points that didn’t
really fit in the story but that may be of some interest.
How to configure sqlite3 output
The default output style in sqlite3 works for some parsing tasks, but it is
not ideal for all purposes. When exploring data it may be helpful to
change the output to columnar form and to add a header row.
Use of SUM or COUNTin data assessment
COUNT works well when field values are easily filtered. On the other
hand, if the values in the dataset are encoded as 1s and 0s then using
SUM can be better quick way to get an aggregate count over a field.
There are two benefits to using SUM like this. The SQL is more compact
with SUM (there’s no where clause) and rows are returned when the
sum equals zero (COUNT doesn’t return the output row in sqlite).
Here’s an example counting alcohol related citations issued to Male
drivers.
sqlite> SELECT year, COUNT(Alcohol)
...> FROM alldata
...> WHERE (year > '1989') AND (year < '2001')
AND gender = 'M' AND alcohol = 1
...> GROUP BY year;
Year COUNT(Alcohol)
---------- --------------
1992 31
1993 42
1994 44
1996 44
1997 48
1998 35
1999 43
2000 103
sqlite> SELECT year, SUM(Alcohol)
...> FROM alldata
...> WHERE (year > '1989') AND (year < '2001')
AND gender = 'M'
...> GROUP BY year;
Year SUM(Alcohol)
---------- ------------
1990 0
1991 0
1992 31
1993 42
1994 44
1995 0
1996 44
1997 48
1998 35
1999 43
2000 103
sqlite>
Thanks for reading this far, I hope these notes prove useful!

Originally posted to [Medium](https://medium.com/) on February 9, 2019.
Updated December, 20 2024.
Updated March, 6 2025.