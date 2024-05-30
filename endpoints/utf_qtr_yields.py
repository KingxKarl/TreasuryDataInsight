import pandas as pd

def format_data(data):
    df = pd.DataFrame(data)

    df['record_date'] = pd.to_datetime(df['record_date'])

    numeric_cols = [
        'yield_pct', 'src_line_nbr', 'record_fiscal_year', 'record_fiscal_quarter',
        'record_calendar_year', 'record_calendar_quarter', 'record_calendar_month', 'record_calendar_day'
    ]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col].str.replace(',', '').str.replace('$', ''), errors='coerce')

    return df.to_dict('records')

endpoint_details = {
    'endpoint': '/v2/accounting/od/utf_qtr_yields',
    'params': {
        'fields': ','.join([
            'record_date', 'quarter_desc', 'yield_pct', 'src_line_nbr', 'record_fiscal_year', 'record_fiscal_quarter',
            'record_calendar_year', 'record_calendar_quarter', 'record_calendar_month', 'record_calendar_day'
        ]),
        'page[size]': 100
    },
    'formatter': format_data
}
