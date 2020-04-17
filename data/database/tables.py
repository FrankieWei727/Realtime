from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, \
    Float, BigInteger, Date, Time, Text, DateTime

Base = declarative_base()


class Timetable(Base):
    __tablename__ = 'timetable'
    id = Column(BigInteger, primary_key=True)

    start_date = Column(Date)
    end_date = Column(Date)

    arrival_time = Column(Time)
    departure_time = Column(Time)

    route_id = Column(String(30))
    route_short_name = Column(String(30))
    route_long_name = Column(String(50))
    route_type = Column(Integer)
    route_color = Column(String(30))
    route_text_color = Column(String(30))
    service_id = Column(String(32))

    trip_id = Column(String(50))
    trip_headsign = Column(Text)

    direction_id = Column(Integer)
    stop_id = Column(String(30))
    stop_name = Column(String(60))
    stop_sequence = Column(Integer)
    pickup_type = Column(Integer)
    drop_off_type = Column(Integer)
    block_id = Column(String(32))
    shape_id = Column(String(32))
    stop_lat = Column(Float)
    stop_lon = Column(Float)
    location_type = Column(Integer)
    parent_station = Column(String(32))
    wheelchair_accessible = Column(Integer)
    monday = Column(Integer)
    tuesday = Column(Integer)
    wednesday = Column(Integer)
    thursday = Column(Integer)
    friday = Column(Integer)
    saturday = Column(Integer)
    sunday = Column(Integer)
    agency_name = Column(String(32))
    agency_timezone = Column(String(32))


class TripUpdate(Base):
    __tablename__ = 'trip_update'
    id = Column(BigInteger, primary_key=True)

    datetime = Column(DateTime(timezone=True))
    trip_id = Column(String(50))
    route_id = Column(String(30))

    schedule_relationship = Column(String(30))
    stop_id = Column(String(30))

    arrival_time = Column(DateTime(timezone=True))
    arrival_delay = Column(Integer)
    departure_time = Column(DateTime(timezone=True))
    departure_delay = Column(Integer)
    update_schedule_relationship = Column(String(30))


class VehiclePosition(Base):
    __tablename__ = 'vehicle_position'
    id = Column(BigInteger, primary_key=True)

    datetime = Column(DateTime(timezone=True))
    vehicle = Column(String(100))
    trip_id = Column(String(50))
    stop_id = Column(String(50))
    schedule_relationship = Column(String(50))
    route_id = Column(String(50))
    lat = Column(Float)
    lon = Column(Float)
    congestion_level = Column(String(40))
    label = Column(Text)


class LineAlert(Base):
    __tablename__ = 'line_alert'
    id = Column(BigInteger, primary_key=True)

    datetime = Column(DateTime(timezone=True))
    agency_id = Column(String(32))
    route_id = Column(String(32))
    header_text = Column(Text)
    description_text = Column(Text)


class StationAlert(Base):
    __tablename__ = 'station_alert'
    id = Column(BigInteger, primary_key=True)

    datetime = Column(DateTime(timezone=True))
    agency_id = Column(String(32))
    stop_id = Column(String(50))
    cause = Column(String(50))
    effect = Column(String(50))
    header_text = Column(Text)
    description_text = Column(Text)


class TripAlert(Base):
    __tablename__ = 'trip_alert'
    id = Column(BigInteger, primary_key=True)

    datetime = Column(DateTime(timezone=True))
    agency_id = Column(String(32))
    trip_id = Column(String(50))
    header_text = Column(Text)
    description_text = Column(Text)


AllClasses = (Timetable, TripUpdate, VehiclePosition, TripAlert, LineAlert, StationAlert)
