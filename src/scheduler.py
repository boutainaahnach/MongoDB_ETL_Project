import schedule
import time

from pipeline import run_pipeline

schedule.every(1).minutes.do(run_pipeline)

print("Scheduler démarré...")

while True:
    schedule.run_pending()
    time.sleep(1)