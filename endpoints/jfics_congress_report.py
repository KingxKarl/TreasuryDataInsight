import pandas as pd

def format_data(data):
    df = pd.DataFrame(data)

    df['record_date'] = pd.to_datetime(df['record_date'])
    df['payment_sent_dt'] = pd.to_datetime(df['payment_sent_dt'])

    numeric_cols = [
        'confirmed_payment_amt', 'principal_amt', 'attorneys_fee_amt', 'cost_amt', 'interest_amt'
    ]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col].str.replace(',', '').str.replace('$', ''), errors='coerce')

    df['src_line_nbr'] = pd.to_numeric(df['src_line_nbr'], errors='coerce')

    return df.to_dict('records')

endpoint_details = {
    'endpoint': '/v2/payments/jfics/jfics_congress_report',
    'params': {
        'fields': ','.join([
            'record_date', 'judgment_type_cd', 'defendant_agency_nm', 'submitting_agency_nm', 
            'control_nbr', 'plaintiffs_counsel_nm', 'payment_id', 'payment_sent_dt', 
            'confirmed_payment_amt', 'principal_amt', 'principal_citation_cd', 
            'principal_citation_desc', 'attorneys_fee_amt', 'attorneys_fee_citation_cd', 
            'attorneys_fee_citation_desc', 'cost_amt', 'cost_citation_cd', 'cost_citation_desc',
            'interest_amt', 'interest_citation_cd', 'interest_citation_desc', 'src_line_nbr'
        ]),
        'page[size]': 100
    },
    'formatter': format_data
}
