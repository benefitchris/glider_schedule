# -*- coding: utf-8 -*-

import pandas as pd
from pathlib import Path
from serv.config import trans_dict
from serv.config import vf_csv_header


def load_user_with_function(file):
    """Import / loads user data and service functions from csv file

        Parameters
        ----------
        file : Path or str
            file path

        Returns
        -------
        dict_u : dict
            dictionary from csv import

        Examples
        --------

        >>> from serv.servInterface import load_user_with_function
        ... 
        >>> users = load_user_with_function(user_path)

        .. versionadded:: 1.0.0
    """

    df_u = pd.read_csv(file, sep=';', encoding='UTF-8')
    
    dict_u = {}
    
    for key, value in trans_dict.items():
        print('INFO: trans_dict =', key, '<->', value)
        dict_u[key] = list(df_u[value][df_u[value].notna()].values)

    return dict_u


def load_service_from_csv(file, function='Teacher'):
    """ ToDo
    """
    
    try:
        df_in = pd.read_csv(file, sep=';', encoding='ANSI') 
        dates = pd.to_datetime(df_in['Dienstbeginn'], dayfirst=True, format='%d.%m.%Y %H:%M').dt.strftime('%d.%m.%Y')
        df_service = pd.DataFrame(data=df_in['Person'].values, index=dates, columns=[function])
        return df_service

    
    except IOError as e:
        print("An error occurred:", e)
        return False
    
    
def export_service_to_csv(df_schedule, *function):
    """Export service pandas DataFrame to csv format 

        This function provides the needed csv format to import services at www.vereionsfliegde.de

        Parameters
        ----------
        df_schedule : pandas DataFrame
            table with all services
        function : str or list(str)
            name of functions in schedule

        Examples
        --------

        >>> from serv.servInterface import export_service_to_csv
        ... 
        >>> export_service_to_csv(df_schedule, *functions)

        .. versionadded:: 1.0.0
    """
    
    for func in function:
        dict_export = {vf_csv_header[0]: [trans_dict[func]]*df_schedule[func].size,
               vf_csv_header[1]: pd.to_datetime(df_schedule[func].index, dayfirst=True, format='%d.%m.%Y').strftime('%d.%m.%Y 09:00'),
               vf_csv_header[2]: pd.to_datetime(df_schedule[func].index, dayfirst=True, format='%d.%m.%Y').strftime('%d.%m.%Y 19:00'),
               vf_csv_header[3]: '1',
               vf_csv_header[4]: df_schedule[func].values,
               vf_csv_header[5]: ''}
        df_export = pd.DataFrame(data=dict_export)
        
        try:
            df_export.to_csv(Path(r'{}_export.csv'.format(func)), sep=';', index=False, encoding='ANSI')
        except Exception as error:
            print('Error function \'export_service_to_csv\':', error)
