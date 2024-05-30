import pandas as pd

def format_data(data):
    df = pd.DataFrame(data)

    df['record_date'] = pd.to_datetime(df['record_date'])

    numeric_cols = ['dollar_amt_sold', 'src_line_nbr', 'year']
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col].str.replace(',', '').str.replace('$', ''), errors='coerce')

    return df.to_dict('records')

endpoint_details = {
    'endpoint': '/v1/accounting/od/tcir_quarterly_table_1',
    'params': {
        'fields': ','.join([
            'record_date', 'table_nm', 'month', 'year', 'dollar_amt_sold',
            'avg_yield_to_maturity', 'src_line_nbr'
        ]),
        'page[size]': 100
    },
    'formatter': format_data
}
