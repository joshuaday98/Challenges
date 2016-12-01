"""
>>> str_surgery('many students are writing code', ['students', 'code'])
'students are writing code'
>>> str_surgery('a b c d a', ['a', 'c', 'd'])
'c d a'
>>> str_surgery('Jack and Jill went up the hill To fetch a pail of water. Jack fell down and broke his crown, And Jill came tumbling after. Up Jack got, and home did trot, As fast as he could caper, To old Dame Dob, who patched his nob With vinegar and brown paper.', ['dob', 'vinegar'])
'dob who patched his nob with vinegar and brown paper'
"""
import re
import string


def clean_strang(strang):
    strang = re.sub('['+string.punctuation+']', '', strang).lower().split(' ')
    return strang


def str_surgery(strang, key):
    strang = clean_strang(strang)

    eval_list = (strang[strang.index(char):] for char in key if char in strang)

    eval_list = (element for element in eval_list if set(element).issuperset(set(key)))

    result = ' '.join(min(eval_list, key=len))

    return(result)