'''
Data Table Name: Short-Term Cash Investments
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
Description: Tier one of a two-tier hierarchy for categorizing short-term cash investments. Indicates whether the transaction amount represents deposits or withdrawals.
Data Type: STRING
Is Required: 
'''

# Field Name: transaction_type_desc
'''
Display Name: Transaction Type Description
Description: Tier two of a two-tier hierarchy for categorizing short-term cash investments.
Data Type: STRING
Is Required: 1
'''

# Field Name: depositary_type_a_amt
'''
Display Name: Type A Depositary Amount
Description: The amount of deposits or withdrawals for depositary type A. All figures are rounded to the nearest million.
Data Type: CURRENCY0
Is Required: 1
'''

# Field Name: depositary_type_b_amt
'''
Display Name: Type B Depositary Amount
Description: The amount of deposits or withdrawals for depositary type B. All figures are rounded to the nearest million.
Data Type: CURRENCY0
Is Required: 1
'''

# Field Name: depositary_type_c_amt
'''
Display Name: Type C Depositary Amount
Description: The amount of deposits or withdrawals for depositary type C. All figures are rounded to the nearest million.
Data Type: CURRENCY0
Is Required: 1
'''

# Field Name: total_amt
'''
Display Name: Total Amount
Description: Total amount of transactions across all depositary types for the day. All figures are rounded to the nearest million.
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

# Field Name: sub_table_name
'''
Display Name: Sub Table Name
Description: Additional detail about the corresponding table in the Daily Treasury Statement.
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
        'depositary_type_a_amt', 'depositary_type_b_amt', 'depositary_type_c_amt', 'total_amt'
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
    'endpoint': '/v1/accounting/dts/short_term_cash_investments',
    'params': {
        'fields': ','.join([
            'record_date', 'transaction_type', 'transaction_type_desc', 'depositary_type_a_amt',
            'depositary_type_b_amt', 'depositary_type_c_amt', 'total_amt', 'table_nbr', 'table_nm',
            'sub_table_name', 'src_line_nbr', 'record_fiscal_year', 'record_fiscal_quarter',
            'record_calendar_year', 'record_calendar_quarter', 'record_calendar_month', 'record_calendar_day'
        ]),
        'page[size]': 100
    },
    'formatter': format_data
}
