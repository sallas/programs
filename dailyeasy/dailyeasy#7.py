morsecode = '.... . .-.. .-.. --- / -.. .- .. .-.. -.-- / .--. .-. --- --. .-. .- -- -- . .-. / --. --- --- -.. / .-.. ..- -.-. -.- / --- -. / - .... . / -.-. .... .- .-.. .-.. . -. --. . ... / - --- -.. .- -.--'
morsedict =  { "/" : " ", ".-": 'A',"-...": 'B',  "-.-.": 'C',  "-..": 'D',  ".": 'E',  "..-.": 'F',  "--.": 'G',  "....": 'H',  "..": 'I',  ".---": 'J',  "-.-": 'K',  ".-..": 'L',  "--": 'M',  "-.": 'N',  "---": 'O',  ".--.": 'P',  "--.-": 'Q',  ".-.": 'R',  "...": 'S',  "-": 'T',  "..-": 'U',  "...-": 'V',  ".--": 'W',  "-..-": 'X',  "-.--": 'Y',  "--.-": 'Z' }
sentance = ""
for word in morsecode.split(' '):
    sentance += morsedict[word]
print sentance
print "now for the other way around"
sentance = ""
for i in "HELLO DAILY PROGRAMMER GOOD LUCK ON THE CHALLENGES TODAY":
    for morse, alpha in morsedict.iteritems():
        if alpha == i:
            sentance += morse
    sentance += ' '
print sentance
