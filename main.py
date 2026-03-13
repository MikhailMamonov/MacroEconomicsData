import argparse
from typing import List, Dict
import csv


class CountryData:
    country: str = ""
    year: int = 0
    gdp: int = 0
    gdp_growth: float = 0.0
    inflation: float = 0.0
    unemployment: float = 0.0
    population: int = 0
    continent: str = ""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Название файлов и отчета")
    parser.add_argument("--files", type=str, nargs="+", help="Список файлов для обработки")
    parser.add_argument("--report", type=str, help="Отчет")
    return parser.parse_args()


def get_rows(files: List[str]) -> List[List[str]]:
    rows:List[List[str]] = []
    for file in files:
        with open(file, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                rows.append(row)
    return rows

def get_country_data_items(rows: List[List[str]])-> Dict[str, List[CountryData]]:
    countryDataDict ={}
    

    




def main():
    args = parse_args()
    print(args)
    rows = get_rows(args.files)
    rowItems: Dict[str, List[CountryData]] = 






if __name__ == "__main__":
    main()