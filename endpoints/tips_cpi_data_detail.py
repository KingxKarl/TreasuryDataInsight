import pandas as pd

def format_data(data):
    df = pd.DataFrame(data)

    df['original_issue_date'] = pd.to_datetime(df['original_issue_date'])
    df['index_date'] = pd.to_datetime(df['index_date'])

    numeric_cols = ['ref_cpi', 'index_ratio', 'src_line_nbr']
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col].str.replace(',', '').str.replace('$', ''), errors='coerce')

    return df.to_dict('records')

endpoint_details = {
    'endpoint': '/v1/accounting/od/tips_cpi_data_detail',
    'params': {
        'fields': ','.join([
            'cusip', 'original_issue_date', 'index_date', 'ref_cpi', 'index_ratio',
            'pdf_link', 'xml_link'
        ]),
        'page[size]': 100
    },
    'formatter': format_data
}
