#!/usr/bin/env python3


# Woven implementation

def titlecase(string, exceptions):
    words = string.split()
    title = []
    for position, word in enumerate(words):
        if position == 0 or position == len(words) or word not in exceptions:
            title.append(word.title())
        else:
            title.append(word)
    return ' '.join(title)


# Tangled implementation

def o(w,es):
    if w not in es:
        return True
    return False

def p(i,ws):
    if i==0 or i==len(ws)-1:
        return True
    return False

def t(s,es):
    ws = s.split()
    t  = [w.title() if o(w,es) or p(i,ws) else w for i,w in enumerate(ws)]
    return ' '.join(t)


if __name__ == '__main__':
    strings    = ['the cathedral and the bazaar', \
                    'bitcoin: a peer-to-peer electronic cash system', \
                    'programming from the ground up', \
                    'production of commodities by means of commodities', \
                    'the mythical man-month', \
                    'finite-dimensional vector spaces', \
                    'maximum linux security', \
                    'wage labour and capital', \
                    'digital fortress', \
                    'the player of games']
    exceptions = ['a', \
                    'an', \
                    'at', \
                    'and', \
                    'but', \
                    'by', \
                    'for', \
                    'from', \
                    'nor', \
                    'of', \
                    'on', \
                    'or', \
                    'the', \
                    'to']
    for string in strings:
        if titlecase(string, exceptions) != t(string, exceptions):
            print(titlecase(string, exceptions))
        else:
            import re
            message = 'The woven implementation returned a different value \
                        than the one returned by the tangled implementation.'
            print(re.sub(' +', ' ', message))