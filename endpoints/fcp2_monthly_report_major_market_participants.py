import pandas as pd

def format_data(data):
    df = pd.DataFrame(data)

    df['record_date'] = pd.to_datetime(df['record_date'])
    df['report_date'] = pd.to_datetime(df['report_date'])

    numeric_cols = [
        'spot_fwd_future_purch_amt', 'spot_fwd_future_sold_amt', 'assets_amt', 'liabilities_amt', 'call_options_bought_amt',
        'call_options_written_amt', 'put_options_bought_amt', 'put_options_written_amt', 'options_net_delta_amt', 'exchange_rate'
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
    'endpoint': '/v1/accounting/tb/fcp2_monthly_report_major_market_participants',
    'params': {
        'fields': ','.join([
            'record_date', 'foreign_currency_desc', 'foreign_currency_denom', 'report_date', 'spot_fwd_future_purch_amt',
            'spot_fwd_future_sold_amt', 'assets_amt', 'liabilities_amt', 'call_options_bought_amt', 'call_options_written_amt',
            'put_options_bought_amt', 'put_options_written_amt', 'options_net_delta_amt', 'exchange_rate', 'src_line_nbr',
            'record_fiscal_year', 'record_fiscal_quarter', 'record_calendar_year', 'record_calendar_quarter',
            'record_calendar_month', 'record_calendar_day'
        ]),
        'page[size]': 100
    },
    'formatter': format_data
}
