import pandas as pd

def format_data(data):
    df = pd.DataFrame(data)
    
    # Convert date columns to datetime
    df['record_date'] = pd.to_datetime(df['record_date'])
    
    # Convert numeric columns to appropriate types
    currency_cols = [
        'net_premium_amt', 'net_discount_amt', 'accrued_int_amt', 'interest_paid_amt', 
        'inflation_comp_amt', 'month_total_amt', 'fytd_total_amt'
    ]
    for col in currency_cols:
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
    'endpoint': '/v2/accounting/od/interest_cost_fund',
    'params': {
        'fields': ','.join([
            'record_date', 'fund_id', 'fund_desc', 'cost_type_desc', 'net_premium_amt',
            'net_discount_amt', 'accrued_int_amt', 'interest_paid_amt', 'inflation_comp_amt',
            'month_total_amt', 'fytd_total_amt', 'src_line_nbr', 'record_fiscal_year',
            'record_fiscal_quarter', 'record_calendar_year', 'record_calendar_quarter',
            'record_calendar_month', 'record_calendar_day'
        ]),
        'page[size]': 100
    },
    'formatter': format_data
}
