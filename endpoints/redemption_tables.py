'''
Data Table Name: Redemption Tables
'''

# Field Name: redemp_period
'''
Display Name: Redemption Period
Description: The month(s) for which redemption and interest earned values are applicable
Data Type: STRING
Is Required: 1
'''

# Field Name: issue_name
'''
Display Name: Issue Name
Description: Type of accrual savings bond (E, EE, and I)
Data Type: STRING
Is Required: 1
'''

# Field Name: issue_year
'''
Display Name: Issue Year
Description: Year an accrual savings bond was issued
Data Type: YEAR
Is Required: 1
'''

# Field Name: issue_months
'''
Display Name: Issue Months
Description: Month(s) in which a given accrual savings bond was issued
Data Type: STRING
Is Required: 1
'''

# Field Name: yield_from_issue_pct
'''
Display Name: Yield from Issue
Description: Interest earnings expressed as a percentage on accrual savings bond from issue month/year to redemption date.
Data Type: PERCENTAGE
Is Required: 
'''

# Field Name: redemp_value_10_amt
'''
Display Name: Redemption Value $10
Description: Total amount a $10 accrual savings bond is worth in that redemption month/year
Data Type: CURRENCY
Is Required: 
'''

# Field Name: int_earned_10_amt
'''
Display Name: Interest Earned $10
Description: Interest earned on a $10 accrual savings bond from issue month/year to redemption month/year
Data Type: CURRENCY
Is Required: 
'''

# Field Name: redemp_value_25_amt
'''
Display Name: Redemption Value $25
Description: Total amount a $25 accrual savings bond is worth in that redemption month/year
Data Type: CURRENCY
Is Required: 
'''

# Field Name: int_earned_25_amt
'''
Display Name: Interest Earned $25
Description: Interest earned on a $25 accrual savings bond from issue month/year to redemption month/year
Data Type: CURRENCY
Is Required: 
'''

# Field Name: redemp_value_50_amt
'''
Display Name: Redemption Value $50
Description: Total amount a $50 accrual savings bond is worth in that redemption month/year
Data Type: CURRENCY
Is Required: 
'''

# Field Name: int_earned_50_amt
'''
Display Name: Interest Earned $50
Description: Interest earned on a $50 accrual savings bond from issue month/year to redemption month/year
Data Type: CURRENCY
Is Required: 
'''

# Field Name: redemp_value_75_amt
'''
Display Name: Redemption Value $75
Description: Total amount a $75 accrual savings bond is worth in that redemption month/year
Data Type: CURRENCY
Is Required: 
'''

# Field Name: int_earned_75_amt
'''
Display Name: Interest Earned $75
Description: Interest earned on a $75 accrual savings bond from issue month/year to redemption month/year
Data Type: CURRENCY
Is Required: 
'''

# Field Name: redemp_value_100_amt
'''
Display Name: Redemption Value $100
Description: Total amount a $100 accrual savings bond is worth in that redemption month/year
Data Type: CURRENCY
Is Required: 
'''

# Field Name: int_earned_100_amt
'''
Display Name: Interest Earned $100
Description: Interest earned on a $100 accrual savings bond from issue month/year to redemption month/year
Data Type: CURRENCY
Is Required: 
'''

# Field Name: redemp_value_200_amt
'''
Display Name: Redemption Value $200
Description: Total amount a $200 accrual savings bond is worth in that redemption month/year
Data Type: CURRENCY
Is Required: 
'''

# Field Name: int_earned_200_amt
'''
Display Name: Interest Earned $200
Description: Interest earned on a $200 accrual savings bond from issue month/year to redemption month/year
Data Type: CURRENCY
Is Required: 
'''

# Field Name: redemp_value_500_amt
'''
Display Name: Redemption Value $500
Description: Total amount a $500 accrual savings bond is worth in that redemption month/year
Data Type: CURRENCY
Is Required: 
'''

# Field Name: int_earned_500_amt
'''
Display Name: Interest Earned $500
Description: Interest earned on a $500 accrual savings bond from issue month/year to redemption month/year
Data Type: CURRENCY
Is Required: 
'''

# Field Name: redemp_value_1000_amt
'''
Display Name: Redemption Value $1,000
Description: Total amount a $1,000 accrual savings bond is worth in that redemption month/year
Data Type: CURRENCY
Is Required: 
'''

# Field Name: int_earned_1000_amt
'''
Display Name: Interest Earned $1,000
Description: Interest earned on a $1,000 accrual savings bond from issue month/year to redemption month/year
Data Type: CURRENCY
Is Required: 
'''

# Field Name: redemp_value_5000_amt
'''
Display Name: Redemption Value $5,000
Description: Total amount a $5,000 accrual savings bond is worth in that redemption month/year
Data Type: CURRENCY
Is Required: 
'''

# Field Name: int_earned_5000_amt
'''
Display Name: Interest Earned $5,000
Description: Interest earned on a $5,000 accrual savings bond from issue month/year to redemption month/year
Data Type: CURRENCY
Is Required: 
'''

# Field Name: redemp_value_10000_amt
'''
Display Name: Redemption Value $10,000
Description: Total amount a $10,000 accrual savings bond is worth in that redemption month/year
Data Type: CURRENCY
Is Required: 
'''

# Field Name: int_earned_10000_amt
'''
Display Name: Interest Earned $10,000
Description: Interest earned on a $10,000 accrual savings bond from issue month/year to redemption month/year
Data Type: CURRENCY
Is Required: 
'''

# Field Name: src_line_nbr
'''
Display Name: Source Line Number
Description: Indicates the row of the corresponding table where the data point can be found.
Data Type: INTEGER
Is Required: 1
'''


import pandas as pd

def format_data(data):
    df = pd.DataFrame(data)

    df['redemp_period'] = pd.to_datetime(df['redemp_period'])

    numeric_cols = [
        'redemp_value_10_amt', 'int_earned_10_amt', 'redemp_value_25_amt', 'int_earned_25_amt',
        'redemp_value_50_amt', 'int_earned_50_amt', 'redemp_value_75_amt', 'int_earned_75_amt',
        'redemp_value_100_amt', 'int_earned_100_amt', 'redemp_value_200_amt', 'int_earned_200_amt',
        'redemp_value_500_amt', 'int_earned_500_amt', 'redemp_value_1000_amt', 'int_earned_1000_amt',
        'redemp_value_5000_amt', 'int_earned_5000_amt', 'redemp_value_10000_amt', 'int_earned_10000_amt'
    ]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col].str.replace(',', '').str.replace('$', ''), errors='coerce')

    df['src_line_nbr'] = pd.to_numeric(df['src_line_nbr'], errors='coerce')
    df['issue_year'] = pd.to_numeric(df['issue_year'], errors='coerce')

    return df.to_dict('records')

endpoint_details = {
    'endpoint': '/v2/accounting/od/redemption_tables',
    'params': {
        'fields': ','.join([
            'redemp_period', 'issue_name', 'issue_year', 'issue_months',
            'yield_from_issue_pct', 'redemp_value_10_amt', 'int_earned_10_amt',
            'redemp_value_25_amt', 'int_earned_25_amt', 'redemp_value_50_amt',
            'int_earned_50_amt', 'redemp_value_75_amt', 'int_earned_75_amt',
            'redemp_value_100_amt', 'int_earned_100_amt', 'redemp_value_200_amt',
            'int_earned_200_amt', 'redemp_value_500_amt', 'int_earned_500_amt',
            'redemp_value_1000_amt', 'int_earned_1000_amt', 'redemp_value_5000_amt',
            'int_earned_5000_amt', 'redemp_value_10000_amt', 'int_earned_10000_amt',
            'src_line_nbr'
        ]),
        'page[size]': 100
    },
    'formatter': format_data
}
