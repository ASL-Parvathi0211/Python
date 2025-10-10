# variables: Memory allocation of a value inside the system..
    # Variables will not store the values. Variables will store the memory allocations of the values.
    # It will create some memory dynamicaly. A variable that whatever you'r going to see here is going to take the memory allocation of the value, not a = 12
    
    #a = 12
        #print(a)
            #print(id(a))

    #b = 12
        #print(b)
            #print(id(b))

    #c = 12
        #print(c) 
            #print(id(c))


# list1 = [1,2,3]
        #print(list1)
        # print(id(list1))

    # list2 = [1,2,3]
        # print(list2)
        # print(id(list2))

    # print(list2[1])
    # print(id(list2[1]))
    # print(id(list2[0]))
    # print(id(list2[2]))
    # print(id(list2))


# Rules while declaring the variables..

    # 1) A variable can be the combination of lower case,upper case and numbers..
        # a = 12, A = 12, aA = 12, Aa = 32, a1A = 75, A1a = 22
    # 2) A variable should not start with number at any cost..
        # 1a = 32 (not accepted)
    # 3) A variable should not contian any special symbols except underscore (_)..
        # a@ = 43, b# = 21 b& = 32( none of them accepted )
        # a_ =54, A_1 =54 ( accepted )
    # 4) Single underscore can also be considered as variable..
        # _ = 43( accepted )
    # 5) Keywords cannot be taken as variables..
        # if = 23( not accepted )

# Example for 1
    # aA="python"
    # print(aA)

    # a1 = 43
    # print(a1)

#Example for 2
    # 1a = 43 ( error )

# Example for 3
    # a$ = 35 ( error )
    # a& = 67 ( error )

    # a_ = 32    (accepted)
        # print(a_)   
    # _a = 32    (accepted)
        # print(_a)

# Example for 4
    # _ = 5  (accepted)
    # print(_)



# Example for 5
    # if = 43   (Not accepted)