import pandas as pd

def format_data(data):
    df = pd.DataFrame(data)

    df['record_date'] = pd.to_datetime(df['record_date'])
    df['original_dated_date'] = pd.to_datetime(df['original_dated_date'])
    df['original_issue_date'] = pd.to_datetime(df['original_issue_date'])
    df['maturity_date'] = pd.to_datetime(df['maturity_date'])
    df['start_of_accrual_period'] = pd.to_datetime(df['start_of_accrual_period'])
    df['end_of_accrual_period'] = pd.to_datetime(df['end_of_accrual_period'])

    numeric_cols = [
        'spread', 'daily_index', 'daily_int_accrual_rate', 'daily_accrued_int_per100', 'accr_int_per100_pmt_period'
    ]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col].str.replace(',', '').str.replace('$', ''), errors='coerce')

    return df.to_dict('records')

endpoint_details = {
    'endpoint': '/v1/accounting/od/frn_daily_indexes',
    'params': {
        'fields': ','.join([
            'record_date', 'frn', 'cusip', 'original_dated_date', 'original_issue_date', 'maturity_date',
            'spread', 'start_of_accrual_period', 'end_of_accrual_period', 'daily_index', 'daily_int_accrual_rate',
            'daily_accrued_int_per100', 'accr_int_per100_pmt_period'
        ]),
        'page[size]': 100
    },
    'formatter': format_data
}
