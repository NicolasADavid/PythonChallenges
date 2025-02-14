'''
You're working on the UI for the text messaging app for a phone. In a message notification, there is limited space, so the entire message cannot be shown, so the app designer wants to show a truncated form of the message in the space allotted.

The message will be words separated by spaces. Don't worry about punctuation or other special characters. Consider any series of characters other than spaces as a word.

Given an input text message (string) and a maximum number of characters (integer), return the truncated string.

The rules for truncation are as follows:
- If the string must be truncated, it must be indicated as such with an elipsis, three periods.
- If there is a word before the '...' then there must also be a space.
- Including the truncation indicator, the resulting string must be less than the provided maximum number of characters.
- Truncation can only happen on word boundaries (mustn't include partial words)
- If the whole string fits in the allotted space, no truncation is necessary, just return the original string.
 

EXAMPLE(S)
truncate_message("This is a test message", 8) == 'This ...'
truncate_message("This is a test message", 11) == 'This is ...'
truncate_message("This is a test message", 15) == 'This is a ...'
truncate_message("This is a test message", 20) == 'This is a test ...'
truncate_message("This is a test message", 25) == 'This is a test message'
 

FUNCTION SIGNATURE
function truncate_message(message, threshold) {
def truncate_message(message: str, threshold: int) -> str:
'''


def truncate_message(message: str, threshold: int) -> str:

    # Option 1:
    # Split the message into words

    # Option 2:
    # Find the index where truncation should start, search left until space or beginning of string

    if len(message) <= threshold:
        return message
    
    result = ""

    words = message.split(" ")

    for word in words:
        if len(word) + 4  <= threshold:
            result += word + " "
            threshold -= len(word) + 1
        else:
            result += "..."
            break

    return result
    

print(truncate_message("", 3) == '')
print(truncate_message("ab", 3) == 'ab')
print(truncate_message("abc", 3) == 'abc')
print(truncate_message("abc", 4) == 'abc')
print(truncate_message("abcd", 4) == 'abcd')
print(truncate_message("abcd", 3) == '...')
print(truncate_message("Hello", 4) == '...')
print(truncate_message("Hello", 5) == 'Hello')
print(truncate_message("Hello Cat", 8) == '...')
print(truncate_message("Hello Cat", 9) == 'Hello Cat')
print(truncate_message("Hello Cat", 5) == '...')
print(truncate_message("Hello Rufus", 9) == 'Hello ...')
print(truncate_message("Hello Rufus", 11) == 'Hello Rufus')
print(truncate_message("Hello Rufus", 12) == 'Hello Rufus')

print(truncate_message("This is a test message", 3) == '...')
print(truncate_message("This is a test message", 7) == '...')
print(truncate_message("This is a test message", 8) == 'This ...')
print(truncate_message("This is a test message", 10) == 'This ...')
print(truncate_message("This is a test message", 11) == 'This is ...')
print(truncate_message("This is a test message", 15) == 'This is a ...')
print(truncate_message("This is a test message", 20) == 'This is a test ...')
print(truncate_message("This is a test message", 25) == 'This is a test message')