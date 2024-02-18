gl = {}

def main():
    while True:
        try:
            item = input().upper()
            if item in gl:
                gl[item] += 1
            else:
                gl[item] = 1
        except EOFError:
            break

    sl = sorted(gl.items())
    for key,value in sl:
        print(value, key)


main()