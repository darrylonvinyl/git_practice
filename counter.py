#!/usr/bin/python3.6

def counter(start, stop):
    x = start
    if x > stop:
        return_string = "Counting down: "
        while x >= stop:
            return_string += str(x)
            if start != stop:
                return_string += ","
            x = x - 1
    return return_string

print(counter(5,1))
