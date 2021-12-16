from datetime import datetime
import locale as lc


def get_arival_date():
    while True:
        date_str = input("Enter arrical date (YYYY-MM_DD): ")
        try:
            arrival_date = datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Try again.")
            continue

        now = datetime.now()
        today = datetime(now.year, now.month, now.day)
        if arrival_date < today:
            print("Arroval date must be today or later. Try again.")
            continue
        else:
            return arrival_date


def get_departure_date(arrival_date):
    while True:
        date_str = input("Emter departure date (YYYY-MM-DD): ")
        try:
            departure_date = datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Try again.")

        if departure_date <= arrival_date:
            print("Departure date must be after arrical date. Try again.")
            continue
        else:
            return departure_date


def print_reservation(arrival_date, departure_date, rate, rate_message):
    result = lc.setlocale(lc.LC_ALL, "")
    if result[0] == "C":
        lc.setlocale(lc.LC_ALL, "en_US")

    total_nights = (departure_date - arrival_date).days
    total_cost = rate * total_nights

    date_format = "%B %d, %Y"
    print("Arrival Date: ", arrival_date.strftime(date_format))
    print("Departure Date: ", departure_date.strftime(date_format))
    print("Nightly Rate: ", lc.currency(rate), rate_message)
    print("Total nights: ", total_nights)
    print("Total price: ", lc.currency(total_cost))
    print()



def main():
    print("Hotel Reservation program")
    while True:

        arrival_date = get_arival_date()
        departure_date = get_departure_date(arrival_date)
        print()

        rate = 85.0
        rate_message = ""
        if arrival_date.month == 8:
            rate = 105.0
            rate_message = "(High Season)"

        print_reservation(arrival_date, departure_date, rate, rate_message)

        result = input("Continue? (y/n): ")
        print()
        if result.lower() != "y":
            print("Exit")
            break

if __name__ == "__main__":
    main()
