from tabulate import tabulate
from app.parser import parse_args
from app.loader import get_rows
from app.registry import get_report



def run_cli():
    args = parse_args()
    print(args)
    rows = get_rows(args.files)

    report = get_report(args.report)
    result = report.generate(rows)

    field = ["country", "average gdp"]
    print(tabulate(result, tablefmt="grid", floatfmt=".2f", headers=field))