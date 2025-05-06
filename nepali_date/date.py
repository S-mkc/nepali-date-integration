import datetime
from nepali_datetime import date as nepali_date

def format_value(value, df=None):
    """
    Custom format_value exposed to Jinja — converts AD to BS.
    Only for fieldtype: Date
    """
    if not value:
        return ""

    try:
        if df and df.get("fieldtype") == "Date":
            ad_date = datetime.datetime.strptime(str(value), "%Y-%m-%d").date()
            bs_date = nepali_date.from_datetime_date(ad_date)
            return bs_date.strftime('%K-%n-%D (%k %N %G)')
    except Exception:
        pass

    return value  # fallback to original value

def custom_format_value(value, options=None):
    """
    Custom function to format the value based on specific logic.
    This can handle Nepali date formatting or other custom formatting.
    """
    # Example: Custom logic to format Nepali Date
    if isinstance(value, str) and len(value) == 10:  # Assuming the format is like 'YYYY-MM-DD'
        # Custom logic to convert or format the date
        # Replace this with actual formatting logic if needed
        return "Custom formatted date"  # Example return
    
    # Default formatting logic if no specific handling is needed
    return original_format_value(value, options)


# <P>Posting Date: {{ format_value(doc.posting_date, {"fieldtype": "Date"}) }}</p>    need to use on print format
