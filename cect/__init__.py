#! /usr/bin/env python


def print_(msg, print_it=True):  # print_it=False when not verbose
    if print_it:
        pre = "cect      >>> "
        print("%s %s" % (pre, msg.replace("\n", "\n" + pre)))
