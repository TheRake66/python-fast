from datetime import datetime

now = datetime.now()

variables: dict[str, str] = {
  "datetime_full": now.strftime("%Y-%m-%d %H:%M:%S"),
  "datetime_date": now.strftime("%Y-%m-%d"),
  "datetime_time": now.strftime("%H:%M:%S")
}