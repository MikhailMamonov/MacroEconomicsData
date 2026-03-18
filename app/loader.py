from typing import List, Dict
import csv

def get_rows(files: List[str]) -> List[Dict[str, str]]:
    rows:List[Dict[str,str]] = []
    for file in files:
        with open(file, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                rows.append(row)
    return rows