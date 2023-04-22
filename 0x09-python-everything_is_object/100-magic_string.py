#!/usr/bin/python3
def magic_string():
magic_string.str = getattr(magic_string, 'str', 0) + 1
return ('BestSchool' + ', BestSchool' * (magic_string.str-1)) + "$"
