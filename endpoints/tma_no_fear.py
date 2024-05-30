import pandas as pd

def format_data(data):
    df = pd.DataFrame(data)

    df['record_date'] = pd.to_datetime(df['record_date'])

    numeric_cols = [
        'bal_of_131000_amt', 'bal_of_590000_amt',
        'src_line_nbr', 'record_fiscal_year', 'record_fiscal_quarter',
        'record_calendar_year', 'record_calendar_quarter', 'record_calendar_month', 'record_calendar_day'
    ]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col].str.replace(',', '').str.replace('$', ''), errors='coerce')

    return df.to_dict('records')

endpoint_details = {
    'endpoint': '/v1/accounting/od/tma_no_fear',
    'params': {
        'fields': ','.join([
            'record_date', 'partner_cd', 'agency_nm', 'bal_of_131000_amt', 'bal_of_590000_amt',
            'src_line_nbr', 'record_fiscal_year', 'record_fiscal_quarter',
            'record_calendar_year', 'record_calendar_quarter', 'record_calendar_month', 'record_calendar_day'
        ]),
        'page[size]': 100
    },
    'formatter': format_data
}
