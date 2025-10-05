
# Keywords: Those words whose functionality is already defined..

# Can we name the keywords.py file in Python?
# There is a file called keywords.py in Python. If we save the file keywords.py. It doesn’t create an issue/error now. When we try to execute the code, then it shows an error.

# How to find the keywords file?
# Open File Explorer, local disk (C), Users, asple, App data, Local, Programs, Python, Python311, lib, and keyword.py.
# (C:\Users\aslpe\AppData\Local\Programs\Python\Python311\Lib)
# Then open it with any software.
# "Kwlist" stands for "keywords list."

# What does "import" mean?
# Import means loading the code but not copy-pasting the code/one code of a Python file in some other Python file.
# EX: Kwlist has 50 keywords, which means Kwlist is storing all the data.
# So this kwlist list is written in one Python file. I want to use the same kwlist in another file. We don’t need to copy and paste the file. We can use the concept of importing.

# How to import data?
# There are 2 types of importing the data.
    # Import: We are importing the complete module. So, that’s the module name. (dot) that respective attribute name/variable name.
    # Unnecessary huge amounts of data are loaded. The complete file is loaded.
        # Import file name 
            # Print  (file name.(dot)file name (from which the data is importing))
            # EX: Import keyword
            # print(keyword.kwlist)

# Another way to import data is from using
   # From: We are not importing the complete module. We are going inside the module, and we are just importing only the Kwlist.
   # If we want the specific function to be loaded, we can choose from.
   # From file name import file name (from which the data is importing)
        # print(file name) (from which the data is importing)
        # EX: from keyword import kwlist
        # print(kwlist)

# How do I find out if there are 35 keywords or not?
# Len: Will return the length of the data.
    # print(len(file name))
    # EX: print(len(keyword.kwlist))

