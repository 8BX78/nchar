# how many n_char_words in string
def n_word_in_str(str, n):
    num_n_words = 0
    words = str.split()
    for word in words:
        #print("word is:",word, len(word))
        if len(word) == n:
            #print("found",n,"char word:",word,"\n")
            num_n_words += 1
            
    return (num_n_words)
    
str = input("Enter a string: ")
#num = int(input("Enter a number: "))
for n in range (1,21):
    n_char_word = (n_word_in_str(str,n))
    if n_char_word != 0:
        print("number of",n,"char word is:",n_char_word)
        