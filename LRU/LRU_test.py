from LRU import LRU


def main():

    # initializing with size 3
    test_cache = LRU(3)

    # testing with various values
    test_cache.find(1)
    test_cache.find(2)
    test_cache.find(3)
    test_cache.find(4)
    test_cache.find(1)
    test_cache.find(3)

    # printing the cache after final transaction
    test_cache.print_cache()


if __name__ == '__main__':
    main()
