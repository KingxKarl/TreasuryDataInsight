import pandas as pd

def format_data(data):
    df = pd.DataFrame(data)

    df['record_date'] = pd.to_datetime(df['record_date'])

    numeric_cols = [
        'gross_amt', 'net_amt', 'gross_cnt', 'net_cnt', 'src_line_nbr',
        'record_fiscal_year', 'record_fiscal_quarter', 'record_calendar_year',
        'record_calendar_quarter', 'record_calendar_month', 'record_calendar_day'
    ]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col].str.replace(',', '').str.replace('$', ''), errors='coerce')

    return df.to_dict('records')

endpoint_details = {
    'endpoint': '/v1/debt/top/top_federal',
    'params': {
        'fields': ','.join([
            'record_date', 'creditor_agency_nm', 'creditor_agency_id', 'agency_type', 'agency_site',
            'agency_site_nm', 'source_agency', 'source_agency_1', 'source_agency_site',
            'payment_agency_nm', 'payment_agency', 'agency_type_cd', 'payment_source_desc', 'payment_source_cd',
            'payment_category', 'payment_type_desc', 'payment_type_cd', 'payment_type_id', 'debt_type_cd',
            'debt_type_desc', 'taxable', 'gross_amt', 'net_amt', 'gross_cnt', 'net_cnt',
            'record_fiscal_year', 'record_fiscal_quarter', 'record_calendar_year', 'record_calendar_quarter',
            'record_calendar_month', 'record_calendar_day'
        ]),
        'page[size]': 100
    },
    'formatter': format_data
}
