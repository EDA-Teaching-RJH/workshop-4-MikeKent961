def main():
    camelInput = input("Write camel case variable name here: ")
    snakeOutput = camelToSnake(camelInput)
    print(snakeOutput)


def camelToSnake(varName):
    for i in varName:
        if i.isupper() == True:
            varName = varName.replace(i, "_" + i.lower())

    return varName

main()