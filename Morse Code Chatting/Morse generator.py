Morse_code = {
                    'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-'
} 
def encrypt(Message):
    code = ""
    for symbol in Message:
        if symbol == " ":
            code=code+" "
        else:
            code=code+Morse_code[symbol.upper()]+" "
    return code

def decrypt(code , key):
    attempt=0
    while attempt != 3:
        key  = input("Enter you decryption key = ")
        if key == "12345":
            code  = code.split("  ")
            message = ""
            for word  in code:
                for symbol in word.split(" "):
                    if symbol == "":
                        continue
                    letter = list(Morse_code.keys())[list(Morse_code.values()).index(symbol)]
                    message = message+letter
                message = message+" "
            return message
        elif attempt !=2:
            print("Wrong key Entered Try again ")
        attempt +=1
    return "You Overattempted" 

message = input("Enter any text : ")
code = encrypt(message)
print(code)
print(decrypt(code, "12345"))


    