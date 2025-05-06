from datetime import datetime
from nepali_datetime import date as nepali_date

def ad_to_bs_string(ad_date):
    """
    Converts AD date (datetime/date/str) to a formatted BS string.
    """
    if isinstance(ad_date, str):
        ad_date = datetime.strptime(ad_date, "%Y-%m-%d").date()
    elif isinstance(ad_date, datetime):
        ad_date = ad_date.date()

    try:
        bs_date = nepali_date.from_datetime_date(ad_date)
        return bs_date.strftime("%Y-%m-%d")  # You can use any format here
    except Exception as e:
        return ad_date.strftime("%Y-%m-%d")  # fallback to AD
