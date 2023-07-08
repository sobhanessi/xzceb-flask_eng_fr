''' writing functionality for translating english to french and vise versa'''
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    ''' takes en text and translates it to french!'''
    french_text = MyMemoryTranslator(source="en-US", target="fr-FR").translate(english_text)
    return french_text

def french_to_english(french_text):
    ''' takes fr text and translates it to english!'''
    english_text = MyMemoryTranslator(source="fr-FR", target="en-US").translate(french_text)
    return english_text

