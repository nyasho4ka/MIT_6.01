from state_machines import ABC, Gain, Accumulator, UpDown


def main():
    # Accumulator testing

    acc_one = Accumulator()
    acc_one_inputs = [100, 20, -20, -30, 6, 7]
    acc_one_expected_output = [100, 120, 100, 70, 76, 83]

    acc_two = Accumulator(10)
    acc_two_inputs = [20, 30, 40, -70, -100, 80]
    acc_two_expected_output = [30, 60, 100, 30, -70, 10]

    test_accumulator([acc_one, acc_two],
                     [acc_one_inputs, acc_two_inputs],
                     [acc_one_expected_output, acc_two_expected_output])

    # Gain testing

    gain_one = Gain(5)
    gain_one_inputs = [1, 2, 3, 4, 5, 6]
    gain_one_output = [5, 10, 15, 20, 25, 30]

    gain_two = Gain(0)
    gain_two_inputs = [1, 2, 3, 4, 5, 6]
    gain_two_output = [0, 0, 0, 0, 0, 0]

    gain_three = Gain(-3)
    gain_three_inputs = [1, 5, 1, 3, 3, 8]
    gain_three_output = [-3, -15, -3, -9, -9, -24]

    test_gain([gain_one, gain_two, gain_three],
              [gain_one_inputs, gain_two_inputs, gain_three_inputs],
              [gain_one_output, gain_two_output, gain_three_output])

    # ABC testing

    abc_one = ABC()
    abc_one_inputs = ['a', 'b', 'c', 'a', 'b', 'c', 'b', 'a', 'c']
    abc_one_output = [True, True, True, True, True, True, False, False, False]

    abc_two = ABC()
    abc_two_inputs = ['a', 'a', 'b', 'a', 'b', 'c']
    abc_two_output = [True, False, False, False, False, False]

    test_abc([abc_one, abc_two],
             [abc_one_inputs, abc_two_inputs],
             [abc_one_output, abc_two_output])

    # UpDown testing

    updown_one = UpDown('word')
    updown_one_inputs = ['word', 'no_word', 'no word', 'word', 'word', 'word']
    updown_one_output = [1, 0, -1, 0, 1, 2]

    updown_two = UpDown('hero')
    updown_two_inputs = ['villain', 'thanos', 'hero', 'hero', 'hero']
    updown_two_output = [-1, -2, -1, 0, 1]

    test_updown([updown_one, updown_two],
                [updown_one_inputs, updown_two_inputs],
                [updown_one_output, updown_two_output])


def test_accumulator(accumulators, inputs, expected_outputs):
    test_state_machines(accumulators, inputs, expected_outputs)


def test_gain(gains, inputs, expected_outputs):
    test_state_machines(gains, inputs, expected_outputs)


def test_abc(abc, inputs, expected_outputs):
    test_state_machines(abc, inputs, expected_outputs)


def test_updown(updowns, inputs, expected_outputs):
    test_state_machines(updowns, inputs, expected_outputs)


def test_state_machines(state_machines, inputs, expected_outputs):
    for i in range(len(state_machines)):
        test_state_machine(state_machines[i], inputs[i], expected_outputs[i])


def test_state_machine(state_machine, input, expected_output):
    state_machine.start()
    actual_output = state_machine.transduce(input)
    if actual_output == expected_output:
        print("Test passed!")
        return
    print("Test failed!")
    print(f"State machine class is {state_machine.__class__.__name__}"
          f"\nInput: {input}"
          f"\nExpected output: {expected_output}"
          f"\nActual output: {actual_output}")


if __name__ == '__main__':
    main()
