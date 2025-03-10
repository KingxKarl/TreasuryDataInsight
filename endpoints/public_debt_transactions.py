'''
Data Table Name: Public Debt Transactions
'''

# Field Name: record_date
'''
Display Name: Record Date
Description: The date that data was published.
Data Type: DATE
Is Required: 1
'''

# Field Name: transaction_type
'''
Display Name: Transaction Type
Description: Indicates whether the transaction amount represents public debt issues or redemptions.
Data Type: STRING
Is Required: 1
'''

# Field Name: security_market
'''
Display Name: Security Marketability
Description: Indicates whether a security type is marketable or nonmarketable. Marketable Debt includes Treasury Bills, Notes, Bonds, Floating Rate Notes, and Inflation-Protected Securities where ownership can be transferred from one person or entity to another. They can also be traded on the secondary market. Nonmarketable securities include Savings Bonds, Government Account Series, State and Local Government Series, Domestic Series and Foreign Series securities where legal ownership cannot be transferred.
Data Type: STRING
Is Required: 
'''

# Field Name: security_type
'''
Display Name: Security Type
Description: The type of debt instrument issued to raise money needed to operate the federal government and pay off maturing obligations. Tier one of a two-tier hierarchy for capturing public debt transactions for various security types.
Data Type: STRING
Is Required: 
'''

# Field Name: security_type_desc
'''
Display Name: Security Type Description
Description: Tier two of a two-tier hierarchy for

 capturing public debt transactions for various security types.
Data Type: STRING
Is Required: 1
'''

# Field Name: transaction_today_amt
'''
Display Name: Transactions Today
Description: The total value of public debt issues or redemptions for the day. All figures are rounded to the nearest million.
Data Type: CURRENCY0
Is Required: 1
'''

# Field Name: transaction_mtd_amt
'''
Display Name: Transactions Month to Date
Description: The month to date value of public debt issues or redemptions for the month. All figures are rounded to the nearest million.
Data Type: CURRENCY0
Is Required: 1
'''

# Field Name: transaction_fytd_amt
'''
Display Name: Transactions Fiscal Year to Date
Description: The fiscal year to date value of public debt issues or redemptions for the fiscal year. All figures are rounded to the nearest million.
Data Type: CURRENCY0
Is Required: 1
'''

# Field Name: table_nbr
'''
Display Name: Table Number
Description: The corresponding table number in the Daily Treasury Statement.
Data Type: STRING
Is Required: 1
'''

# Field Name: table_nm
'''
Display Name: Table Name
Description: The name of the corresponding table in the Daily Treasury Statement.
Data Type: STRING
Is Required: 1
'''

# Field Name: src_line_nbr
'''
Display Name: Source Line Number
Description: Indicates the row of the corresponding table on the Daily Treasury Statement where a data point can be found. This can assist in structuring the data in a similar format to the Daily Treasury Statement and in understanding potential hierarchies within the table.
Data Type: INTEGER
Is Required: 1
'''

# Field Name: record_fiscal_year
'''
Display Name: Fiscal Year
Description: The fiscal year associated with record_date. The federal government's fiscal year runs from October 1 to September 30.
Data Type: YEAR
Is Required: 1
'''

# Field Name: record_fiscal_quarter
'''
Display Name: Fiscal Quarter Number
Description: The fiscal quarter associated with record_date. For the federal government these quarters are: Q1 - October to December, Q2 - January to March, Q3 - April to June, Q4 - July to September.
Data Type: QUARTER
Is Required: 1
'''

# Field Name: record_calendar_year
'''
Display Name: Calendar Year
Description: The calendar year associated with record_date.
Data Type: YEAR
Is Required: 1
'''

# Field Name: record_calendar_quarter
'''
Display Name: Calendar Quarter Number
Description: The calendar quarter associated with record_date.
Data Type: QUARTER
Is Required: 1
'''

# Field Name: record_calendar_month
'''
Display Name: Calendar Month Number
Description: The calendar month associated with record_date.
Data Type: MONTH
Is Required: 1
'''

# Field Name: record_calendar_day
'''
Display Name: Calendar Day Number
Description: The calendar day associated with record_date.
Data Type: DAY
Is Required: 1
'''

import pandas as pd

def format_data(data):
    df = pd.DataFrame(data)

    df['record_date'] = pd.to_datetime(df['record_date'])

    numeric_cols = [
        'transaction_today_amt', 'transaction_mtd_amt', 'transaction_fytd_amt'
    ]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col].str.replace(',', '').str.replace('$', ''), errors='coerce')

    df['src_line_nbr'] = pd.to_numeric(df['src_line_nbr'], errors='coerce')
    df['record_fiscal_year'] = pd.to_numeric(df['record_fiscal_year'], errors='coerce')
    df['record_fiscal_quarter'] = pd.to_numeric(df['record_fiscal_quarter'], errors='coerce')
    df['record_calendar_year'] = pd.to_numeric(df['record_calendar_year'], errors='coerce')
    df['record_calendar_quarter'] = pd.to_numeric(df['record_calendar_quarter'], errors='coerce')
    df['record_calendar_month'] = pd.to_numeric(df['record_calendar_month'], errors='coerce')
    df['record_calendar_day'] = pd.to_numeric(df['record_calendar_day'], errors='coerce')

    return df.to_dict('records')

endpoint_details = {
    'endpoint': '/v1/accounting/dts/public_debt_transactions',
    'params': {
        'fields': ','.join([
            'record_date', 'transaction_type', 'security_market', 'security_type', 'security_type_desc',
            'transaction_today_amt', 'transaction_mtd_amt', 'transaction_fytd_amt', 'table_nbr', 'table_nm',
            'src_line_nbr', 'record_fiscal_year', 'record_fiscal_quarter', 'record_calendar_year',
            'record_calendar_quarter', 'record_calendar_month', 'record_calendar_day'
        ]),
        'page[size]': 100
    },
    'formatter': format_data
}
