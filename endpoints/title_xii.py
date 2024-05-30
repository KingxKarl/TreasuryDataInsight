'''
Data Table Name: Advances to State Unemployment Funds (Social Security Act Title XII)
'''

# Field Name: record_date
'''
Display Name: Record Date
Description: The date that data was published.
Data Type: DATE
Is Required: 1
'''

# Field Name: state_nm
'''
Display Name: State Name
Description: The applicable state's name that received advances.
Data Type: STRING
Is Required: 1
'''

# Field Name: interest_rate_pct
'''
Display Name: Interest Rate Percent
Description: The interest rate on advances set by the quarterly yield amount.
Data Type: PERCENTAGE
Is Required: 1
'''

# Field Name: outstanding_advance_bal
'''
Display Name: Outstanding Advance Balance
Description: The outstanding advances balance.
Data Type: CURRENCY
Is Required: 1
'''

# Field Name: advance_auth_month_amt
'''
Display Name: Advance Authorization Current Month
Description: The approved amount the state is authorized to receive in advances for the current month.
Data Type: CURRENCY
Is Required: 1
'''

# Field Name: gross_advance_draws_month_amt
'''
Display Name: Gross Advance Draws Current Month
Description: The gross advances amount received by the state for the current month.
Data Type: CURRENCY
Is Required: 1
'''

# Field Name: interest_accrued_fytd_amt
'''
Display Name: Interest Accrued Fiscal Year to Date
Description: The interest accrued on the outstanding advances balance.
Data Type: CURRENCY
Is Required: 1
'''

# Field Name: interest_paid_amt
'''
Display Name: Interest Paid Amount
Description: The interest paid on advances by the applicable state.
Data Type: CURRENCY
Is Required: 1
'''

# Field Name: src_line_nbr
'''
Display Name: Source Line Number
Description: Indicates the row of the corresponding table where the data point can be found.
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
        'interest_rate_pct', 'outstanding_advance_bal', 'advance_auth_month_amt',
        'gross_advance_draws_month_amt', 'interest_accrued_fytd_amt', 'interest_paid_amt'
    ]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col].str.replace(',', '').str.replace('$', '').str.replace('%', ''), errors='coerce')

    df['src_line_nbr'] = pd.to_numeric(df['src_line_nbr'], errors='coerce')
    df['record_fiscal_year'] = pd.to_numeric(df['record_fiscal_year'], errors='coerce')
    df['record_fiscal_quarter'] = pd.to_numeric(df['record_fiscal_quarter'], errors='coerce')
    df['record_calendar_year'] = pd.to_numeric(df['record_calendar_year'], errors='coerce')
    df['record_calendar_quarter'] = pd.to_numeric(df['record_calendar_quarter'], errors='coerce')
    df['record_calendar_month'] = pd.to_numeric(df['record_calendar_month'], errors='coerce')
    df['record_calendar_day'] = pd.to_numeric(df['record_calendar_day'], errors='coerce')

    return df.to_dict('records')

endpoint_details = {
    'endpoint': '/v2/accounting/od/title_xii',
    'params': {
        'fields': ','.join([
            'record_date', 'state_nm', 'interest_rate_pct', 'outstanding_advance_bal',
            'advance_auth_month_amt', 'gross_advance_draws_month_amt', 'interest_accrued_fytd_amt',
            'interest_paid_amt', 'src_line_nbr', 'record_fiscal_year', 'record_fiscal_quarter',
            'record_calendar_year', 'record_calendar_quarter', 'record_calendar_month', 'record_calendar_day'
        ]),
        'page[size]': 100
    },
    'formatter': format_data
}
