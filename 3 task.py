def lowAndUpper(function):
    def wrapper():
        func = function()
        swap = func.swapcase()
        return swap
    return wrapper


@lowAndUpper
def word():
    word = input("Input: ")
    return word

print(word())
