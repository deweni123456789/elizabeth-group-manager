from apscheduler.schedulers.asyncio import AsyncIOScheduler

scheduler = AsyncIOScheduler()

def register(app):
    scheduler.start()
    # Example: schedule a message
    # scheduler.add_job(lambda: print("Scheduled task"), 'interval', minutes=5)
