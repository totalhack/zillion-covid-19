#!/usr/bin/env python
"""Helper script to test out reports

Example:
python run_report.py -m cases deaths -d date -c "[('date', '>', '2020-03-20')]"
"""
import ast
import logging

from tlbx import Script, Arg, st

from zillion_covid_19.warehouse import wh


@Script(
    Arg("-m", "--metrics", nargs="+", help="Metrics to include in report"),
    Arg("-d", "--dimensions", nargs="+", help="Dimensions to include in report"),
    Arg("-c", "--criteria", help="String to be eval'd as criteria param"),
    Arg("-ll", "--log_level", type=int, default=None, help="Set log level"),
)
def main(metrics=None, dimensions=None, criteria=None, log_level=None):
    if criteria:
        criteria = ast.literal_eval(criteria)

    if log_level:
        logger = logging.getLogger()
        logger.setLevel(log_level)

    print("Metrics:", metrics)
    print("Dimensions:", dimensions)
    print("Criteria:", criteria)

    result = wh.execute(metrics=metrics, dimensions=dimensions, criteria=criteria)
    print(result.df_display)


if __name__ == "__main__":
    main()
