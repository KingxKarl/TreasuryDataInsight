import pandas as pd

def format_data(data):
    df = pd.DataFrame(data)

    df['record_date'] = pd.to_datetime(df['record_date'])

    numeric_cols = [
        'current_month_net_txn_amt', 'fytd_net_txn_amt', 'prior_fytd_net_txn_amt',
        'begin_year_acct_bal_amt', 'begin_month_acct_bal_amt', 'close_month_acct_bal_amt'
    ]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col].str.replace(',', '').str.replace('$', ''), errors='coerce')

    df['src_line_nbr'] = pd.to_numeric(df['src_line_nbr'], errors='coerce')
    df['record_fiscal_year'] = pd.to_numeric(df['record_fiscal_year'], errors='coerce')
    df['record_fiscal_quarter'] = pd.to_numeric(df['record_fiscal_quarter'], errors='coerce')
    df['record_calendar_year'] = pd.to_numeric(df['record_calendar_year'], errors='coerce')
    df['record_calendar_quarter'] = pd.to_numeric(df['record_calendar_quarter'], errors='coerce')
    df['record_calendar_month'] = pd.to_numeric(df['record_calendar_month'], errors='coerce')
    df['record_calendar_day'] = pd.to_numeric(df['record_calendar_day'], errors='coerce')

    return df.to_dict('records')

endpoint_details = {
    'endpoint': '/v1/accounting/mts/mts_table_6c',
    'params': {
        'fields': ','.join([
            'record_date', 'parent_id', 'classification_id', 'classification_desc', 
            'current_month_net_txn_amt', 'fytd_net_txn_amt', 'prior_fytd_net_txn_amt',
            'begin_year_acct_bal_amt', 'begin_month_acct_bal_amt', 'close_month_acct_bal_amt',
            'table_nbr', 'src_line_nbr', 'print_order_nbr', 'line_code_nbr', 'data_type_cd', 'record_type_cd',
            'sequence_level_nbr', 'sequence_number_cd', 'record_fiscal_year', 'record_fiscal_quarter',
            'record_calendar_year', 'record_calendar_quarter', 'record_calendar_month', 'record_calendar_day'
        ]),
        'page[size]': 100
    },
    'formatter': format_data
}
