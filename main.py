from randomchar import *
import re
import base64


def variableRenamer(code):
    code = "\n" + code
    variables = re.findall(varRegex, code)
    for i in range(len(variables)):
        var = variables[i].strip("=").strip()
        randomName = randomNameGenerator(var)
        code = re.sub(varReplaceRegex.format(var), randomName, code)

    return code


def functionRenamer(code):
    funcs = re.findall(funcRegex, code)
    for i in range(len(funcs)):
        randomName = randomNameGenerator(funcs[i])

        code = re.sub(funcReplaceRegex.format(funcs[i]), randomName, code)

    return code


def classRenamer(code):
    classes = re.findall(classRegex, code)
    for i in range(len(classes)):
        randomName = randomNameGenerator(classes[i])
        code = re.sub(classReplaceRegex.format(classes[i]), randomName, code)

    return code


def addRandomChineseVars(code, j):
    code = chineseVars(30, j) + j + code

    code = code + j + chineseVars(30, j)

    return code


def b64Encode(code):
    encodedCode = base64.b64encode(code.encode())
    fullCode = f"exec(__import__('base64').b64decode({encodedCode}))"
    return fullCode


def main(code):
    methods = [variableRenamer, functionRenamer, classRenamer, b64Encode]
    for method in methods:
        code = method(code)

    code = addRandomChineseVars(code, "\n")
    code = b64Encode(code)
    code = addRandomChineseVars(code, ";")

    return code
