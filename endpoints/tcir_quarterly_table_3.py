import pandas as pd

def format_data(data):
    df = pd.DataFrame(data)

    df['record_date'] = pd.to_datetime(df['record_date'])
    df['maturity_or_next_int_reset_dt'] = pd.to_datetime(df['maturity_or_next_int_reset_dt'])

    numeric_cols = ['src_line_nbr']
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    return df.to_dict('records')

endpoint_details = {
    'endpoint': '/v1/accounting/od/tcir_quarterly_table_3',
    'params': {
        'fields': ','.join([
            'record_date', 'table_nm', 'term', 'maturity_or_next_int_reset_dt',
            'applicable_treasury_rate', 'rate_adjustment', 'contract_int_rate', 'src_line_nbr'
        ]),
        'page[size]': 100
    },
    'formatter': format_data
}
