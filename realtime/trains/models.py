# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class LineAlert(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    agency_id = models.CharField(max_length=32, blank=True, null=True)
    route_id = models.CharField(max_length=32, blank=True, null=True)
    header_text = models.TextField(blank=True, null=True)
    description_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'line_alert'


class StationAlert(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    agency_id = models.CharField(max_length=32, blank=True, null=True)
    stop_id = models.CharField(max_length=50, blank=True, null=True)
    cause = models.CharField(max_length=50, blank=True, null=True)
    effect = models.CharField(max_length=50, blank=True, null=True)
    header_text = models.TextField(blank=True, null=True)
    description_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'station_alert'


class Timetable(models.Model):
    id = models.BigAutoField(primary_key=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    arrival_time = models.TimeField(blank=True, null=True)
    departure_time = models.TimeField(blank=True, null=True)
    route_id = models.CharField(max_length=30, blank=True, null=True)
    route_short_name = models.CharField(max_length=30, blank=True, null=True)
    route_long_name = models.CharField(max_length=50, blank=True, null=True)
    route_type = models.IntegerField(blank=True, null=True)
    route_color = models.CharField(max_length=30, blank=True, null=True)
    route_text_color = models.CharField(max_length=30, blank=True, null=True)
    service_id = models.CharField(max_length=32, blank=True, null=True)
    trip_id = models.CharField(max_length=50, blank=True, null=True)
    trip_headsign = models.TextField(blank=True, null=True)
    direction_id = models.IntegerField(blank=True, null=True)
    stop_id = models.CharField(max_length=30, blank=True, null=True)
    stop_name = models.CharField(max_length=60, blank=True, null=True)
    stop_sequence = models.IntegerField(blank=True, null=True)
    pickup_type = models.IntegerField(blank=True, null=True)
    drop_off_type = models.IntegerField(blank=True, null=True)
    block_id = models.CharField(max_length=32, blank=True, null=True)
    shape_id = models.CharField(max_length=32, blank=True, null=True)
    stop_lat = models.FloatField(blank=True, null=True)
    stop_lon = models.FloatField(blank=True, null=True)
    location_type = models.IntegerField(blank=True, null=True)
    parent_station = models.CharField(max_length=32, blank=True, null=True)
    wheelchair_accessible = models.IntegerField(blank=True, null=True)
    monday = models.IntegerField(blank=True, null=True)
    tuesday = models.IntegerField(blank=True, null=True)
    wednesday = models.IntegerField(blank=True, null=True)
    thursday = models.IntegerField(blank=True, null=True)
    friday = models.IntegerField(blank=True, null=True)
    saturday = models.IntegerField(blank=True, null=True)
    sunday = models.IntegerField(blank=True, null=True)
    agency_name = models.CharField(max_length=32, blank=True, null=True)
    agency_timezone = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'timetable'


class TripAlert(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    agency_id = models.CharField(max_length=32, blank=True, null=True)
    trip_id = models.CharField(max_length=50, blank=True, null=True)
    header_text = models.TextField(blank=True, null=True)
    description_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trip_alert'


class TripUpdate(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    trip_id = models.CharField(max_length=50, blank=True, null=True)
    route_id = models.CharField(max_length=30, blank=True, null=True)
    schedule_relationship = models.CharField(max_length=30, blank=True, null=True)
    stop_id = models.CharField(max_length=30, blank=True, null=True)
    arrival_time = models.DateTimeField(blank=True, null=True)
    arrival_delay = models.IntegerField(blank=True, null=True)
    departure_time = models.DateTimeField(blank=True, null=True)
    departure_delay = models.IntegerField(blank=True, null=True)
    update_schedulerelationship = models.CharField(db_column='update_scheduleRelationship', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'trip_update'


class VehiclePosition(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    vehicle = models.CharField(max_length=100, blank=True, null=True)
    trip_id = models.CharField(max_length=50, blank=True, null=True)
    stop_id = models.CharField(max_length=50, blank=True, null=True)
    schedule_relationship = models.CharField(max_length=50, blank=True, null=True)
    route_id = models.CharField(max_length=50, blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)
    congestion_level = models.CharField(max_length=40, blank=True, null=True)
    label = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vehicle_position'
