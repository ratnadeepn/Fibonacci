def fibonacci(val):
    if val<=0:
        return None

    elif val==1 or val==2:
        return 1

    else:
        fib = {}
        fib = {0: 0, 1: 1}
        for i in range(2, val + 1):
            if i not in fib:
                fib[i] = (fib[i - 1] + fib[i - 2])
        return fib[val]

class CalcClass(object):

    def __init__(self, val):
        self.value = val

    def calculate(self):
        result= fibonacci(int(self.value))
        #print(result)
        return result

