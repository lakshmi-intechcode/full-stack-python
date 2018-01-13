#!/usr/bin/env python3


# Woven implementation

def remove_duplicate(string):
    list1 = []
    list2 = []
    for elements in string:
        if elements in list1 and elements == list1[-1]:
            list2.append(elements)
        else:
            list1.append(elements)
    s1 = ''.join(list1)
    s2 = ''.join(list2)
    print(s1,s2)


# Tangled implementation


if __name__ == '__main__':
    remove_duplicate()