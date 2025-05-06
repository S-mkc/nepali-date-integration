# utils.py

from nepali.date_converter import converter

def convert_ad_to_bs(ad_date):
    """
    Convert a given AD date to Nepali (BS) date.
    
    :param ad_date: The AD date as a string (e.g., '2023-04-23' or '23-04-2025')
    :return: The converted BS date as a string (e.g., '2080-01-10')
    """
    try:
        # Try to parse the date in different formats (DD-MM-YYYY or YYYY-MM-DD)
        # Normalize the format to 'YYYY-MM-DD'
        if len(ad_date.split('-')) == 3:
            if len(ad_date.split('-')[0]) == 4:
                # It's already in 'YYYY-MM-DD'
                ad_year, ad_month, ad_day = map(int, ad_date.split('-'))
            else:
                # Convert from 'DD-MM-YYYY' to 'YYYY-MM-DD'
                ad_day, ad_month, ad_year = map(int, ad_date.split('-'))
        else:
            raise ValueError("Invalid date format")

        # Convert AD date to Nepali Date (BS)
        np_year, np_month, np_date = converter.english_to_nepali(ad_year, ad_month, ad_day)

        # Return BS date in 'YYYY-MM-DD' format
        return f"{np_year}-{str(np_month).zfill(2)}-{str(np_date).zfill(2)}"
    
    except Exception as e:
        print(f"Error: {e}")
        return ad_date  # In case of error, return the original AD date
