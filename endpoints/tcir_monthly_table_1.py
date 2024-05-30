import pandas as pd

def format_data(data):
    df = pd.DataFrame(data)

    df['record_date'] = pd.to_datetime(df['record_date'])

    # Define numeric columns and their conversion
    numeric_cols = ['src_line_nbr']
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # For columns that are strings and should remain strings, no need for additional conversion
    return df.to_dict('records')

endpoint_details = {
    'endpoint': '/v1/accounting/od/tcir_monthly_table_1',
    'params': {
        'fields': ','.join([
            'record_date', 'table_nm', 'maturity', 'previous_month_year',
            'rate_used_for_prev_month_year', 'current_month_year',
            'rate_ind_for_curr_month_year', 'rate_change', 'src_line_nbr'
        ]),
        'page[size]': 100
    },
    'formatter': format_data
}
