m = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }

# def main():
#     food = get_inp("Item: ")
#     total = 0
#     while True:
#         try:
#             if food in m:
#                 total += m[food]
#                 print(total)
#                 # print("total: " + ("{:.2f}".format(total)) + "$")

# def get_inp(prompt):
#     while True:
#         try:
#             x = input(prompt)
#             x = x.title()
#             if x not in m:
#                 raise EOFError
#         except EOFError:
#             break
#         else:
#             return x

# def main():
#     while True:
#         try:
#             f = input("Item: ").title()
#             total = 0
#             if f in m:
#                 total += m[f]
#                 print("Total: " + ("{:.2f}".format(total)) + "$")
#         except EOFError:
#             print()
#             break
# main()

# def main():
#     while True:
#         try:
#             t = 0
#             f = input("Item: ").title()
#         except EOFError:
#             print
#             break
#     if f in m:
#         t += m[f]
#         print("Total: " + ("{:.2f}".format(t)) + "$")

# main()

# def main():
#     total = 0
#     while True:
#         try:
#             item = input("Item: ").title()
#         except EOFError:
#             print()
#             break
#         if item in menu:
#             total += menu[item]
#             print("Total: $", f"{total:.2f}", sep="")

# main()



def main():
    t = 0
    while True:
        try:
            f = input("Item: ").title()
        except EOFError:
            print()
            break
        if f in m:
            t += m[f]
            print("$" + ("{:.2f}".format(t)))


main()