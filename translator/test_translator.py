import pytest
from translator import MangaTranslator


@pytest.fixture
def translator():
    return MangaTranslator()


def test_translate_with_google(translator):
    ja_text = "こんばんは！"
    en_translation = "Good evening!"
    translated_text = translator.translate(ja_text, method="google")
    assert translated_text == en_translation


def test_translate_with_hf(translator):
    ja_text = "こんばんは！"
    en_translation = "Good evening!"
    translated_text = translator.translate(ja_text, method="hf")
    assert translated_text == en_translation


def test_invalid_translation_method(translator):
    ja_text = "こんばんは！"

    try:
        translator.translate(ja_text, method="Mirai")
    except ValueError as e:
        assert str(e) == "Invalid translation method."
    else:
        assert False, "No exception was raised."
