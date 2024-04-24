def reverse(string):

    if len(string) <= 1:
        return string
    else:
        return reverse(string[1:]) + string[0]


original_string = "Waleed Chaudhry"
reversed_string = reverse(original_string)
print(reversed_string)
