def Encryption(word, k):
    encrypted = ""
    for i in word:
        dec = chr(ord(i) + key)
        encrypted += dec
    return encrypted


def Decryption(word, k):
    decrypted = ""
    for i in word:
        dec = chr(ord(i) - key)
        decrypted += dec
    return decrypted


if __name__ == "__main__":
    print("Program for Shift Cipher")
    while(1):
        choice = int(input("\nEnter Your Choice:\n1.Encryption\n2.Decryption\n"))
        if choice == 1:
            plain_text = input("Enter the plain text: ")
            key = int(input("Key: "))
            result = Encryption(plain_text, key)
            print(result)

        elif choice == 2:
            plain_text = input("Enter the cipher text: ")
            key = int(input("Key: "))
            result = Decryption(plain_text, key)
            print(result)

        else:
            exit
