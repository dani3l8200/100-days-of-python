for fizz_buzz_game in range(0, 101):
    if fizz_buzz_game % 3 == 0 and fizz_buzz_game % 5 == 0:
        print('FizzBuzz')
    elif fizz_buzz_game % 3 == 0:
        print('Fizz')
    elif fizz_buzz_game % 5 == 0:
        print('Buzz')
    else:
        print(fizz_buzz_game)