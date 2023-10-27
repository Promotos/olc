import sys


class OlcRunner():

    def run(self):
        print(self._getPrompt())

    def _getPrompt(self) -> str:
        if (len(sys.argv) == 1):
            raise AttributeError("No prompt argument was given.")

        return sys.argv[1]
