def main():
    # breakfast = list(range(7, 8))
    # lunch = list(range(12, 13))
    # dinner = list(range(18, 19))
    converted_time = convert(input("Time?(##:##): ").strip())
    if converted_time >= 7 and converted_time <= 8:
        print("breakfast time")
    elif converted_time >= 12 and converted_time <= 13:
        print("lunch time")
    elif converted_time >= 18 and converted_time <= 19:
        print("dinner time")
    else:
        return 1


def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)
    if hours < 24 and hours >= 0:
        hours
    else:
        return print("incorrect time format")
    if minutes < 60 and minutes >= 0:
        minutes
    else:
        return print("incorrect time format")
    return hours + (minutes / 60)


if __name__ == "__main__":
    main()
