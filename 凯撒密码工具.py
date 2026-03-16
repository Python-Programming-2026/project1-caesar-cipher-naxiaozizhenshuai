def caesar_encrypt(text, shift):
    result = ""
    shift = shift % 26
    for char in text:
       if char.isupper():
            new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            result += new_char
       elif char.islower():
            new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            result += new_char
       else:
            result += char
    return result
def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)
print("凯撒密码工具")
print("1.加密")
print("2.解密")
print("3.穷举法破解凯撒密码")
choice=int(input("选择："))
if(choice==1):
    text=input("明文：")
    shift=int(input("密匙："))
    print("密文：",caesar_encrypt(text, shift))
if(choice==2):
    text=input("密文：")
    shift=int(input("密匙："))
    print("明文：",caesar_decrypt(text, shift))
if(choice==3):
    text=input("密文：")
    for shift in range(1,26):
        print("当密钥是：时",shift,"明文：",caesar_decrypt(text, shift))
