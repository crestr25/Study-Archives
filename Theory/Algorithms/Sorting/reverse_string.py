def reverse_string(string):

    if len(string) == 1:
        return string
    
    return reverse_string(string[1:]) + string[0]



if __name__ == "__main__":
    print(reverse_string("Hello World!"))
