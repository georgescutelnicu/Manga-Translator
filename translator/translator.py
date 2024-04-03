from deep_translator import GoogleTranslator
from transformers import pipeline

class MangaTranslator:
    def __init__(self):
        self.target = "en"
        self.source = "ja"

    def translate(self, text, method="google"):
        """
        Translates the given text to the target language using the specified method.

        Args:
            text (str): The text to be translated.
            method (str):'google' for Google Translator, 
                         'hf' for Helsinki-NLP's opus-mt-ja-en model (HF pipeline)

        Returns:
            str: The translated text.
        """
        if method == "hf":
            return self._translate_with_hf(self._preprocess_text(text))
        elif method == "google":
          return self._translate_with_google(self._preprocess_text(text))
        else:
          raise ValueError("Invalid translation method.")
            
    def _translate_with_google(self, text):
        translator = GoogleTranslator(source=self.source, target=self.target)
        translated_text = translator.translate(text)
        return translated_text

    def _translate_with_hf(self, text):
        pipe = pipeline("translation", model=f"Helsinki-NLP/opus-mt-ja-en")
        translated_text = pipe(text)[0]["translation_text"]
        return translated_text
    
    def _preprocess_text(self, text):
        preprocessed_text = text.replace("．", ".")
        return preprocessed_text
