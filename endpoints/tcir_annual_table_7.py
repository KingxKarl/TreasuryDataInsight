import pandas as pd

def format_data(data):
    df = pd.DataFrame(data)

    df['record_date'] = pd.to_datetime(df['record_date'])

    df['src_line_nbr'] = pd.to_numeric(df['src_line_nbr'], errors='coerce')
    df['calendar_year'] = pd.to_numeric(df['calendar_year'], errors='coerce')

    return df.to_dict('records')

endpoint_details = {
    'endpoint': '/v1/accounting/od/tcir_annual_table_7',
    'params': {
        'fields': ','.join([
            'record_date', 'table_nm', 'legislation', 'calendar_year', 'calendar_year_rate', 'src_line_nbr'
        ]),
        'page[size]': 100
    },
    'formatter': format_data
}
