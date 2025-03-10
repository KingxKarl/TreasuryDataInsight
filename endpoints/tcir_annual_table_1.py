import pandas as pd

def format_data(data):
    df = pd.DataFrame(data)

    df['record_date'] = pd.to_datetime(df['record_date'])

    df['src_line_nbr'] = pd.to_numeric(df['src_line_nbr'], errors='coerce')
    df['fiscal_year'] = pd.to_numeric(df['fiscal_year'], errors='coerce')

    return df.to_dict('records')

endpoint_details = {
    'endpoint': '/v1/accounting/od/tcir_annual_table_1',
    'params': {
        'fields': ','.join([
            'record_date', 'table_nm', 'from_and_including', 'up_to_but_not_including', 
            'fiscal_year', 'fiscal_year_rate', 'src_line_nbr'
        ]),
        'page[size]': 100
    },
    'formatter': format_data
}
