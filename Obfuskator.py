from main import main
import  string


class Obfuskator:
    def __init__(self):
        pass

    @staticmethod
    def obfuscate(file):
        try:
            code = open(file, 'r', encoding="utf-8").read()

        except Exception as e:
            return e, False

        obfuscatedCode = main(code)

        return obfuscatedCode


result = Obfuskator.obfuscate("test.py")
open("result.py", "w", encoding='utf8').write(result)
