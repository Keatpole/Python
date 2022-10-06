import timeit

def check_prime(num):
    """Check if num is a prime number"""
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

prime_numbers = []

def check(verbose=False):
    for i in range(2, 100000):
        if verbose:
            print(i)
        if check_prime(i):
            prime_numbers.append(i)
        
if __name__ == "__main__":
    time_not_verbose = timeit.timeit("check(verbose=False)", setup="from __main__ import check", number=1)

    prime_numbers = []

    time_verbose = timeit.timeit("check(verbose=True)", setup="from __main__ import check", number=1)

    with open('prime_numbers.txt', 'w') as f:
        for i in prime_numbers:
            f.write(str(i) + '\n')
        
        f.write("\nTime with verbose: {}\n".format(time_verbose))
        f.write("Time without verbose: {}\n".format(time_not_verbose))