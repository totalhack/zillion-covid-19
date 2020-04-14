Zillion COVID-19
================

This is an example repo showing how one can use
[Zillion](https://github.com/totalhack/zillion) to analyze data related to the
COVID-19 outbreak.

The `zillion` warehouse is defined in `zillion_covid_19/covid_warehouse.json`.
It references a local sqlite database that has been pulled from the Glide COVID-19
[repo](https://github.com/kmatarese/glide-covid-19). A handful of views have been
added to aid in the warehouse definition. Updates to that database can be synced
using the `sync_sqlite_db.sh` script.

To see the available warehouse metrics, dimensions, and datasources try the following
from the `zillion_covid_19` directory:

```shell
$ python warehouse.py
```

To run reports on the command line use the `run_report.py` helper script. The
following example would show cases and deaths by country for a particular date
(not cumulative, there are separate metrics for that):

```shell
$ python run_report.py -m cases deaths -d country -c '[("date", "=" , "2020-04-02")]'
```

Use `--help` for more information. The output is simply a printed dataframe,
so data may be truncated in the terminal. 

> **Note:** this is meant to be a quick example. Zillion is still in its infancy and
is subject to rapid changes. The source data is not being updated automatically.
