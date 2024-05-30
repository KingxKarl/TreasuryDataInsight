'''
Data Table Name: 120 Day Delinquent Debt Referral Compliance Report
'''

# Field Name: record_date
'''
Display Name: Record Date
Description: The date that data was published.
Data Type: DATE
Is Required: 1
'''

# Field Name: agency_bureau_indicator
'''
Display Name: Agency Bureau Indicator
Description: Distinguishes between Agency and Bureau.
Data Type: STRING
Is Required: 
'''

# Field Name: agency_nm
'''
Display Name: Agency Name
Description: Indicates the Agency to which the Bureau belongs, if applicable.
Data Type: STRING
Is Required: 
'''

# Field Name: bureau_nm
'''
Display Name: Bureau Name
Description: The name of the Bureau for which compliance rate data is presented.
Data Type: STRING
Is Required: 
'''

# Field Name: total_eligible_debt_amt
'''
Display Name: Total Eligible Debt Amount
Description: Dollar value of debt required to be referred to the Treasury Offset Program by the Agency or Bureau (Part 2 section B line 1 M (amount) as reported on the Treasury Report on Receivables).
Data Type: CURRENCY
Is Required: 1
'''

# Field Name: total_eligible_debt_cnt
'''
Display Name: Total Eligible Debt Count
Description: Number of debts required to be referred to the Treasury Offset Program by the Agency or Bureau (Part 2 section B line 1 M (number) as reported on the Treasury Report on Receivables).
Data Type: NUMBER
Is Required: 1
'''

# Field Name: eligible_debt_referred_amt
'''
Display Name: Eligible Debt Referred Amount
Description: Dollar value of debt referred directly to the Treasury Offset Program by the Agency or Bureau and debt referred to the Treasury Offset Program through Cross-Servicing (Part 2 section B line 1 N (amount) + Part 2 section B line 1 O (amount) as reported on the Treasury Report on Receivables).
Data Type: CURRENCY
Is Required: 1
'''

# Field Name: eligible_debt_referred_cnt
'''
Display Name: Eligible Debt Referred Count
Description: Number of debts referred directly to the Treasury Offset Program by the Agency or Bureau and debt referred to the Treasury Offset Program through Cross-Servicing (Part 2 section B line 1 N (number) + Part 2 section B line 1 O (number) as reported on the Treasury Report on Receivables).
Data Type: NUMBER
Is Required: 1
'''

# Field Name: eligible_debt_not_referred_amt
'''
Display Name: Eligible Debt Not Referred Amount
Description: Dollar value of debt required to be referred to the Treasury Offset Program by the Agency or Bureau that has not yet been referred (Part 2 section B line 1 P (amount) as reported on the Treasury Report on Receivables).
Data Type: CURRENCY
Is Required: 1
'''

# Field Name: eligible_debt_not_referred_cnt
'''
Display Name: Eligible Debt Not Referred Count
Description: Number of debts required to be referred to the Treasury Offset Program by the Agency or Bureau that has not yet been referred (Part 2 section B line 1 P (number) as reported on the Treasury Report on Receivables).
Data Type: NUMBER
Is Required: 1
'''

# Field Name: compliance_rate_amt
'''
Display Name: Compliance Rate Amount
Description: The dollar value of debt referred directly to the Treasury Offset Program by the Agency or Bureau and the debt referred to the Treasury Offset Program through Cross-Servicing for the Agency or Bureau divided by the dollar value of debt required to be referred to the Treasury Offset Program by the Agency or Bureau. (CALCULATION: Part 2 section B line 1 N (amount) + Part 2 section B line 1 O (amount) / Part 2 section B line 1 M (amount)).
Data Type: PERCENTAGE
Is Required: 1
'''

# Field Name: compliance_rate_cnt
'''
Display Name: Compliance Rate Count
Description: The number of debts referred directly to the Treasury Offset Program by the Agency or Bureau and the number of debts referred to the Treasury Offset Program through Cross-Servicing for the Agency or Bureau divided by the number of debts required to be referred to the Treasury Offset Program by the Agency or Bureau. (CALCULATION: Part 2 section B line 1 N (number) + Part 2 section B line 1 O (number) / Part 2 section B line 1 M (number)).
Data Type: PERCENTAGE
Is Required: 1
'''

# Field Name: cfo_agency_indicator
'''
Display Name: CFO Agency Indicator
Description: Indicates if the Agency is a CFO Agency.
Data Type: STRING
Is Required: 
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
        'total_eligible_debt_amt', 'total_eligible_debt_cnt', 'eligible_debt_referred_amt', 
        'eligible_debt_referred_cnt', 'eligible_debt_not_referred_amt', 'eligible_debt_not_referred_cnt', 
        'compliance_rate_amt', 'compliance_rate_cnt'
    ]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col].str.replace(',', '').str.replace('$', '').str.replace('%', ''), errors='coerce')
    
    return df.to_dict('records')

endpoint_details = {
    'endpoint': '/v2/debt/tror/data_act_compliance',
    'params': {
        'fields': ','.join([
            'record_date', 'agency_bureau_indicator', 'agency_nm', 'bureau_nm', 
            'total_eligible_debt_amt', 'total_eligible_debt_cnt', 
            'eligible_debt_referred_amt', 'eligible_debt_referred_cnt', 
            'eligible_debt_not_referred_amt', 'eligible_debt_not_referred_cnt', 
            'compliance_rate_amt', 'compliance_rate_cnt', 
            'cfo_agency_indicator', 'record_fiscal_year', 'record_fiscal_quarter', 
            'record_calendar_year', 'record_calendar_quarter', 
            'record_calendar_month', 'record_calendar_day'
        ]),
        'page[size]': 100
    },
    'formatter': format_data
}
