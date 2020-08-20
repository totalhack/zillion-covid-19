Zillion COVID-19
================

This is an example repo showing how one can use
[Zillion](https://github.com/totalhack/zillion) to analyze data related to the
COVID-19 outbreak.

The `zillion` warehouse is defined in `zillion_covid_19/covid_warehouse.json`.
It references a remote sqlite database that is pulled from the Glide COVID-19
[repo](https://github.com/kmatarese/glide-covid-19). The warehouse is
configured to ignore the download if the sqlite database already exists
locally (check in `/tmp` for glide_covid_19.db), so it is a one-time snapshot
unless you adjust the `if_exists` setting in `covid_warehouse.json` or
periodically remove your local sqlite DB so it gets refreshed on the next
warehouse init.

To see the available warehouse metrics, dimensions, and datasources try the
following from the `zillion_covid_19` directory:

```shell
$ python warehouse.py

"""
---- Warehouse
metrics:
  {
      'cases': <Metric name='cases' type='integer'>,
      'cases_cumsum': <Metric name='cases_cumsum' type='integer'>,
      'cumulative_cases': <Metric name='cumulative_cases' type='integer'>,
      ...
"""
```

To run reports on the command line use the `run_report.py` helper script. The
following example would show cases and deaths by country for a particular date
(not cumulative, there are separate metrics for that):

```shell
$ python run_report.py -m cases deaths -d country -c '[("date", "=" , "2020-04-02")]'

"""
             Cases  Deaths
Country
Afghanistan     36       2
Albania         18       1
Algeria        139      28
Andorra         38       1
Angola           0       0
...            ...     ...
Venezuela        3       2
Vietnam         15       0
Yemen            0       0
Zambia           3       1
Zimbabwe         1       0
"""
```

Use `--help` for more information. The output is simply a printed dataframe,
so data may be truncated in the terminal. 

> **Note:** this is meant to be a quick example. Zillion is still in its
infancy and is subject to rapid changes.
