import fileinput

#Matriz caracter y regrese indices ( tupla )
def getIndex(Alphabet, message_char):
    for i in range(0, len(Alphabet)):
        for j in range(0, len(Alphabet[0])):
            #print(Alphabet[i][j])
            if Alphabet[i][j] == message_char:
                tupla = (i, j)
                return tupla
    
#Decrypt

def main():
    #Matrix given
    Alphabet = [['E', 'N', 'C','R','Y'], ['P', 'T', 'A', 'B', 'D'], ['F', 'G', 'H', 'I', 'K'], ['L', 'M', 'O', 'Q', 'S'], ['U', 'V', 'W', 'X', 'Z']]
    #Read and get string without spaces
    lines = []
    for line in fileinput.input():
        #print(line)
        lines.append(line.rstrip())
    message = lines[1]

    if " " in message:
        for line in message:
            lines.append(line)
            message = lines[1]
            message = message.replace(" ", "")
            message1 = message.split(',')
            array_elements1 = []
            array_elements2 = []

        for element in message1[0]:
            tupla = getIndex(Alphabet, element)
            array_elements1.append(tupla[0])
            array_elements2.append(tupla[1])

        array_elements = array_elements1 + array_elements2
            
        s = ""
        for i in range(len(message)):
            n = i * 2
            s += (Alphabet[array_elements[n]][array_elements[n+1]])

        print(s)
    else:
        for line in message:
            lines.append(line)
            message = lines[1]
            message1 = message.split(',')
            array_elements = []
 

        for element in message1[0]:
            tupla = getIndex(Alphabet, element)
            array_elements.append(tupla[0])
            array_elements.append(tupla[1])

        s = ""
        for i in range(len(message)):
            s += (Alphabet[array_elements[i]][array_elements[i + int(len(message))]])

        print(s)

  
if __name__ == '__main__':
    main()
