"""Marks Tool - print a short report for a list of marks."""

from config import load_env
from starts import average, highest, lowest

MARKS = [72, 65, 88, 91, 54]

def main():

    settings = load_env()
    print(settings["APP_NAME"])
    print("count  :", len(MARKS))
    print("Average:", average(MARKS))
    print("Highest:", highest(MARKS))
    print("Lowest :", lowest(MARKS))

if __name__ == "__main__":

    main()
