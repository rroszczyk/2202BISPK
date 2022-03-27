from datetime import datetime

def isWeekday():
    today = datetime.today()
    return (0 <= today.weekday() < 5)