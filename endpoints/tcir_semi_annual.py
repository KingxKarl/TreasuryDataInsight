import pandas as pd

def format_data(data):
    df = pd.DataFrame(data)

    df['record_date'] = pd.to_datetime(df['record_date'])
    df['effective_start_date'] = pd.to_datetime(df['effective_start_date'])

    numeric_cols = ['src_line_nbr']
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    return df.to_dict('records')

endpoint_details = {
    'endpoint': '/v1/accounting/od/tcir_semi_annual',
    'params': {
        'fields': ','.join([
            'record_date', 'legislation', 'effective_start_date', 'effective_date_range',
            'calendar_year_rate', 'src_line_nbr'
        ]),
        'page[size]': 100
    },
    'formatter': format_data
}
