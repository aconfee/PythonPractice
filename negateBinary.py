import math


def negateBinary(binaryCharArray):
    # Flip each bit
    for i in range(len(binaryCharArray)):
        binaryCharArray[i] = '0' if binaryCharArray[i] == '1' else '1'

    # Add one
    for i in reversed(range(len(binaryCharArray))):
        if binaryCharArray[i] == '1':
            binaryCharArray[i] = '0'
        else:
            binaryCharArray[i] = '1'
            break

    return binaryCharArray


def negateBinaryFast(binaryCharArray):
    performAdd = True
    for i in reversed(range(len(binaryCharArray))):
        # Flip each bit
        binaryCharArray[i] = '0' if binaryCharArray[i] == '1' else '1'

        # Add one
        if binaryCharArray[i] == '1' and performAdd:
            binaryCharArray[i] = '0'
        elif binaryCharArray[i] == '0' and performAdd:
            binaryCharArray[i] = '1'
            performAdd = False

    return binaryCharArray
