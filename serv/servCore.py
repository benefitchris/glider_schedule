# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import holidays


__version__ = '1.1.0'


user_scores = {'stat': 0.0, 'score': 0.0, 'weight': 1.0, 'max': None, 'b-e': None , 'pref_day': None, 'comp_we': False}


def _get_formatted_date(date):
    return date.strftime('%d.%m.%Y')


def get_schedule_frame(start_date='2024-03-23', end_date='2024-11-03'):

    data = []
    current_date = pd.to_datetime(start_date)
    bw_holidays = holidays.Germany(years=current_date.year, prov='BW')
    
    while current_date <= pd.to_datetime(end_date):
        weekday = current_date.strftime('%a')
        date = _get_formatted_date(current_date)
    
        # only saturday and sunday or holiday
        if weekday == 'Sat' or weekday == 'Sun' or current_date in bw_holidays:
            data.append([weekday, date])
        
        current_date += pd.DateOffset(days=1)
    
    df_dates = pd.DataFrame(data, columns=['Weekday', 'Date'])
    df_dates = df_dates.set_index('Date')
    
    return df_dates


def get_b_e_quad_factor(day, base, max_days, level=1.0, function=False):

    B = base
    L = level
    E = max_days - 1
    K = E * E * 1.0 / 6.0
    D = np.roots([1.0, -E, K])[0]
    #print('INFO: D =', D, '(root)')
    
    # coefficients
    a = (L - B) / (D * (D - E))
    #print('INFO: a = ', a)
    b = (B - L) * E / (D * (D - E))
    #print('INFO: b = ', b)
    c = B
    #print('INFO: c = ', B)
    
    f = lambda d : a * d * d + b * d + c
    
    if function:
        days = np.linspace(0.0, E, num=E+1)
        df_func = pd.DataFrame(data=f(days), index=days, columns=['b-e_factor'])
        df_func['level'] = L
        return df_func
    else:
        return f(day)


def get_b_e_step_factor(day, base, max_days, level=1.0, window=0.5, function=False):

    d_step = max_days * (1.0 - window) / 2.0
    bottom = base
    top = base + 1 / window * (level - base)
    
    f = lambda d : bottom * (d < d_step) + top * (d >= d_step) * (d <= max_days - d_step) + bottom * (d > max_days - d_step)
    
    if function:
        days = np.linspace(0.0, max_days - 1, num=max_days)
        df_func = pd.DataFrame(data=f(days), index=days, columns=['b-e_factor'])
        df_func['level'] = level
        return df_func
    else:
        return f(day)


def get_b_e_factor(day, base, max_days, window=0.5, function=False):

    d_step = max_days * (1.0 - window) / 2.0
    bottom = base * (window / 0.5)
    top = 1 / base * (0.5 / window)
    
    f = lambda d : bottom * (d < d_step) + top * (d >= d_step) * (d <= max_days - d_step) + bottom * (d > max_days - d_step)
    
    if function:
        days = np.linspace(0.0, max_days - 1, num=max_days)
        df_func = pd.DataFrame(data=f(days), index=days, columns=['b-e_factor'])
        return df_func
    else:
        return f(day)

