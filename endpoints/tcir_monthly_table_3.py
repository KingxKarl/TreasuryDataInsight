import pandas as pd

def format_data(data):
    df = pd.DataFrame(data)

    df['record_date'] = pd.to_datetime(df['record_date'])

    numeric_cols = ['src_line_nbr']
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    return df.to_dict('records')

endpoint_details = {
    'endpoint': '/v1/accounting/od/tcir_monthly_table_3',
    'params': {
        'fields': ','.join([
            'record_date', 'table_nm', 'legislation', 'monthly_rate', 'src_line_nbr'
        ]),
        'page[size]': 100
    },
    'formatter': format_data
}