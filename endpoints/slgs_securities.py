import pandas as pd

def format_data(data):
    df = pd.DataFrame(data)

    df['record_date'] = pd.to_datetime(df['record_date'])
    
    numeric_cols = [
        'new_subscriptions_cnt', 'new_subscriptions_amt', 'cancelled_subscriptions_cnt', 'cancelled_subscriptions_amt',
        'issues_0_3_mos_cnt', 'issues_0_3_mos_amt', 'issues_3_6_mos_cnt', 'issues_3_6_mos_amt',
        'issues_6_mos_to_2_yrs_cnt', 'issues_6_mos_to_2_yrs_amt', 'issues_2_5_yrs_cnt', 'issues_2_5_yrs_amt',
        'issues_5_10_yrs_cnt', 'issues_5_10_yrs_amt', 'issues_over_10_yrs_cnt', 'issues_over_10_yrs_amt',
        'outstanding_0_3_mos_cnt', 'outstanding_0_3_mos_amt', 'outstanding_3_6_mos_cnt', 'outstanding_3_6_mos_amt',
        'outstanding_6_mos_to_2_yrs_cnt', 'outstanding_6_mos_to_2_yrs_amt', 'outstanding_2_5_yrs_cnt',
        'outstanding_2_5_yrs_amt', 'outstanding_5_10_yrs_cnt', 'outstanding_5_10_yrs_amt', 
        'outstanding_over_10_yrs_cnt', 'outstanding_over_10_yrs_amt', 'demand_deposit_redemptions_cnt',
        'demand_deposit_redemptions_amt', 'time_deposit_redemptions_cnt', 'time_deposit_redemptions_amt'
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
    'endpoint': '/v1/accounting/od/slgs_securities',
    'params': {
        'fields': ','.join([
            'record_date', 'new_subscriptions_cnt', 'new_subscriptions_amt', 'cancelled_subscriptions_cnt', 
            'cancelled_subscriptions_amt', 'issues_0_3_mos_cnt', 'issues_0_3_mos_amt', 'issues_3_6_mos_cnt', 
            'issues_3_6_mos_amt', 'issues_6_mos_to_2_yrs_cnt', 'issues_6_mos_to_2_yrs_amt', 'issues_2_5_yrs_cnt', 
            'issues_2_5_yrs_amt', 'issues_5_10_yrs_cnt', 'issues_5_10_yrs_amt', 'issues_over_10_yrs_cnt', 
            'issues_over_10_yrs_amt', 'outstanding_0_3_mos_cnt', 'outstanding_0_3_mos_amt', 
            'outstanding_3_6_mos_cnt', 'outstanding_3_6_mos_amt', 'outstanding_6_mos_to_2_yrs_cnt', 
            'outstanding_6_mos_to_2_yrs_amt', 'outstanding_2_5_yrs_cnt', 'outstanding_2_5_yrs_amt', 
            'outstanding_5_10_yrs_cnt', 'outstanding_5_10_yrs_amt', 'outstanding_over_10_yrs_cnt', 
            'outstanding_over_10_yrs_amt', 'demand_deposit_redemptions_cnt', 'demand_deposit_redemptions_amt', 
            'time_deposit_redemptions_cnt', 'time_deposit_redemptions_amt', 'src_line_nbr', 'record_fiscal_year', 
            'record_fiscal_quarter', 'record_calendar_year', 'record_calendar_quarter', 'record_calendar_month', 
            'record_calendar_day'
        ]),
        'page[size]': 100
    },
    'formatter': format_data
}
