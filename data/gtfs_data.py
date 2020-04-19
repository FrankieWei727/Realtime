from os import path
import os
import logging.config
from data.database import tables
from sqlalchemy import create_engine
from data.dataProcess import trip_update, static_timetable, alert, vehicle_position
from sqlalchemy.orm import sessionmaker
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR


def create_log():
    # create logger
    log_path = "log/logging.conf"
    log_file_path = path.join(path.dirname(path.abspath(__file__)), log_path)
    logging.config.fileConfig(log_file_path)
    logs = logging.getLogger('gtfs_events')
    return logs


def connect_database():
    # Database config
    database_type = "postgresql"
    user = "frankie"
    password = "0203"
    hostname = "localhost:5432"
    database_name = "trains"

    eng = create_engine(f'{database_type}://{user}:{password}@{hostname}/{database_name}',
                        echo=True)
    return eng


if __name__ == '__main__':

    os.chdir(os.path.dirname(__file__))
    api_key = open("apikey.txt", "r").read().split('.')[0]

    model = 'sydneytrains'
    logger = create_log()

    engine = connect_database()
    Session = sessionmaker(bind=engine)
    session = Session()

    executors = {
        'default': ThreadPoolExecutor(20),
        'processpool': ProcessPoolExecutor(max_workers=5)
    }

    job_defaults = {
        'coalesce': True,
        'max_instances': 5,
        'misfire_grace_time': 30
    }
    scheduler = BackgroundScheduler(executors=executors, job_defaults=job_defaults)

    if api_key is None:
        logger.warning('API key is require.')
        exit(1)

    # Check if it has the tables before start the project
    for table in tables.Base.metadata.tables.keys():
        try:
            if not engine.has_table(table):
                logger.info('Creating table %s', table)
                tables.Base.metadata.tables[table].create(engine)
            else:
                logger.info('%s - The tables has been created --- %s', model, table)
        except Exception as err:
            logger.error('Database Error: %s', str(err))
            exit(1)

    logger.info("Start running project ---- model %s", model)


    def job_timetable():
        static_timetable.timetable(api_key, model, session, logger)


    def job_update_info():
        trip_update.trip_update(api_key, model, session, logger)
        vehicle_position.vehicle_position(api_key, model, session, logger)
        alert.alert(api_key, model, session, logger)


    def jod_delete_older_record():
        # Delete the data of 3 days age
        logger.info("%s - Delete the old data of 3 days ago", model)
        session.execute("""
            DELETE FROM public.trip_alert
                  WHERE datetime < CURRENT_TIMESTAMP(2) - interval '3 day'
        """)
        session.execute("""
            DELETE FROM public.line_alert
                  WHERE datetime < CURRENT_TIMESTAMP(2) - interval '3 day'
        """)
        session.execute("""
            DELETE FROM public.station_alert
                  WHERE datetime < CURRENT_TIMESTAMP(2) - interval '3 day'
        """)
        session.execute("""
            DELETE FROM public.trip_update
                  WHERE datetime < CURRENT_TIMESTAMP(2) - interval '3 day'
        """)
        session.execute("""
            DELETE FROM public.vehicle_position
                  WHERE datetime < CURRENT_TIMESTAMP(2) - interval '3 day'
        """)
        session.execute("""
            DELETE FROM public.timetable
                  WHERE start_date < CURRENT_TIMESTAMP(2) - interval '3 day'
        """)

        session.commit()


    def my_listener(event):
        if event.exception:
            scheduler.shutdown()
            session.close_all()
            print('The job crashed :(')
            logger.warning("%s - %s", model, event.exception)
            exit(1)
        else:
            print('The job worked :)')


    scheduler.add_job(job_timetable, 'cron', hour=5, jitter=120, id="job_timetable")
    scheduler.add_job(jod_delete_older_record, 'cron', hour=1, jitter=120, id="jod_delete_older_record")
    scheduler.add_job(job_update_info, 'cron', hour='6-23', minute="*", id="job_update_info")
    scheduler.add_listener(my_listener, EVENT_JOB_ERROR | EVENT_JOB_EXECUTED)

    keep_running = True
    while keep_running:
        option = input("Please select: 1.get data 2.delete tables 3.pause project 4.exit :")
        if option == "1":
            scheduler.start()

        if option == "2":
            for theClass in tables.AllClasses:
                theClass.__table__.drop(engine)
            logger.info("%s - Delete all the tables --- %s", model, tables.Base.metadata.tables.keys())

        if option == "3":
            logger.info("%s - Pause the project.", model)
            scheduler.pause_job('job_timetable')
            scheduler.pause_job('job_trip_update')
            scheduler.pause_job('job_vehicle_position')
            scheduler.pause_job('job_alert')

        if option == "4":
            scheduler.remove_all_jobs()
            if scheduler.state is not 0:
                scheduler.shutdown()
            session.close_all()
            logger.info("Stop running project ---- model %s", model)
            keep_running = False
    exit(0)
