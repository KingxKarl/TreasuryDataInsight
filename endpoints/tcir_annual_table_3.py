import pandas as pd

def format_data(data):
    df = pd.DataFrame(data)

    df['record_date'] = pd.to_datetime(df['record_date'])

    df['src_line_nbr'] = pd.to_numeric(df['src_line_nbr'], errors='coerce')
    df['fiscal_year'] = pd.to_numeric(df['fiscal_year'], errors='coerce')

    return df.to_dict('records')

endpoint_details = {
    'endpoint': '/v1/accounting/od/tcir_annual_table_3',
    'params': {
        'fields': ','.join([
            'record_date', 'table_nm', 'legislation', 'fiscal_year', 'fiscal_year_rate', 
            'adj_rate_nearest_eighth_pct', 'src_line_nbr'
        ]),
        'page[size]': 100
    },
    'formatter': format_data
}
