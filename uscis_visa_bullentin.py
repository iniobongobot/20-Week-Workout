import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta


current_month = datetime.now().strftime("%B")  # Full month name (e.g., "March")
current_year = datetime.now().strftime("%Y")
next_month = (datetime.now() + relativedelta(months=1)).strftime("%B")


def get_visa_date(month):
    df = pd.read_html(f"https://travel.state.gov/content/travel/en/legal/visa-law0/visa-bulletin/{current_year}/visa-bulletin-for-{month}-{current_year}.html")
    visa_dates = []
    for table in df:
        if 5 in table.columns:
            if "Employment" in table[0][0]:
                x = table.drop(columns=[2,3,4,5])
                visa_dates.append(x.iloc[2][1])
    return f"Hey Ini,\n\nThe FINAL ACTION DATES FOR EB2 is {visa_dates[0]}.\n\nDATES FOR FILING OF EB2 APPLICATIONS is {visa_dates[1]} for {month} {current_year}".title()


def final_output():
    try:
        output = get_visa_date(next_month.lower())
    except:
        output = get_visa_date(current_month.lower())

    return output