# тестовое 1
from pypred import Predicate
import math
import requests

url = 'https://api.weatherbit.io/v2.0/current'
lang = '&lang=en'
key = '&key=1868c44aa0624c1888883e9307fbfba2'
endpoints = '?city=Moscow&country=Russia'

response = requests.get(f"{url}{endpoints}{key}{lang}").json()

temperature = response['data'][0]["app_temp"]
description = response['data'][0]['weather']['description']

print(f"{temperature}, {description}")

# # тестовое 2


def sumFactorials(n):
    sum = 0
    for i in range(5, n + 1):
        factorial = math.factorial(i)
        sum += factorial
    return (sum)


result = sumFactorials(7)
print(result)

# тестовое 2: другой способ


def calculateStartFactorial(n):
  # вычисляем факториал числа, от которого начнется отсчёт
    factorial = 1
    while n > 1:
        factorial *= n
        n -= 1
    return factorial


def sumAnotherFactorials(n):
    factorial = calculateStartFactorial(4)
    sum = 0
    for i in range(5, n + 1):
        factorial *= i
        sum += factorial
    return sum


result = sumAnotherFactorials(7)
print(result)

# тестовое 3

mans = [{
        "comment": "нам надо заказать пиццу заказать пиццу, потому что курьер её не довез",
        "country": "Belarus",
        "city": "Minsk"
        }, {
        "comment": " ",
        "country": "Belarus",
        "city": "Grodno"
        }]
str = "country is 'Belarus' and city is 'Minsk' and comment contains 'заказать пиццу'"


def testIsFromMinsk(str, mans):
    isFromMinsk = Predicate(str)

    for i in mans:
        res = isFromMinsk.evaluate(i)
        if res:
            print('Заказать пиццу можно на сайте «pizzatempo.by»')
        else:
            print('Надо переехать')


testIsFromMinsk(str, mans)

# тестовое 4

regularExpression = "comment matches '(?i)(\W|^)(не\s{0,3}отдал|не\s{0,3}прив[её]з|не\s{0,3}дов[её]з|не\s{0,3}вез[её]т|заказ\s{0,3}потерян|заказ\s{0,3}не\s{0,3}доехал)(\W|$)'"


def testIsPizzaHere(regularExpression, mans):
    isPizzaHere = Predicate(regularExpression)

    for i in mans:
        res = isPizzaHere.evaluate(i)
        if res:
            print('Простите, что огорчили')
        else:
            print('Приятного аппетита')


testIsPizzaHere(regularExpression, mans)
