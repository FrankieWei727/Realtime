from os import path
import os
import logging.config
from data.database import tables
from sqlalchemy import create_engine
from data.dataProcess import trip_update, static_timetable, alert, vehicle_position
from sqlalchemy.orm import sessionmaker
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from apscheduler.schedulers.background import BackgroundScheduler, BlockingScheduler
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
    session = sessionmaker(bind=engine)
    s = session()

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
        exit(0)

    # Check if it has the tables
    for table in tables.Base.metadata.tables.keys():
        try:
            if not engine.has_table(table):
                logger.info('Creating table %s', table)
                tables.Base.metadata.tables[table].create(engine)
            else:
                logger.info('The tables has been created --- %s', table)
        except Exception as err:
            logger.error('Database Error: %s', str(err))
            exit(1)

    logger.info("Start running project ---- model %s", model)


    def job_timetable():
        static_timetable.timetable(api_key, model, s, logger)


    def job_update_info():
        trip_update.trip_update(api_key, model, s, logger)
        vehicle_position.vehicle_position(api_key, model, s, logger)
        alert.alert(api_key, model, s, logger)


    def my_listener(event):
        if event.exception:
            scheduler.shutdown()
            session.close_all()
            print('The job crashed :(')
            exit(0)
        else:
            print('The job worked :)')


    scheduler.add_job(job_timetable, 'interval', hours=1, jitter=120, id="job_timetable")
    scheduler.add_job(job_update_info, 'interval', minutes=1, id="job_update_info")
    scheduler.add_listener(my_listener, EVENT_JOB_ERROR | EVENT_JOB_EXECUTED)

    keep_running = True
    while keep_running:
        option = input("Please select: 1.get data 2.delete tables 3.pause project 4.exit :")
        if option == "1":
            scheduler.start()

        if option == "2":
            for theClass in tables.AllClasses:
                theClass.__table__.drop(engine)
            logger.info("Delete all the tables --- %s", tables.Base.metadata.tables.keys())

        if option == "3":
            logger.info("Pause the project.")
            scheduler.pause_job('job_timetable')
            scheduler.pause_job('job_trip_update')
            scheduler.pause_job('job_vehicle_position')
            scheduler.pause_job('job_alert')

        if option == "4":
            logger.info("Stop running project.")
            scheduler.remove_all_jobs()
            scheduler.shutdown()
            session.close_all()
            keep_running = False
            exit(0)
