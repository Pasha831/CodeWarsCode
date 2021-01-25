def generate_hashtag(s: str):
    output = '#'

    for word in s.split():
        output += word.capitalize()
    
    if s == '' or len(output) > 140:
        return False
    else:
        return output 

print(generate_hashtag(''))