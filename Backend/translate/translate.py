from googletrans import Translator

def TextTranslator(text):
    translator = Translator()
    
    if(text == list):
        translated = []
        for t in text:
            translated.append(translator.translate(t).text)
        return translated

    translated = translator.translate(text)
    return translated.text