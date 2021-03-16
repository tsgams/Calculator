import operator as op

# argument must be a list of numbers and operators
# for example: expr = [1, '+', 2, '-', 3, '*', 4, '/']


def calc(A) -> float:
    # define mathematical operators
    operands = ['+', '-', '*', '/']

    operators = {  # operators['operator'](a,b)
        operands[0]: op.add,  # summation
        operands[1]: op.sub,  # subtraction
        operands[2]: op.mul,  # multiplication
        operands[3]: op.truediv  # division
    }

    i = 0
    B = []  # vector of + and - operators
    while i < (len(A) - 1) // 2:
        temp_num = A[2 * i]
        temp_op = A[2 * i + 1]

        if temp_op in operands[0:2]:  # if + and - operators we rewrite them in the B vector
            B.append(temp_num)
            B.append(temp_op)
            if i + 1 is (len(A) - 1) // 2:
                B.append(A[2 * (i + 1)])
        else:  # otherwise we calculate the sub-expressions until we have + or - operator
            while temp_op in operands[2:4]:
                if i + 1 == (len(A) - 1) // 2:  # if we are on the last number of the vector
                    temp_num = operators[temp_op](float(temp_num), float(A[2 * (i + 1)]))
                    B.append(temp_num)
                    i += 1
                    break
                temp_num = operators[temp_op](float(temp_num), float(A[2 * (i + 1)]))
                temp_op = A[2 * (i + 1) + 1]  # the next operator
                i += 1
                if temp_op in operands[0:2]:
                    B.append(temp_num)
                    B.append(temp_op)
                    if i + 1 == (len(A) - 1) // 2:  # if we are on the last number of the vector
                        B.append(A[2 * (i + 1)])
                        break
        i += 1

    result = float(B[0])
    for i in range(0, (len(B) - 1) // 2):  # sum up every number in the vector
        result = operators[B[2 * i + 1]](result, float(B[2 * (i + 1)]))

    return result

