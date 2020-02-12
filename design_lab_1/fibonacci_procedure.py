def fib(n):
    if n == 0 or n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


def test_fib(user_inputs, expected_outputs):
    actual_outputs = []
    for user_input in user_inputs:
        actual_outputs.append(fib(user_input))

    if expected_outputs == actual_outputs:
        print("SUCCESS")
        return
    print("FAILURE")


if __name__ == '__main__':
    user_inputs = [0, 1, 2, 3, 4, 5]
    expected_outputs = [1, 1, 2, 3, 5, 8]
    test_fib(user_inputs, expected_outputs)
