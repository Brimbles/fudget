import pandas as pd
import numpy_financial as npf
import matplotlib.pyplot as plt
from collections import namedtuple

# loan characteristics
original_balance = 500_000
coupon = 0.08
term = 120

# payments
periods = range(1, term+1)
interest_payment = npf.ipmt(
    rate=coupon / 12, per=periods, nper=term, pv=-original_balance)
principal_payment = npf.ppmt(
    rate=coupon / 12, per=periods, nper=term, pv=-original_balance)

# print(f'interest payment is {interest_payment}')
# print(f'principal_payment is {principal_payment}')


# pandas float formatting_
pd.options.display.float_format = '{:,.2f}'.format

# cash flow table_
cf_data = {'Interest': interest_payment, 'Principal': principal_payment}
cf_table = pd.DataFrame(data=cf_data, index=periods)
cf_table['Payment'] = cf_table['Interest'] + cf_table['Principal']
cf_table['Ending Balance'] = original_balance - \
                             cf_table['Principal'].cumsum()
cf_table['Beginning Balance'] = [original_balance] + \
                                list(cf_table['Ending Balance'])[:-1]
cf_table = cf_table[['Beginning Balance', 'Payment', 'Interest', 
                     'Principal', 'Ending Balance']]
print(cf_table.head(8))