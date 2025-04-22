# -*- coding: utf-8 -*-


# available test persons per service domain
def get_test_user(simple=False):

    if simple:
        user_dict = {'Winch': ['Sand', 'Ger', 'Mas', 'Col']}
    else:
        user_dict = {'Controller': ['Lu', 'Sam', 'Dan', 'Toni', 'Pam', 'Val', 'Rin', 'Mas'],
                     'Pilot': ['Man', 'Ral', 'Rich', 'Mat', 'Gus', 'Fal'],
                     'Teacher': ['Rich', 'Tom', 'Sand', 'Bill', 'Mon', 'Mat'],
                     'Winch': ['Sand', 'Bong', 'Mas', 'Rin', 'Col']}
        
    return user_dict
