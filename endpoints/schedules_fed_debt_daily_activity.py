import pandas as pd

def format_data(data):
    df = pd.DataFrame(data)

    df['record_date'] = pd.to_datetime(df['record_date'])

    numeric_cols = [
        'public_prin_borrowings_amt', 'public_prin_repayments_amt', 'public_interest_accrued_amt',
        'public_interest_paid_amt', 'public_net_unamortized_amt', 'public_net_amortization_amt',
        'intragov_prin_net_increase_amt', 'intragov_interest_accrued_amt', 'intragov_interest_paid_amt',
        'intragov_net_unamortized_amt', 'intragov_net_amortization_amt'
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
    'endpoint': '/v1/accounting/od/schedules_fed_debt_daily_activity',
    'params': {
        'fields': ','.join([
            'record_date', 'type', 'public_prin_borrowings_amt', 'public_prin_repayments_amt', 
            'public_interest_accrued_amt', 'public_interest_paid_amt', 'public_net_unamortized_amt', 
            'public_net_amortization_amt', 'intragov_prin_net_increase_amt', 'intragov_interest_accrued_amt', 
            'intragov_interest_paid_amt', 'intragov_net_unamortized_amt', 'intragov_net_amortization_amt', 
            'src_line_nbr', 'record_fiscal_year', 'record_fiscal_quarter', 'record_calendar_year', 
            'record_calendar_quarter', 'record_calendar_month', 'record_calendar_day'
        ]),
        'page[size]': 100
    },
    'formatter': format_data
}
