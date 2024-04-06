from googletrans import Translator


def translate_text(text, target="es"):
    translator = Translator()
    translated = translator.translate(text, dest=target)
    return translated.text


text = input("Translate something here: ")
res = translate_text(text)
print("Translated:", res)

file_object = open('Translated.txt', 'w')
file_object.write((res))
