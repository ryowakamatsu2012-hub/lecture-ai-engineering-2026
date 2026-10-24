import io
from contextlib import redirect_stdout

from app import ask as ask_module


class DummyUsageMetadata:
    prompt_token_count = 123
    candidates_token_count = 45


class DummyResponse:
    text = "hello from model"
    usage_metadata = DummyUsageMetadata()


class DummyClient:
    def __init__(self, api_key):
        self.api_key = api_key

    @property
    def models(self):
        return self

    def generate_content(self, model, contents):
        assert model == ask_module.MODEL
        assert contents == "hello"
        return DummyResponse()


def test_ask_prints_input_and_output_tokens(monkeypatch):
    monkeypatch.setattr(ask_module, "get_api_key", lambda: "test-key")
    monkeypatch.setattr(ask_module.genai, "Client", DummyClient)

    stdout = io.StringIO()
    with redirect_stdout(stdout):
        result = ask_module.ask("hello")

    assert result == "hello from model"
    output = stdout.getvalue()
    assert "[input tokens] 123" in output
    assert "[output tokens] 45" in output
