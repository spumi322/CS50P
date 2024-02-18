months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
         ]

# def main():
#     date = get_date(input("Date: "))
#     print(date[0], date[1], date[2])

# def get_date(prompt):
#     while True:
#         try:
#             d = input(prompt)
#             if "/" in d:
#                 split = d.split("/")
#                 m = split[0]
#                 d = split[1]
#                 y = split[2]
#             if "," in d:
#                 mdy = d.split(",")
#                 md = mdy[0]
#                 y = mdy[1].strip()
#                 a = md.split(",")
#                 m = a[0]
#                 d = a[1]
#                 if m in months:
#                     return months.index(m + 1)
#                 else:
#                     raise NameError
#             return [y, m, d]
#         except NameError:
#             pass

# main()

def main():
    while True:
        date = input("Date: ").strip()
        try:
            if "/" in date:
                m, d, y = date.split("/")
                if (int(m) >= 1 and int(m) <= 12) and (int(d) >= 1 and int(d) <= 31):
                    break
            elif "," in date:
                date = date.replace(",", "")
                m, d, y = date.split(" ")
                if int(d) > 31 or int(d) < 1:
                    raise ValueError
                if m in months:
                    m = months.index(m) + 1
                    break
            else:
                raise ValueError
        except ValueError:
            pass
    print(y + "-" + f"{int(m):02}" + "-" + f"{int(d):02}")


main()



