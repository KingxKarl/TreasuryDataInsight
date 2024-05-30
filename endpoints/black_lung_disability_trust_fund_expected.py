import pandas as pd

def format_data(data):
    df = pd.DataFrame(data)
    
    # Convert date columns to datetime
    df['record_date'] = pd.to_datetime(df['record_date'])
    
    # Convert numeric columns to appropriate types
    df['fiscal_year'] = pd.to_numeric(df['fiscal_year'], errors='coerce')
    df['fiscal_year_expected_thous_amt'] = pd.to_numeric(df['fiscal_year_expected_thous_amt'].str.replace(',', '').str.replace('$', ''), errors='coerce')
    df['src_line_nbr'] = pd.to_numeric(df['src_line_nbr'], errors='coerce')
    df['record_fiscal_year'] = pd.to_numeric(df['record_fiscal_year'], errors='coerce')
    df['record_fiscal_quarter'] = pd.to_numeric(df['record_fiscal_quarter'], errors='coerce')
    df['record_calendar_year'] = pd.to_numeric(df['record_calendar_year'], errors='coerce')
    df['record_calendar_quarter'] = pd.to_numeric(df['record_calendar_quarter'], errors='coerce')
    df['record_calendar_month'] = pd.to_numeric(df['record_calendar_month'], errors='coerce')
    df['record_calendar_day'] = pd.to_numeric(df['record_calendar_day'], errors='coerce')
    
    return df.to_dict('records')

endpoint_details = {
    'endpoint': '/v1/accounting/od/black_lung_disability_trust_fund_expected',
    'params': {
        'fields': ','.join([
            'record_date', 'fiscal_year', 'table_nbr', 'table_nm', 'account_desc', 
            'component_desc', 'fiscal_year_expected_thous_amt', 'src_line_nbr', 
            'record_fiscal_year', 'record_fiscal_quarter', 'record_calendar_year', 
            'record_calendar_quarter', 'record_calendar_month', 'record_calendar_day'
        ]),
        'page[size]': 100
    },
    'formatter': format_data
}
