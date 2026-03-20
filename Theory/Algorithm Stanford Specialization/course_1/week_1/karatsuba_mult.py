def karatsuba_mult(x: int, y: int) -> int:
    """
    Karatsuba Multiplication
    """

    if x < 10 or y < 10:
        return x * y

    # get length of numbers
    digits = max(len(str(x)), len(str(y)))
    digits_half = digits // 2
    a, b = divmod(x, 10**digits_half)
    c, d = divmod(y, 10**digits_half)

    # print(a, b, c, d)
    # step 1 - AC
    s1 = karatsuba_mult(a, c)
    # step 2 - BD
    s2 = karatsuba_mult(b, d)
    # step 3 - (A+B)(C+D)
    s3 = karatsuba_mult(a + b, c + d)
    s3 = s3 - s1 - s2    


    return (s1 * 10**(2*digits_half)) + (s3 * 10**digits_half) + (s2)
    
if __name__ == "__main__":

    x = 5678
    y = 1234

    print(karatsuba_mult(x, y))

    # 10^n/2 a + b, 10^n/2 c + d notation
