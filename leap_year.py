#!/usr/bin/env python3

# Created by: Titwech wal
# Created on: Apirl 13
# program tells user the leap year
# with their input


# checks if it is a leap year
def main():
    user_year_string = input("Enter a year: ")
    print("")
    try:
        # casts user input to integer
        user_year_int = int(user_year_string)
        if (user_year_int % 4) == 0:
            if (user_year_int % 100) == 0:
                if (user_year_int % 400) == 0:
                    # displays that it is a leap year
                    print("It's a leap year!")
                else:
                    print("This is not a leap year.")
            else:
                print("It's a leap year!")
        else:
            print("This is not a leap year.")
    # checks for errors
    except Exception:
        print("{} is not valid. Enter a number". format(user_year_string))


if __name__ == "__main__":
    main()
