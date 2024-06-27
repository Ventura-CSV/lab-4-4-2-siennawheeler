def main():
    """
    ########################################
    Code Your Program here
    ########################################
    """
    x = 0
    while x < 1:
        try: 
            number = int(input())
        except ValueError:
            print('Input must be numeric')
        else:
            print(number)
            x = x + 1

    ########################################
    # Do not delete the return statement
    ########################################
    return number


if __name__ == '__main__':
    main()
