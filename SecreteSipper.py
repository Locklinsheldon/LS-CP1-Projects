#Locklin Sheldon, ProficiencyTest: Secret Cypher


def secrete_sipper(text):
    return "".join(chr(ord(char) + 9) if char.isalpha() else char for char in text)


def desipper_sipper(text):
    return "".join(chr(ord(char) - 9) if char.isalpha() else char for char in text)


user_input = input("Enter a stringybalingy to mumblejumble: ")
enc_mess = secrete_sipper(user_input)
print("Jumbled mess:", enc_mess)


print("Your original input was:", user_input)


enc_in = input("Enter an encrypted string to decode: ")
dec_mess = desipper_sipper(enc_in)
print("Decody message:", dec_mess)

