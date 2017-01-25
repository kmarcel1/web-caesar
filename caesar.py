
def alphabet_position(letter, number):
    if len(letter) != 1:
        return -1 #Invalid input
    elif letter.isalpha() == False:
        return letter #If its not an alphabet
    else:
        ans = ord(letter) + number
        # the below if-statement makes sure the value does not overflow.
        if ans > ord('z') and letter.islower():
            ans = ans - ord('z') + ord('a')
        elif ans > ord('Z') and letter.isupper():
            ans = ans - ord('Z') + ord('A')
        return chr(ans)



def rotate(chaf, rot):
    shift = 97 if letter.islower() else 65
    return chr((ord(char) + rot - shift) % 26 + shift)


def encrypt(message, rot):
    key = 'abcdefghijklmnopqrstuvwxyz'
    result = ''

    for l in message.lower():
        try:
            i = (key.index(l) + rot) % 26
            result += key[i]
        except ValueError:
            result += l

    return result.lower()
