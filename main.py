def count_vowels(s):
    vowels = 'аеиоуыэюяАЕИОУЫЭЮЯ'
    count = 0
    for letter in s:
        if letter in vowels:
            count += 1
    return count