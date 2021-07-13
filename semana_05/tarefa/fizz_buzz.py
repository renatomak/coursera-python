def fizzbuzz(number):
  is_divisible_by_three = number % 3 == 0
  is_divisible_by_five = number % 5 == 0

  if (is_divisible_by_three and is_divisible_by_five):
    return 'FizzBuzz'
  else:
    if is_divisible_by_three:
      return 'Fizz'
    elif is_divisible_by_five:
      return 'Buzz'
    else:
      return number
