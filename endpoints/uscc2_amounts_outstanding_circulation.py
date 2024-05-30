import pandas as pd

def format_data(data):
    df = pd.DataFrame(data)

    df['record_date'] = pd.to_datetime(df['record_date'])
    df['currency_as_of_date'] = pd.to_datetime(df['currency_as_of_date'])

    numeric_cols = [
        'total_currency_amt', 'federal_reserve_notes_amt', 'us_notes_amt', 'currency_no_longer_issued_amt',
        'per_capita_amt', 'src_line_nbr', 'record_fiscal_year', 'record_fiscal_quarter', 'record_calendar_year',
        'record_calendar_quarter', 'record_calendar_month', 'record_calendar_day'
    ]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col].str.replace(',', '').str.replace('$', ''), errors='coerce')

    return df.to_dict('records')

endpoint_details = {
    'endpoint': '/v1/accounting/tb/uscc2_amounts_outstanding_circulation',
    'params': {
        'fields': ','.join([
            'record_date', 'currency_as_of_date', 'currency_denom', 'total_currency_amt',
            'federal_reserve_notes_amt', 'us_notes_amt', 'currency_no_longer_issued_amt',
            'per_capita_amt', 'src_line_nbr', 'record_fiscal_year', 'record_fiscal_quarter',
            'record_calendar_year', 'record_calendar_quarter', 'record_calendar_month', 'record_calendar_day'
        ]),
        'page[size]': 100
    },
    'formatter': format_data
}
