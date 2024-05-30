import pandas as pd

def format_data(data):
    df = pd.DataFrame(data)

    df['original_auction_date'] = pd.to_datetime(df['original_auction_date'])
    df['maturity_date'] = pd.to_datetime(df['maturity_date'])
    df['original_issue_date'] = pd.to_datetime(df['original_issue_date'])
    df['dated_date'] = pd.to_datetime(df['dated_date'])

    numeric_cols = ['ref_cpi_on_dated_date', 'src_line_nbr']
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col].str.replace(',', '').str.replace('$', ''), errors='coerce')

    return df.to_dict('records')

endpoint_details = {
    'endpoint': '/v1/accounting/od/tips_cpi_data_summary',
    'params': {
        'fields': ','.join([
            'cusip', 'interest_rate', 'security_term', 'original_auction_date', 'maturity_date',
            'series', 'original_issue_date', 'dated_date', 'ref_cpi_on_dated_date', 'additional_issue_date'
        ]),
        'page[size]': 100
    },
    'formatter': format_data
}
