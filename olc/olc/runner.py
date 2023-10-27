import sys
import json
import requests


class OlcRunner():

    host = "http://localhost:8888"  # TODO: get from env
    model = "llama2"  # TODO: get from env

    endpoint_generate = "api/generate"

    def run(self):
        prompt = self._getPrompt()

        if not self._is_ollama_running():
            raise RuntimeError(f"Ollama is not running at expected address {self.host}")

        print(self._generate(prompt))

    def _generate(self, prompt: str) -> str:

        request_body = {
            "model": self.model,
            "prompt": prompt
        }

        try:
            request_json = json.dumps(request_body)
            result = requests.post(f"{self.host}/{self.endpoint_generate}", data=request_json)
            if result.status_code != 200:
                raise RuntimeError(f"Unexpected status code: {result.status_code} - {result.text}")

            as_array = result.text.replace("}\n{", "},\n{")
            result_json: dict = json.loads(f"[{as_array}]")

            response = ""
            for item in result_json:
                response += item['response']

            return response
        except Exception as ex:
            raise RuntimeError(ex)

    def _getPrompt(self) -> str:
        if (len(sys.argv) == 1):
            raise AttributeError("No prompt argument was given.")

        return sys.argv[1]

    def _is_ollama_running(self) -> bool:
        try:
            result = requests.get(f"{self.host}/")
            return result.status_code == 200
        except Exception as ex:
            print(ex)
            return False
