from collections import defaultdict
from typing import List, Dict

class AverageGDPReport:
    def generate(self, rows: List[Dict[str, str]]):
        gdp_by_country = defaultdict(list)

        for row in rows:
            country = row["country"]
            gdp = float(row["gdp"])
            gdp_by_country[country].append(gdp) 
        
        result = []

        for country, values in gdp_by_country.items():
            avg = sum(values)/len(values)
            result.append((country, round(avg, 2)))

        result.sort(key=lambda x: x[1], reverse=True)
        return result