import pandas as pd

def format_data(data):
    df = pd.DataFrame(data)

    df['record_date'] = pd.to_datetime(df['record_date'])
    df['first_auc_date_single_price'] = pd.to_datetime(df['first_auc_date_single_price'])
    df['first_auc_date_low_rate'] = pd.to_datetime(df['first_auc_date_low_rate'])
    df['first_auc_date_high_rate'] = pd.to_datetime(df['first_auc_date_high_rate'])
    df['first_auc_date_high_offer'] = pd.to_datetime(df['first_auc_date_high_offer'])
    df['first_auc_date_high_bid_cover'] = pd.to_datetime(df['first_auc_date_high_bid_cover'])

    numeric_cols = [
        'low_rate_pct', 'high_rate_pct', 'high_offer_amt', 'high_bid_cover_ratio'
    ]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col].str.replace(',', '').str.replace('$', '').str.replace('%', ''), errors='coerce')

    df['src_line_nbr'] = pd.to_numeric(df['src_line_nbr'], errors='coerce')
    df['record_fiscal_year'] = pd.to_numeric(df['record_fiscal_year'], errors='coerce')
    df['record_fiscal_quarter'] = pd.to_numeric(df['record_fiscal_quarter'], errors='coerce')
    df['record_calendar_year'] = pd.to_numeric(df['record_calendar_year'], errors='coerce')
    df['record_calendar_quarter'] = pd.to_numeric(df['record_calendar_quarter'], errors='coerce')
    df['record_calendar_month'] = pd.to_numeric(df['record_calendar_month'], errors='coerce')
    df['record_calendar_day'] = pd.to_numeric(df['record_calendar_day'], errors='coerce')

    return df.to_dict('records')

endpoint_details = {
    'endpoint': '/v2/accounting/od/record_setting_auction',
    'params': {
        'fields': ','.join([
            'record_date', 'security_type', 'security_term', 'first_auc_date_single_price', 'low_rate_pct',
            'first_auc_date_low_rate', 'high_rate_pct', 'first_auc_date_high_rate', 'high_offer_amt',
            'first_auc_date_high_offer', 'high_bid_cover_ratio', 'first_auc_date_high_bid_cover', 'src_line_nbr',
            'record_fiscal_year', 'record_fiscal_quarter', 'record_calendar_year', 'record_calendar_quarter',
            'record_calendar_month', 'record_calendar_day'
        ]),
        'page[size]': 100
    },
    'formatter': format_data
}
