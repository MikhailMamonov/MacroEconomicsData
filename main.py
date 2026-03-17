import argparse
from typing import List, Dict
import csv
from tabulate import tabulate


class CountryData:
    country: str = ""
    gdp_values: List[int]

    def __init__(self, country_name: str, gdp_values: List[int]=[]):
        if(not all(isinstance(gdp, int) for gdp in gdp_values)):
            raise  ValueError
        self.country = country_name
        self.gdp_values = gdp_values
    
    def addGdpValue(self, gdpValue:int):
        if type(gdpValue) is not int:
            raise ValueError
        self.gdp_values.append(gdpValue)
    
    def calculate_average(self) -> float:
        if not self.gdp_values:
            return 0
        return sum(self.gdp_values)/len(self.gdp_values)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Название файлов и отчета")
    parser.add_argument("--files", type=str, nargs="+", help="Список файлов для обработки")
    parser.add_argument("--report", type=str, required=True, help="Отчет")
    return parser.parse_args()


def get_rows(files: List[str]) -> List[List[str]]:
    rows:List[List[str]] = []
    for file in files:
        with open(file, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                rows.append(row)
    return rows

def get_countries_data(rows: List[List[str]]) -> Dict[str, CountryData]:
    rowItemsDict: Dict[str, CountryData] = {}
    for row in rows:
        if is_int(row[2]):
            if not row[0] in rowItemsDict:
                rowItemsDict[row[0]] = CountryData(row[0], [int(row[2])])
            else:
                rowItemsDict[row[0]].addGdpValue(int(row[2]))
        else:
            continue
    return rowItemsDict
    

def write_to_csv(filename:str, countries_data: Dict[str, CountryData]):
    countryGdpPairs: Dict[str, str] = {}
    field = [" ","country", "gdp"]

    for key in countries_data:
        countryGdpPairs[key] =  f"{countries_data[key].calculate_average():.2f}"
    print(countryGdpPairs.items())
    sorted_country_gdp_pairs:Dict[str, str] = dict(sorted(countryGdpPairs.items(), key=lambda x: float(x[1]), reverse=True))
    print(sorted_country_gdp_pairs.items())

    table = []
    counter = 0
    for k,v in sorted_country_gdp_pairs.items():
        counter+=1
        print(k,v)
        table.append([counter, k, v])
    print(table)
    
    print(tabulate(table, tablefmt="grid", floatfmt=".2f", headers=field))

    with open(f'{filename}.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(field)
        counter = 0
        for key in sorted_country_gdp_pairs:
            counter+=1
            writer.writerow([counter, key, sorted_country_gdp_pairs[key]])

def is_int(element: any) -> bool:
    #If you expect None to be passed:
    if element is None: 
        return False
    try:
        int(element)
        return True
    except ValueError:
        return False

def main():
    args = parse_args()
    print(args)
    rows = get_rows(args.files)
    countriesData = get_countries_data(rows)
    write_to_csv(args.report, countriesData)



if __name__ == "__main__":
    main()