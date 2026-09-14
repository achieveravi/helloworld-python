class BasicMath:
    def add(*args):
        result = 0
        for num in args:
            result += num
        return result

    def multiply(*args):
        result = 1
        for num in args:
            result *= num
        return result