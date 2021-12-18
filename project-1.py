my_list =[
                    "The Wildlife of Southern Africa",
                    "Discover African Wildlife: Activity Book",
                    "African Wildlife Coloring Book",
                    "Make It Count - Africa: A Numbers and Nature Counting", 
                    "African Wildlife: Images for Use in Collages and Mixed",
                    "East African Wildlife: A Visitor's Guide",
                    "At the Hand of Man: Peril and Hope for Africa's Wildlife", 
                    "Southern African Wildlife: A Visitor's Guide", 
                    "AFRICAN WILDLIFE: Beautiful Framing Pictures of Animals of African Wild Republic", 
                    "The Kingdon Pocket Guide to African Mammals", 
                    "The African Wild Dog: Behaviour,  Ecology, and Conservation"
                    ]

# Select the sentences (strings) from the list
for i in my_list:
    print(i)
    
    # Recognize words and extract them from sentences
    # And move words in a list
    n = i.split()
   # New list for new filter (delete one letter word)
    n1 =[]
    for a in n:
        # Identify words more accurately
        if len(a) == 1:
            # Recognize the elements that one letter
            #method needed
            continue
        n1. append(a)
    print(n1)
    
    # You will understand the meanings later (line 36, 37)
    my_dict ={}
    count = 0
    
    # Create a loop to convert
    # the list elements to dictionary type
    for a in n1:
        
        # Change the counter value
        # for changing the second key of the dictionary elements
        count +=1
        my_dict[a] = count
        
    # Print the dictionary after the operation for each sentence
    # Separate the results for each sentence
    print(my_dict)
    print("\n\n")
    