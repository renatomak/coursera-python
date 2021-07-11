from fizz_buzz import fizz_buzz

def test_fizz_buzz_one():
  assert fizz_buzz(1) == 1

def test_fizz_buzz_three():
  assert fizz_buzz(3) == 'Fizz'

def test_fizz_buzz_fuor():
  assert fizz_buzz(4) == 4

def test_fizz_buzz_five():
  assert fizz_buzz(5) == 'Buzz'

def test_fizz_buzz_fifteen():
  assert fizz_buzz(15) == 'FizzBuzz'