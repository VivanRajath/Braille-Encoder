

def text_to_braille(text: str) -> str:
    braille_map = {
        "a":"⠁","b":"⠃","c":"⠉","d":"⠙","e":"⠑","f":"⠋","g":"⠛","h":"⠓",
        "i":"⠊","j":"⠚","k":"⠅","l":"⠇","m":"⠍","n":"⠝","o":"⠕","p":"⠏",
        "q":"⠟","r":"⠗","s":"⠎","t":"⠞","u":"⠥","v":"⠧","w":"⠺","x":"⠭",
        "y":"⠽","z":"⠵"," ":" "
    }
    return "".join(braille_map.get(ch.lower(), ch) for ch in text)
