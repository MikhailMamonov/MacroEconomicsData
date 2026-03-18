import argparse

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Название файлов и отчета")
    parser.add_argument("--files", type=str, nargs="+", help="Список файлов для обработки")
    parser.add_argument("--report", type=str, required=True, help="Отчет")
    return parser.parse_args()
