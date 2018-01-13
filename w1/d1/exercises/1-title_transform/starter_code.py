#!/usr/bin/env python3


def titlecase(string, exceptions):
	# TODO: Start the exercise.
    pass


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
        print(titlecase(string, exceptions))