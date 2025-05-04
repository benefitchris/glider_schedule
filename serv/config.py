# -*- coding: utf-8 -*-

trans_dict = {'Controller': 'Betriebsleiter', 'Pilot': 'Schlepppilot', 'Teacher': 'Fluglehrer', 'Winch': 'Windenfahrer'}
vf_csv_header = ['Dienstbezeichnung', 'Dienstbeginn', 'Dienstende', 'Max. Personen', 'Person', 'Person2'] # import header definition from www.vereinsflieger.de


def set_config(df_user):

    # ToDo:
    # - Special time period (Fluglager) without some services (e.g pilot, winch)
    # - Individual time periods per user has to be configured as holidays

    # Controller
    df_user.loc['Controller'].at['Blonde, The', 'max'] = 4.0
    df_user.loc['Controller'].at['Grand, Peter', 'pref_day'] = 'Sun'

    # Pilot
    #df_user.loc['Pilot', 'max'] = 6.0 # defines end of season
    df_user.loc['Pilot'].at['Turkish, Jason', 'max'] = 5.0
    
    # Winch
    df_user.loc['Winch'].at['Simpson, Homer', 'max'] = 6.0
    df_user.loc['Winch'].at['Simpson, Homer', 'b-e'] = 0.45

    return df_user
