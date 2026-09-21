"""Marks Tool - print a short report for a list of marks."""

from config import load_evn
from stats import average, highest

MARKS = [72, 65, 88, 91, 54]

def main():
    settings = load_env()
    print(settings["APP_NAME"])
    print("count :", len(MARKS))
    print("Average:", average(MARKS))
    print("Highest:", highest(MAEKS))

if __name__ == "__main__":
    main()
