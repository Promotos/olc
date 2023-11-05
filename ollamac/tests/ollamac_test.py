
from ollamac.ollamac import OlcRunner

def test_defaults():
    runner = OlcRunner()
    assert runner.host == "localhost"
    assert runner.port == 8888
    assert runner.model == "llama2"
    
def test_get_endpoint():
    runner = OlcRunner()
    assert runner._get_endpoint() == "http://localhost:8888"