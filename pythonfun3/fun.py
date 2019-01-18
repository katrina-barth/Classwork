
def main():

    add_two(3,5)
    sub_two(6,4)
    bat = mult_two(5,5)
    bat2 = avg_three(1,3,7)
    print('This is the output of mult_two of 5 and 5: {}'.format(bat))
    print('This is the output of avg_three of 1,3 and 7: {}'.format(bat2))

    """Colon defines start of new block"""
    """Put a colon after a function to set the upcoming block"""

def add_two(v1,v2):
    p = v1+v2
    print(p)

    """
    parameter v1: number 1
    parameter v2: number 2
    returns: result
    """

def sub_two(v1,v2):
    p = v1-v2
    print(p)

def mult_two(v1,v2):
    p = v1 * v2
    return p

def div_two(v1,v2):
    p = v1/v2
    return p

def avg_three(v1,v2,v3):
    p = (v1 + v2 + v3)/3
    return p

if __name__ == "__main__" :
    main()
