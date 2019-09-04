def refine(mylist):
    mylist.insert(-1, "and")
    str1 = ', '.join(str(e) for e in mylist)
    str1 = str1.replace("and,", "and")
    print(str1)


spam = ['apples', 'bananas', 'tofu', 'cats', 1, False, "monkey"]
refine(spam)
