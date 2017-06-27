import time

hrs = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve"]
mins = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fiveteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty", "thirty", "fourty", "fifty"]
hrs.extend(hrs)

def clock(in_time):
    out_time = "It's "
    out_time += hrs[int(in_time[:2])-1] + " "

    if int(in_time[3:]) % 10 == 0 and in_time[3:] != "00":
        out_time += mins[17 + int(in_time[3])] + " "
    elif int(in_time[3:]) % 10 != 0 and int(in_time[3:]) > 0:
        out_time += "oh "
        if int(in_time[3]) > 1:
            out_time += mins[17 + int(in_time[3])] + " "
        out_time += mins[int(in_time[4:]) - 1] + " "

    out_time += "am" if int(in_time[:2]) < 12 else "pm"

    return out_time


def main():
    start_time = time.time()

    print("Enter a time:")
    print(clock(input()))

    print("\nExecution time: %s seconds" % (time.time() - start_time))

if __name__ == "__main__":
    main()