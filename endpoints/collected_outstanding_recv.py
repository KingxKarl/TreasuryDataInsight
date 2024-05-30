import pandas as pd

def format_data(data):
    df = pd.DataFrame(data)
    
    # Convert date columns to datetime
    df['record_date'] = pd.to_datetime(df['record_date'])
    
    # Convert numeric columns to appropriate types
    currency_cols = [
        'beginning_fiscal_year_amt', 'new_receivables_amt', 'accruals_amt', 'collections_total_amt',
        'collections_agency_amt', 'collections_third_amt', 'collections_asset_amt', 'collections_top_cs_amt',
        'collections_sale_foreclose_amt', 'collections_doj_amt', 'collections_other_amt',
        'adjustments_total_amt', 'adjustments_reclassified_amt', 'adjustments_asset_sales_amt', 'adjustments_consolidations_amt',
        'adjustments_foreclosure_amt', 'adjustments_resinstated_amt', 'written_off_total_amt', 'currently_not_collectible_amt',
        'written_off_closed_out_amt', 'end_bal_amt', 'end_foreign_sovereign_amt', 'end_state_local_amt', 'end_rescheduled_ddebt_amt',
        'end_rescheduled_non_ddebt_amt', 'end_interest_late_charge_amt', 'end_a129_exclusions_amt'
    ]
    number_cols = [
        'beginning_fiscal_year_cnt', 'new_receivables_cnt', 'adjustments_total_cnt', 'written_off_total_cnt',
        'currently_not_collectible_cnt', 'written_off_closed_out_cnt', 'end_bal_cnt', 'end_foreign_sovereign_cnt', 'end_state_local_cnt',
        'end_rescheduled_ddebt_cnt', 'end_rescheduled_non_ddebt_cnt', 'end_a129_exclusions_cnt'
    ]

    for col in currency_cols:
        df[col] = pd.to_numeric(df[col].str.replace(',', '').str.replace('$', ''), errors='coerce')
    for col in number_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    df['src_line_nbr'] = pd.to_numeric(df['src_line_nbr'], errors='coerce')
    df['record_fiscal_year'] = pd.to_numeric(df['record_fiscal_year'], errors='coerce')
    df['record_fiscal_quarter'] = pd.to_numeric(df['record_fiscal_quarter'], errors='coerce')
    df['record_calendar_year'] = pd.to_numeric(df['record_calendar_year'], errors='coerce')
    df['record_calendar_quarter'] = pd.to_numeric(df['record_calendar_quarter'], errors='coerce')
    df['record_calendar_month'] = pd.to_numeric(df['record_calendar_month'], errors='coerce')
    df['record_calendar_day'] = pd.to_numeric(df['record_calendar_day'], errors='coerce')
    
    return df.to_dict('records')

endpoint_details = {
    'endpoint': '/v2/debt/tror/collected_outstanding_recv',
    'params': {
        'fields': ','.join([
            'record_date', 'receivable_type_description', 'receivable_type_id', 'funding_type_description', 
            'funding_type_id', 'beginning_fiscal_year_amt', 'beginning_fiscal_year_cnt', 'new_receivables_amt', 
            'new_receivables_cnt', 'accruals_amt', 'collections_total_amt', 'collections_agency_amt', 
            'collections_third_amt', 'collections_asset_amt', 'collections_top_cs_amt', 
            'collections_sale_foreclose_amt', 'collections_doj_amt', 'collections_other_amt', 
            'adjustments_total_amt', 'adjustments_total_cnt', 'adjustments_reclassified_amt', 
            'adjustments_asset_sales_amt', 'adjustments_consolidations_amt', 'adjustments_foreclosure_amt', 
            'adjustments_resinstated_amt', 'written_off_total_amt', 'written_off_total_cnt', 
            'currently_not_collectible_amt', 'currently_not_collectible_cnt', 'written_off_closed_out_amt', 
            'written_off_closed_out_cnt', 'end_bal_amt', 'end_bal_cnt', 'end_foreign_sovereign_amt', 
            'end_foreign_sovereign_cnt', 'end_state_local_amt', 'end_state_local_cnt', 
            'end_rescheduled_ddebt_amt', 'end_rescheduled_ddebt_cnt', 'end_rescheduled_non_ddebt_amt', 
            'end_rescheduled_non_ddebt_cnt', 'end_interest_late_charge_amt', 'end_a129_exclusions_amt', 
            'end_a129_exclusions_cnt', 'src_line_nbr', 'record_fiscal_year', 'record_fiscal_quarter', 
            'record_calendar_year', 'record_calendar_quarter', 'record_calendar_month', 'record_calendar_day'
        ]),
        'page[size]': 100
    },
    'formatter': format_data
}
