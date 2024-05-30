'''
Data Table Name: Debt Subject to Limit
'''

# Field Name: record_date
'''
Display Name: Record Date
Description: The date that data was published.
Data Type: DATE
Is Required: 1
'''

# Field Name: debt_catg
'''
Display Name: Debt Category
Description: Tier one of a two-tier hierarchy for capturing cash basis adjustments of various debt types.
Data Type: STRING
Is Required: 
'''

# Field Name: debt_catg_desc
'''
Display Name: Debt Category Description
Description: Tier two of a two-tier hierarchy for capturing cash basis adjustments of various debt types.
Data Type: STRING
Is Required: 1
'''

# Field Name: close_today_bal
'''
Display Name: Closing Balance Today
Description: The closing balance at the end of business for the day. All figures are rounded to the nearest million.
Data Type: CURRENCY0
Is Required: 
'''

# Field Name: open_today_bal
'''
Display Name: Opening Balance Today
Description: The opening balance at the start of business for the day. All figures are rounded to the nearest million.
Data Type: CURRENCY0
Is Required: 
'''

# Field Name: open_month_bal
'''
Display Name: Opening Balance This Month
Description: The opening balance at the start of business on the first day of the month. All figures are rounded to the nearest million.
Data Type: CURRENCY0
Is Required: 
'''

# Field Name: open_fiscal_year_bal
'''
Display Name: Opening Balance This Fiscal Year
Description: The opening balance at the start of business on the first day of the fiscal year. The federal government's fiscal year starts October 1 and ends September 30. All figures are rounded to the nearest million.
Data Type: CURRENCY0
Is Required: 
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
        'close_today_bal', 'open_today_bal', 'open_month_bal', 'open_fiscal_year_bal'
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
    'endpoint': '/v1/accounting/dts/debt_subject_to_limit',
    'params': {
        'fields': ','.join([
            'record_date', 'debt_catg', 'debt_catg_desc', 'close_today_bal', 'open_today_bal',
            'open_month_bal', 'open_fiscal_year_bal', 'table_nbr', 'table_nm', 'sub_table_name',
            'src_line_nbr', 'record_fiscal_year', 'record_fiscal_quarter', 'record_calendar_year',
            'record_calendar_quarter', 'record_calendar_month', 'record_calendar_day'
        ]),
        'page[size]': 100
    },
    'formatter': format_data
}
