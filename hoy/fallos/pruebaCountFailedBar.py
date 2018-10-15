name_Workwook = 'FLOW Operation and support report ASAP 7.0.2 JAMU66, WASS133 2018-10-15.xlsx'
name_Sheet = 'WASS WEEK'

import pandas as pd
import numpy as np
import CountFailedBar as cfb
rango = 2845 - 2589 #El rango es la resta de las casillas donde se encuentra la informacion

data = cfb.CountFailedBar(name_Workwook, name_Sheet, 2587, rango)
'''el numero que aparece aqui son las lineas
que la lectura de datos debe ignorar, siempre se
restaran dos casillas al limite inferior del rango'''
matrix = data.text_Columns()
matrix = data.clean_all_data(matrix)

''' clasificacion '''

nullWass = []
accountWass = []
nullWass, accountWass = data.clasificar_null_account(matrix, nullWass, accountWass)


null_513 = []
null_520 = []
null_another = []
null_513, null_520, null_another = data.clasificar_520_513_another(nullWass, null_513, null_520, null_another)

account_513 = []
account_520 = []
account_another = []
account_513, account_520, account_another = data.clasificar_520_513_another(accountWass, account_513, account_520, account_another)


print('----------full matrix wassss---------', matrix, len(matrix))
print('----------null wassss---------', nullWass, len(nullWass))
print('-----------account wass-----', accountWass, len(accountWass))

excel_null_513 = pd.DataFrame(null_513)
excel_null_520 = pd.DataFrame(null_520)
excel_null_another = pd.DataFrame(null_another)
excel_account_513 = pd.DataFrame(account_513)
excel_account_520 = pd.DataFrame(account_520)
excel_account_another = pd.DataFrame(account_another)

excel_null_513.to_excel('null_513_WASS.xlsx')
excel_null_520.to_excel('nul_520_WASS.xlsx')
excel_null_another.to_excel('null_another_WASS.xlsx')
excel_account_513.to_excel('account_513_WASS.xlsx')
excel_account_520.to_excel('account_520_WASS.xlsx')
excel_account_another.to_excel('account_another_WASS.xlsx')
