from googletrans import Translator


def IrisTranslate(input,lang):
    translator = Translator()
    if (lang='detect'):
        lang=translator.detect(input)
    return translator.translate(input,dest='en',src=lang)
