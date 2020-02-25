class SM:
    startState = 0

    def start(self):
        self.state = self.startState

    def step(self, inp):
        nextState, output = self.getNextValues(self.state, inp)
        self.state = nextState
        return output

    def transduce(self, inputs):
        self.start()
        return [self.step(inp) for inp in inputs]

    def run(self, n=10):
        return self.transduce([None] * n)

    def getNextValues(self, state, inp):
        nextState = self.getNextState(state, inp)
        return nextState, nextState

    def getNextState(self, state, inp):
        raise NotImplementedError


class Accumulator(SM):
    def __init__(self, initialValue=0):
        self.startState = initialValue

    def getNextState(self, state, inp):
        return state + inp


class Gain(SM):
    def __init__(self, factor):
        self.factor = factor

    def getNextState(self, state, inp):
        return self.factor * inp


class ABC(SM):
    def getNextValues(self, state, inp):
        if state == 0 and inp == 'a':
            return 1, True
        elif state == 1 and inp == 'b':
            return 2, True
        elif state == 2 and inp == 'c':
            return 0, True
        else:
            return 3, False


class UpDown(SM):
    def __init__(self, up):
        self.up = up

    def getNextState(self, state, inp):
        if inp == self.up:
            return state + 1
        return state - 1


class Delay(SM):
    def __init__(self, v0):
        self.startState = v0

    def getNextValues(self, state, inp):
        return inp, state


class Average2(SM):
    def getNextValues(self, state, inp):
        return inp, (inp + state) / 2


class SumLast3(SM):
    startState = (0, 0)

    def getNextValues(self, state, inp):
        previousFirstInput, previousSecondInput = state
        return (previousSecondInput, inp), previousFirstInput + previousSecondInput + inp


class Select(SM):
    def __init__(self, k):
        self.k = k

    def getNextState(self, state, inp):
        return inp[self.k]
