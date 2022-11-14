from apscheduler.schedulers.asyncio import AsyncIOScheduler

scheduler = AsyncIOScheduler(timezone='Asia/Seoul')


@scheduler.scheduled_job('cron', second='10', id='cron_test_01')
async def cron_test_01():
    print(1)
