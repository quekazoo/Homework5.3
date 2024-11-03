def to_hashtag(text):
    cleaned_text = ''.join(char for char in text if char.isalnum() or char.isspace()).split()
    capitalized_words = [word.capitalize() for word in cleaned_text]
    hashtag = '#' + ''.join(capitalized_words)
    return hashtag[:140]

user_input = input("Введіть рядок: ")
hashtag = to_hashtag(user_input)
print(hashtag)