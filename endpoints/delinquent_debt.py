import pandas as pd

def format_data(data):
    df = pd.DataFrame(data)
    
    # Convert date columns to datetime
    df['record_date'] = pd.to_datetime(df['record_date'])
    
    # Convert numeric columns to appropriate types
    currency_cols = [
        'ddebt_1_to_30_days_amt', 'ddebt_31_to_60_days_amt', 'ddebt_61_to_90_days_amt', 'ddebt_91_to_120_days_amt',
        'ddebt_121_to_150_days_amt', 'ddebt_151_to_180_days_amt', 'ddebt_181_to_365_days_amt', 'ddebt_1_to_2_yrs_amt',
        'ddebt_2_to_6_yrs_amt', 'ddebt_6_to_10_yrs_amt', 'ddebt_over_10_yrs_amt', 'ddebt_by_age_total_amt',
        'ddebt_commercial_amt', 'ddebt_consumer_amt', 'ddebt_foreign_sovereign_amt', 'ddebt_state_local_amt',
        'ddebt_by_category_total_amt', 'credit_bureau_commercial_amt', 'credit_bureau_consumer_amt', 'credit_bureau_total_amt',
        'ddebt_1_120_bankruptcy_amt', 'ddebt_1_120_forbear_appeal_amt', 'ddebt_1_120_foreclosure_amt', 'ddebt_1_120_prv_cltn_agcy_amt',
        'ddebt_1_120_litigation_amt', 'ddebt_1_120_intern_offset_amt', 'ddebt_1_120_wage_garnish_amt', 'ddebt_1_120_treas_cs_amt',
        'ddebt_1_120_treas_offset_amt', 'ddebt_1_120_agency_amt', 'ddebt_1_120_other_amt', 'ddebt_1_120_total_amt',
        'top_elig_ddebt_over_120_amt', 'top_elig_cnc_amt', 'top_elig_120_cnc_total_amt', 'top_inelig_bankruptcy_amt',
        'top_inelig_forbear_appeal_amt', 'top_inelig_foreclosure_amt', 'top_inelig_other_amt', 'top_elig_total_amt',
        'top_expt_foreign_sovereign_amt', 'top_expt_state_local_amt', 'top_expt_other_amt', 'top_expt_agency_req_ref_amt',
        'top_expt_agency_direct_ref_amt', 'top_expt_cs_ref_amt', 'top_referred_total_amt', 'cs_elig_ddebt_over_180_amt',
        'cs_elig_cnc_amt', 'cs_elig_180_cnc_total_amt', 'cs_inelig_bankruptcy_amt', 'cs_inelig_forbear_appeal_amt',
        'cs_inelig_foreclosure_amt', 'cs_inelig_other_amt', 'cs_elig_total_amt', 'cs_expt_foreign_sovereign_amt',
        'cs_expt_litigation_amt', 'cs_expt_prv_cltn_agcy_amt', 'cs_expt_internal_offset_amt', 'cs_expt_exempt_treasury_amt',
        'cs_expt_returned_amt', 'cs_expt_other_amt', 'cs_expt_req_ref_amt', 'cs_expt_ref_amt', 'cs_referred_total_amt'
    ]
    number_cols = [
        'ddebt_1_to_30_days_cnt', 'ddebt_31_to_60_days_cnt', 'ddebt_61_to_90_days_cnt', 'ddebt_91_to_120_days_cnt',
        'ddebt_121_to_150_days_cnt', 'ddebt_151_to_180_days_cnt', 'ddebt_181_to_365_days_cnt', 'ddebt_1_to_2_yrs_cnt',
        'ddebt_2_to_6_yrs_cnt', 'ddebt_6_to_10_yrs_cnt', 'ddebt_over_10_yrs_cnt', 'ddebt_by_age_total_cnt',
        'ddebt_commercial_cnt', 'ddebt_consumer_cnt', 'ddebt_foreign_sovereign_cnt', 'ddebt_state_local_cnt',
        'ddebt_by_category_total_cnt', 'credit_bureau_commercial_cnt', 'credit_bureau_consumer_cnt', 'credit_bureau_total_cnt',
        'ddebt_1_120_bankruptcy_cnt', 'ddebt_1_120_forbear_appeal_cnt', 'ddebt_1_120_foreclosure_cnt', 'ddebt_1_120_prv_cltn_agcy_cnt',
        'ddebt_1_120_litigation_cnt', 'ddebt_1_120_intern_offset_cnt', 'ddebt_1_120_wage_garnish_cnt', 'ddebt_1_120_treas_cs_cnt',
        'ddebt_1_120_treas_offset_cnt', 'ddebt_1_120_agency_cnt', 'ddebt_1_120_other_cnt', 'ddebt_1_120_total_cnt',
        'top_elig_ddebt_over_120_cnt', 'top_elig_cnc_cnt', 'top_elig_120_cnc_total_cnt', 'top_inelig_bankruptcy_cnt',
        'top_inelig_forbear_appeal_cnt', 'top_inelig_foreclosure_cnt', 'top_inelig_other_cnt', 'top_elig_total_cnt',
        'top_expt_foreign_sovereign_cnt', 'top_expt_state_local_cnt', 'top_expt_other_cnt', 'top_expt_agency_req_ref_cnt',
        'top_expt_agency_direct_ref_cnt', 'top_expt_cs_ref_cnt', 'top_referred_total_cnt', 'cs_elig_ddebt_over_180_cnt',
        'cs_elig_cnc_cnt', 'cs_elig_180_cnc_total_cnt', 'cs_inelig_bankruptcy_cnt', 'cs_inelig_forbear_appeal_cnt',
        'cs_inelig_foreclosure_cnt', 'cs_inelig_other_cnt', 'cs_elig_total_cnt', 'cs_expt_foreign_sovereign_cnt',
        'cs_expt_litigation_cnt', 'cs_expt_prv_cltn_agcy_cnt', 'cs_expt_internal_offset_cnt', 'cs_expt_exempt_treasury_cnt',
        'cs_expt_returned_cnt', 'cs_expt_other_cnt', 'cs_expt_req_ref_cnt', 'cs_expt_ref_cnt', 'cs_referred_total_cnt'
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
    'endpoint': '/v2/debt/tror/delinquent_debt',
    'params': {
        'fields': ','.join([
            'record_date', 'receivable_type_description', 'receivable_type_id', 'funding_type_description', 
            'funding_type_id', 'ddebt_1_to_30_days_amt', 'ddebt_1_to_30_days_cnt', 'ddebt_31_to_60_days_amt', 
            'ddebt_31_to_60_days_cnt', 'ddebt_61_to_90_days_amt', 'ddebt_61_to_90_days_cnt', 'ddebt_91_to_120_days_amt', 
            'ddebt_91_to_120_days_cnt', 'ddebt_121_to_150_days_amt', 'ddebt_121_to_150_days_cnt', 'ddebt_151_to_180_days_amt', 
            'ddebt_151_to_180_days_cnt', 'ddebt_181_to_365_days_amt', 'ddebt_181_to_365_days_cnt', 'ddebt_1_to_2_yrs_amt', 
            'ddebt_1_to_2_yrs_cnt', 'ddebt_2_to_6_yrs_amt', 'ddebt_2_to_6_yrs_cnt', 'ddebt_6_to_10_yrs_amt', 
            'ddebt_6_to_10_yrs_cnt', 'ddebt_over_10_yrs_amt', 'ddebt_over_10_yrs_cnt', 'ddebt_by_age_total_amt', 
            'ddebt_by_age_total_cnt', 'ddebt_commercial_amt', 'ddebt_commercial_cnt', 'ddebt_consumer_amt', 'ddebt_consumer_cnt', 
            'ddebt_foreign_sovereign_amt', 'ddebt_foreign_sovereign_cnt', 'ddebt_state_local_amt', 'ddebt_state_local_cnt', 
            'ddebt_by_category_total_amt', 'ddebt_by_category_total_cnt', 'credit_bureau_commercial_amt', 'credit_bureau_commercial_cnt', 
            'credit_bureau_consumer_amt', 'credit_bureau_consumer_cnt', 'credit_bureau_total_amt', 'credit_bureau_total_cnt', 
            'ddebt_1_120_bankruptcy_amt', 'ddebt_1_120_bankruptcy_cnt', 'ddebt_1_120_forbear_appeal_amt', 'ddebt_1_120_forbear_appeal_cnt', 
            'ddebt_1_120_foreclosure_amt', 'ddebt_1_120_foreclosure_cnt', 'ddebt_1_120_prv_cltn_agcy_amt', 'ddebt_1_120_prv_cltn_agcy_cnt', 
            'ddebt_1_120_litigation_amt', 'ddebt_1_120_litigation_cnt', 'ddebt_1_120_intern_offset_amt', 'ddebt_1_120_intern_offset_cnt', 
            'ddebt_1_120_wage_garnish_amt', 'ddebt_1_120_wage_garnish_cnt', 'ddebt_1_120_treas_cs_amt', 'ddebt_1_120_treas_cs_cnt', 
            'ddebt_1_120_treas_offset_amt', 'ddebt_1_120_treas_offset_cnt', 'ddebt_1_120_agency_amt', 'ddebt_1_120_agency_cnt', 
            'ddebt_1_120_other_amt', 'ddebt_1_120_other_cnt', 'ddebt_1_120_total_amt', 'ddebt_1_120_total_cnt', 'top_elig_ddebt_over_120_amt', 
            'top_elig_ddebt_over_120_cnt', 'top_elig_cnc_amt', 'top_elig_cnc_cnt', 'top_elig_120_cnc_total_amt', 'top_elig_120_cnc_total_cnt', 
            'top_inelig_bankruptcy_amt', 'top_inelig_bankruptcy_cnt', 'top_inelig_forbear_appeal_amt', 'top_inelig_forbear_appeal_cnt', 
            'top_inelig_foreclosure_amt', 'top_inelig_foreclosure_cnt', 'top_inelig_other_amt', 'top_inelig_other_cnt', 'top_elig_total_amt', 
            'top_elig_total_cnt', 'top_expt_foreign_sovereign_amt', 'top_expt_foreign_sovereign_cnt', 'top_expt_state_local_amt', 
            'top_expt_state_local_cnt', 'top_expt_other_amt', 'top_expt_other_cnt', 'top_expt_agency_req_ref_amt', 'top_expt_agency_req_ref_cnt', 
            'top_expt_agency_direct_ref_amt', 'top_expt_agency_direct_ref_cnt', 'top_expt_cs_ref_amt', 'top_expt_cs_ref_cnt', 'top_referred_total_amt', 
            'top_referred_total_cnt', 'cs_elig_ddebt_over_180_amt', 'cs_elig_ddebt_over_180_cnt', 'cs_elig_cnc_amt', 'cs_elig_cnc_cnt', 
            'cs_elig_180_cnc_total_amt', 'cs_elig_180_cnc_total_cnt', 'cs_inelig_bankruptcy_amt', 'cs_inelig_bankruptcy_cnt', 
            'cs_inelig_forbear_appeal_amt', 'cs_inelig_forbear_appeal_cnt', 'cs_inelig_foreclosure_amt', 'cs_inelig_foreclosure_cnt', 
            'cs_inelig_other_amt', 'cs_inelig_other_cnt', 'cs_elig_total_amt', 'cs_elig_total_cnt', 'cs_expt_foreign_sovereign_amt', 
            'cs_expt_foreign_sovereign_cnt', 'cs_expt_litigation_amt', 'cs_expt_litigation_cnt', 'cs_expt_prv_cltn_agcy_amt', 
            'cs_expt_prv_cltn_agcy_cnt', 'cs_expt_internal_offset_amt', 'cs_expt_internal_offset_cnt', 'cs_expt_exempt_treasury_amt', 
            'cs_expt_exempt_treasury_cnt', 'cs_expt_returned_amt', 'cs_expt_returned_cnt', 'cs_expt_other_amt', 'cs_expt_other_cnt', 
            'cs_expt_req_ref_amt', 'cs_expt_req_ref_cnt', 'cs_expt_ref_amt', 'cs_expt_ref_cnt', 'cs_referred_total_amt', 'cs_referred_total_cnt', 
            'src_line_nbr', 'record_fiscal_year', 'record_fiscal_quarter', 'record_calendar_year', 'record_calendar_quarter', 
            'record_calendar_month', 'record_calendar_day'
        ]),
        'page[size]': 100
    },
    'formatter': format_data
}
