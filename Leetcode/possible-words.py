


def solution(text, letters):
    
    s = set(letters)
    
    result = 0
    
    words = text.split()
    
    for word in words:
        
        possible = True
        
        for character in word:
            if character.lower() not in s and character.isalpha():
                possible = False
                
        if possible:
            result += 1
            
    return result

print(solution(text = "Hello, this is CodeSignal!", letters = ["e", 
 "i", 
 "h", 
 "l", 
 "o", 
 "s"]))