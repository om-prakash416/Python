def count_character_occurrences(input_string):
    char_count={}
    
    for char in input_string:
    
        if char in char_count:
            char_count[char]+=1
        
        else:
            char_count[char] = 1
        
    return char_count

input_string = input("Enter a string: ")

char_count = count_character_occurrences(input_string)

for char ,count in char_count.items():
    print(f"'{char}':{count}")