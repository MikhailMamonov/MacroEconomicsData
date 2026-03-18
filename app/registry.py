from app.reports.average_gdp import AverageGDPReport

_REPORTS = {
    "average-gdp" : AverageGDPReport(),
}

def get_report(name: str):
    if name not in _REPORTS:
        raise ValueError(f'Unknown report: {name}')
    
    return _REPORTS[name]