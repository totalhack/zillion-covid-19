#!/bin/bash

curl "https://raw.githubusercontent.com/kmatarese/glide-covid-19/master/glide_covid_19/data/sqlite.db" > sqlite.db

sqlite3 sqlite.db < sqlite_updates.sql
