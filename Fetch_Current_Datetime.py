from datetime import datetime
import pytz
def application_datetime():
    now = datetime.now()
    # assuming now contains a timezone aware datetime
    tz = pytz.timezone('Asia/Kolkata')
    yourdatetime_now = now.astimezone(tz)
    return(yourdatetime_now)

