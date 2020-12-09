#!/usr/bin/env python3

# created by: Ryan Walsh
# created on: December 2020
# this program tells you if the year entered is a leap year


def main():
    # this program tells you if the year entered is a leap year

    # input
    year = input("Enter a year please: ")
    print("\n", end="")

    # process & output
    try:
        year = int(year)
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    print("{0} year is a leap year.".format(year))
                else:
                    print("{0} is a common year".format(year))
                    print("\n", end="")
            else:
                print("{0} is a leap year.".format(year))
        else:
            print("{0} is a common year.".format(year))
    except Exception:
        print("That was not a year. Try again.")


if __name__ == "__main__":
    main()
