import pandas as pd

def format_data(data):
    df = pd.DataFrame(data)

    df['redemp_period'] = pd.to_datetime(df['redemp_period'])
    df['redemption_year'] = pd.to_numeric(df['redemption_year'], errors='coerce')
    df['redemption_month'] = pd.to_numeric(df['redemption_month'], errors='coerce')
    df['issue_year'] = pd.to_numeric(df['issue_year'], errors='coerce')

    numeric_cols = [
        'issue_jan_amt', 'issue_feb_amt', 'issue_mar_amt', 'issue_apr_amt', 
        'issue_may_amt', 'issue_jun_amt', 'issue_jul_amt', 'issue_aug_amt', 
        'issue_sep_amt', 'issue_oct_amt', 'issue_nov_amt', 'issue_dec_amt'
    ]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col].str.replace(',', '').str.replace('$', ''), errors='coerce')

    df['src_line_nbr'] = pd.to_numeric(df['src_line_nbr'], errors='coerce')

    return df.to_dict('records')

endpoint_details = {
    'endpoint': '/v2/accounting/od/sb_value',
    'params': {
        'fields': ','.join([
            'redemp_period', 'redemption_year', 'redemption_month', 'series_cd', 
            'issue_year', 'issue_jan_amt', 'issue_feb_amt', 'issue_mar_amt', 
            'issue_apr_amt', 'issue_may_amt', 'issue_jun_amt', 'issue_jul_amt', 
            'issue_aug_amt', 'issue_sep_amt', 'issue_oct_amt', 'issue_nov_amt', 
            'issue_dec_amt', 'src_line_nbr'
        ]),
        'page[size]': 100
    },
    'formatter': format_data
}
