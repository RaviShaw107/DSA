character = input("enter a character:: ")
vowel = ['a', 'e', 'i', 'o', 'u'] # list

if character in vowel:
    print("'"+character+"' is a vowel")
else:
    print("'"+character+"' is a consonent")