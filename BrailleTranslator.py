# This is a level 1 challenge from Google foobar
# Braille translator which can handle less than 50 characters
# The translator can only translate alphabets, spaces and capitalization

braille_translator = {
    "a": "100000",
    "b": "110000",
    "c": "100100",
    "d": "100110",
    "e": "100010",
    "f": "110100",
    "g": "110110",
    "h": "110010",
    "i": "010100",
    "j": "010110",
    "k": "101000",
    "l": "111000",
    "m": "101100",
    "n": "101110",
    "o": "101010",
    "p": "111100",
    "q": "111110",
    "r": "111010",
    "s": "011100",
    "t": "011110",
    "u": "101001",
    "v": "111001",
    "w": "010111",
    "x": "101101",
    "y": "101111",
    "z": "101011",
    "capital": "000001",
    " ": "000000"
}


def is_validate_text(text):
    if len(text) < 50:
        for i in text:
            if i.isalpha() or i. isspace():
                continue
            else:
                return False
    else:
        return False
    return True


def solution(text):
    if is_validate_text(text):
        output = ""
        for character in text:
            if character.isupper():
                output += braille_translator.get("capital")
            output += braille_translator.get(character.lower())
        return output
    else:
        return False


input1 = input("Input: ")
print("Output: ")
print(solution(input1))
