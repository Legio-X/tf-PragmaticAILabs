from random import choices


def fruit():
    fruits = ["apple", "orange", "pear"]
    return choices(fruits)[0]
