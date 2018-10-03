# Edit the doc and type in the message you would want to reverse below

message = 'I am learning how to program with python ' 
translatedmessage = ''

i = len(message) - 1
while i >= 0:
    translated = translated + message[i]
    i = i - 1

print(translatedmessage)
