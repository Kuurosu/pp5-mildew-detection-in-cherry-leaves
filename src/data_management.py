import base64
from datetime import datetime


def download_dataframe_as_csv(df):
    """
    Generate a download link for a DataFrame as a CSV file.

    Args:
        df (pandas.DataFrame): The DataFrame to be downloaded.

    Returns:
        str: HTML code for a download link.

    """
    # Get the current datetime
    datetime_now = datetime.now().strftime("%d%b%Y_%Hh%Mmin%Ss")
    
    # Convert DataFrame to CSV bytes and encode as base64
    csv = df.to_csv().encode()
    b64 = base64.b64encode(csv).decode()
    
    # Generate HTML code for download link with timestamped filename
    href = (
        f'<a href="data:file/csv;base64,{b64}" download="Report {datetime_now}.csv" '
        f'target="_blank">Download Report</a>'
    )
    return href