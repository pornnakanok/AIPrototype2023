import argparse

def parse_input():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--num',
        type=int,
        required=True,
        help='Input for the multiplyby9 function'
    )
    args = parser.parse_args()
    return args

def printHello():
    print('Hello world!')

def multiplyby9(inputV):
    print(9*inputV)

if __name__ == "__main__":
    input_v = parse_input()
    print(f'the input num is {input_v.num}')
    print('You are in the main function')
    multiplyby9(20)
    printHello()