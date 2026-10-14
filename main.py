
from datetime import datetime, timezone

def parse_date(value):
    formats = [
        "%Y-%m-%d %H:%M:%S",  # 2026-10-14 15:30:00
        "%Y-%m-%d",            # 2026-10-14
        "%d/%m/%Y %H:%M:%S",  # 14/10/2026 15:30:00
        "%d/%m/%Y",            # 14/10/2026
        "%m/%d/%Y %H:%M:%S",  # 10/14/2026 15:30:00
        "%m/%d/%Y",            # 10/14/2026
        "%d-%m-%Y %H:%M:%S",  # 14-10-2026 15:30:00
        "%d-%m-%Y",            # 14-10-2026
        "%Y-%m-%dT%H:%M:%S",  # 2026-10-14T15:30:00
        "%Y-%m-%dT%H:%M:%SZ", # 2026-10-14T15:30:00Z
    ]

    for fmt in formats:
        try:
            return datetime.strptime(value.strip(), fmt)
        except ValueError:
            continue

    raise ValueError("Unsupported date format.")

def convert_to(date_time):

    if date_time.tzinfo is None:
        date_time = date_time.astimezone()

    return int(date_time.timestamp())


def convert_from(timestamp):
    return datetime.fromtimestamp(timestamp, tz=timezone.utc)


def main():
    while True:

        print("\n==============================================")
        print("          Unix Timestamp Converter")
        print("==============================================\n")

        print("0. Exit")
        print("1. DateTime to Unix Timestamp")
        print("2. Unix Timestamp to DateTime")

        print("\n==============================================\n")

        option = input("Select option: ").strip()

        if option == "0":
            print("Closing...")
            break

        if option not in ("1", "2"):
            print("\nInvalid option.")
            continue

        try:
            if option == "1":
                value = input(
                    "Enter date and time: "
                ).strip()

                date_time = parse_date(value)

                result = convert_to(date_time)

                print(f"\nUnix Timestamp: {result}")

            elif option == "2":
                value = int(input("Enter Unix Timestamp: ").strip())

                result = convert_from(value)

                print(f"\nDateTime UTC: {result.strftime('%Y-%m-%d %H:%M:%S')}")

        except ValueError:
            print("\nInvalid value. Check the date format or timestamp.")

        input("\nPress ENTER to continue...")


if __name__ == "__main__":
    main()
	