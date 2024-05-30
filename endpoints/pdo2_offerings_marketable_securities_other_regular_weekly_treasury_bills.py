import pandas as pd

def format_data(data):
    df = pd.DataFrame(data)

    df['record_date'] = pd.to_datetime(df['record_date'])
    df['auction_date'] = pd.to_datetime(df['auction_date'])
    df['issue_date'] = pd.to_datetime(df['issue_date'])

    numeric_cols = [
        'tendered_mil_amt', 'acc_mil_amt', 'acc_yield_discount_margin', 'eq_price_for_notes_bonds'
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
    'endpoint': '/v1/accounting/tb/pdo2_offerings_marketable_securities_other_regular_weekly_treasury_bills',
    'params': {
        'fields': ','.join([
            'record_date', 'auction_date', 'issue_date', 'securities_desc',
            'period_to_final_maturity', 'tendered_mil_amt', 'acc_mil_amt', 'acc_yield_discount_margin',
            'eq_price_for_notes_bonds', 'src_line_nbr', 'record_fiscal_year', 'record_fiscal_quarter',
            'record_calendar_year', 'record_calendar_quarter', 'record_calendar_month', 'record_calendar_day'
        ]),
        'page[size]': 100
    },
    'formatter': format_data
}
