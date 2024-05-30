from fetch_data import fetch_data_with_pagination, fetch_initial_data, get_most_recent_record_date
from store_data import store_data_in_mongodb
import importlib
import pymongo
from datetime import timedelta

endpoints = [
    'adjustment_public_debt_transactions_cash_basis',
    'agriculture_disaster_relief_trust_fund_expected',
    'agriculture_disaster_relief_trust_fund_results',
    'airport_airway_trust_fund_expected',
    'airport_airway_trust_fund_results',
    'avg_interest_rates',
    'balance_sheets',
    'black_lung_disability_trust_fund_expected',
    'black_lung_disability_trust_fund_results',
    'cash_balance',
    'collected_outstanding_recv',
    'data_act_compliance',
    'debt_outstanding',
    'debt_subject_to_limit',
    'debt_to_penny',
    'delinquent_debt',
    'deposits_withdrawals_operating_cash',
    'esf1_balances',
    'esf2_statement_net_cost',
    'fbp_gl_borrowing_balances',
    'fbp_gl_repay_advance_balances',
    'fcp1_weekly_report_major_market_participants',
    'fcp2_monthly_report_major_market_participants',
    'fcp3_quarterly_report_large_market_participants',
    'federal_maturity_rates',
    'federal_tax_deposits',
    'ffo5_internal_revenue_by_state',
    'ffo6_customs_border_protection_collections',
    'fip_statement_of_account_table1',
    'fip_statement_of_account_table2',
    'fip_statement_of_account_table3',
    'frn_daily_indexes',
    'gift_contributions',
    'gold_reserve',
    'harbor_maintenance_trust_fund_expected',
    'harbor_maintenance_trust_fund_results',
    'hazardous_substance_superfund_expected',
    'hazardous_substance_superfund_results',
    'highway_trust_fund',
    'highway_trust_fund_expected',
    'highway_trust_fund_results',
    'income_tax_refunds_issued',
    'inland_waterways_trust_fund_expected',
    'inland_waterways_trust_fund_results',
    'insurance_amounts',
    'interest_cost_fund',
    'interest_expense',
    'interest_uninvested',
    'inter_agency_tax_transfers',
    'jfics_congress_report',
    'leaking_underground_storage_tank_trust_fund_expected',
    'leaking_underground_storage_tank_trust_fund_results',
    'long_term_projections',
    'mts_table_1',
    'mts_table_2',
    'mts_table_3',
    'mts_table_4',
    'mts_table_5',
    'mts_table_6',
    'mts_table_6a',
    'mts_table_6b',
    'mts_table_6c',
    'mts_table_6d',
    'mts_table_6e',
    'mts_table_7',
    'mts_table_8',
    'mts_table_9',
    'net_position',
    'nuclear_waste_fund_results',
    'ofs1_distribution_federal_securities_class_investors_type_issues',
    'ofs2_estimated_ownership_treasury_securities',
    'oil_spill_liability_trust_fund_expected',
    'oil_spill_liability_trust_fund_results',
    'operating_cash_balance',
    'patient_centered_outcomes_research_trust_fund_expected',
    'patient_centered_outcomes_research_trust_fund_results',
    'pdo1_offerings_regular_weekly_treasury_bills',
    'pdo2_offerings_marketable_securities_other_regular_weekly_treasury_bills',
    'public_debt_transactions',
    'qualified_tax',
    'receipts_by_department',
    'reconciliations',
    'record_setting_auction',
    'redemption_tables',
    'reforestation_trust_fund_expected',
    'reforestation_trust_fund_results',
    'savings_bonds_pcs',
    'sb_value',
    'schedules_fed_debt',
    'schedules_fed_debt_daily_activity',
    'schedules_fed_debt_daily_summary',
    'schedules_fed_debt_fytd',
    'securities_accounts',
    'securities_conversions',
    'securities_c_of_i',
    'securities_outstanding',
    'securities_redemptions',
    'securities_sales',
    'securities_sales_term',
    'securities_transfers',
    'short_term_cash_investments',
    'slgs_demand_deposit_rates',
    'slgs_savings_bonds',
    'slgs_securities',
    'slgs_statistics',
    'slgs_time_deposit_rates',
    'social_insurance',
    'sport_fish_restoration_boating_trust_fund_expected',
    'sport_fish_restoration_boating_trust_fund_results',
    'statement_net_cost',
    'tcir_annual_table_1',
    'tcir_annual_table_2',
    'tcir_annual_table_3',
    'tcir_annual_table_4',
    'tcir_annual_table_5',
    'tcir_annual_table_6',
    'tcir_annual_table_7',
    'tcir_annual_table_8',
    'tcir_annual_table_9',
    'tcir_monthly_table_1',
    'tcir_monthly_table_2',
    'tcir_monthly_table_3',
    'tcir_monthly_table_4',
    'tcir_monthly_table_5',
    'tcir_monthly_table_6',
    'tcir_quarterly_table_1',
    'tcir_quarterly_table_2a',
    'tcir_quarterly_table_2b',
    'tcir_quarterly_table_3',
    'tcir_semi_annual',
    'tips_cpi_data_detail',
    'tips_cpi_data_summary',
    'title_xii',
    'tma_contract_disputes',
    'tma_no_fear',
    'tma_unclaimed_money',
    'top_federal',
    'top_state',
    'tror',
    'uranium_enrichment_decontamination_decommissioning_fund_expected',
    'uranium_enrichment_decontamination_decommissioning_fund_results',
    'uscc1_amounts_outstanding_circulation',
    'uscc2_amounts_outstanding_circulation',
    'us_victims_state_sponsored_terrorism_fund_expected',
    'us_victims_state_sponsored_terrorism_fund_results',
    'utf_qtr_yields',
    'vaccine_injury_compensation_trust_fund_expected',
    'vaccine_injury_compensation_trust_fund_results',
    'wool_research_development_promotion_trust_fund_expected',
    'wool_research_development_promotion_trust_fund_results',
]

def main():
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    db = client['treasury_Data']

    for endpoint_file in endpoints:
        try:
            module = importlib.import_module(f'endpoints.{endpoint_file}')
            endpoint_details = module.endpoint_details

            print(f"Fetching data from {endpoint_file} endpoint...")

            collection = db[endpoint_file]

             # Get the most recent record date from the database
            most_recent_date = get_most_recent_record_date(collection)
            if most_recent_date:
                start_date = (most_recent_date + timedelta(days=1)).strftime('%Y-%m-%d')
            else:
                start_date = None

            initial_data, initial_meta = fetch_initial_data(endpoint_details, start_date)
            total_count = initial_meta['total-count']

            # Check if data is already up-to-date
            if collection.count_documents({}) >= total_count and not start_date:
                print(f"Data from {endpoint_file} endpoint is already up to date.")
                continue

            # Fetch remaining data if not up-to-date
            all_data = fetch_data_with_pagination(endpoint_details, start_date)
            formatted_data = endpoint_details['formatter'](all_data)

            print(f"Storing data from {endpoint_file} endpoint to MongoDB...")
            store_data_in_mongodb(formatted_data, 'treasury_Data', endpoint_file)

            # Print the dates of the new records added
            new_record_dates = sorted(set(record['record_date'] for record in all_data))
            for date in new_record_dates:
                print(f"New record date: {date}")

        except KeyError as e:
            print(f"KeyError processing endpoint {endpoint_file}: {e}")

        except Exception as e:
            print(f"Error processing endpoint {endpoint_file}: {e}")

if __name__ == "__main__":
    main()
