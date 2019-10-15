

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()



DESCRIPTOR = _descriptor.FileDescriptor(
  name='tfnsw-gtfs-realtime.proto',
  package='transit_realtime',
  syntax='proto2',
  serialized_pb=_b('\n\x19tfnsw-gtfs-realtime.proto\x12\x10transit_realtime\"q\n\x0b\x46\x65\x65\x64Message\x12,\n\x06header\x18\x01 \x02(\x0b\x32\x1c.transit_realtime.FeedHeader\x12,\n\x06\x65ntity\x18\x02 \x03(\x0b\x32\x1c.transit_realtime.FeedEntity*\x06\x08\xe8\x07\x10\xd0\x0f\"\xcf\x01\n\nFeedHeader\x12\x1d\n\x15gtfs_realtime_version\x18\x01 \x02(\t\x12Q\n\x0eincrementality\x18\x02 \x01(\x0e\x32+.transit_realtime.FeedHeader.Incrementality:\x0c\x46ULL_DATASET\x12\x11\n\ttimestamp\x18\x03 \x01(\x04\"4\n\x0eIncrementality\x12\x10\n\x0c\x46ULL_DATASET\x10\x00\x12\x10\n\x0c\x44IFFERENTIAL\x10\x01*\x06\x08\xe8\x07\x10\xd0\x0f\"\xca\x01\n\nFeedEntity\x12\n\n\x02id\x18\x01 \x02(\t\x12\x19\n\nis_deleted\x18\x02 \x01(\x08:\x05\x66\x61lse\x12\x31\n\x0btrip_update\x18\x03 \x01(\x0b\x32\x1c.transit_realtime.TripUpdate\x12\x32\n\x07vehicle\x18\x04 \x01(\x0b\x32!.transit_realtime.VehiclePosition\x12&\n\x05\x61lert\x18\x05 \x01(\x0b\x32\x17.transit_realtime.Alert*\x06\x08\xe8\x07\x10\xd0\x0f\"\x9a\x05\n\nTripUpdate\x12.\n\x04trip\x18\x01 \x02(\x0b\x32 .transit_realtime.TripDescriptor\x12\x34\n\x07vehicle\x18\x03 \x01(\x0b\x32#.transit_realtime.VehicleDescriptor\x12\x45\n\x10stop_time_update\x18\x02 \x03(\x0b\x32+.transit_realtime.TripUpdate.StopTimeUpdate\x12\x11\n\ttimestamp\x18\x04 \x01(\x04\x12\r\n\x05\x64\x65lay\x18\x05 \x01(\x05\x1aI\n\rStopTimeEvent\x12\r\n\x05\x64\x65lay\x18\x01 \x01(\x05\x12\x0c\n\x04time\x18\x02 \x01(\x03\x12\x13\n\x0buncertainty\x18\x03 \x01(\x05*\x06\x08\xe8\x07\x10\xd0\x0f\x1a\xe9\x02\n\x0eStopTimeUpdate\x12\x15\n\rstop_sequence\x18\x01 \x01(\r\x12\x0f\n\x07stop_id\x18\x04 \x01(\t\x12;\n\x07\x61rrival\x18\x02 \x01(\x0b\x32*.transit_realtime.TripUpdate.StopTimeEvent\x12=\n\tdeparture\x18\x03 \x01(\x0b\x32*.transit_realtime.TripUpdate.StopTimeEvent\x12j\n\x15schedule_relationship\x18\x05 \x01(\x0e\x32@.transit_realtime.TripUpdate.StopTimeUpdate.ScheduleRelationship:\tSCHEDULED\"?\n\x14ScheduleRelationship\x12\r\n\tSCHEDULED\x10\x00\x12\x0b\n\x07SKIPPED\x10\x01\x12\x0b\n\x07NO_DATA\x10\x02*\x06\x08\xe8\x07\x10\xd0\x0f*\x06\x08\xe8\x07\x10\xd0\x0f\"\xe0\x06\n\x0fVehiclePosition\x12.\n\x04trip\x18\x01 \x01(\x0b\x32 .transit_realtime.TripDescriptor\x12\x34\n\x07vehicle\x18\x08 \x01(\x0b\x32#.transit_realtime.VehicleDescriptor\x12,\n\x08position\x18\x02 \x01(\x0b\x32\x1a.transit_realtime.Position\x12\x1d\n\x15\x63urrent_stop_sequence\x18\x03 \x01(\r\x12\x0f\n\x07stop_id\x18\x07 \x01(\t\x12Z\n\x0e\x63urrent_status\x18\x04 \x01(\x0e\x32\x33.transit_realtime.VehiclePosition.VehicleStopStatus:\rIN_TRANSIT_TO\x12\x11\n\ttimestamp\x18\x05 \x01(\x04\x12K\n\x10\x63ongestion_level\x18\x06 \x01(\x0e\x32\x31.transit_realtime.VehiclePosition.CongestionLevel\x12K\n\x10occupancy_status\x18\t \x01(\x0e\x32\x31.transit_realtime.VehiclePosition.OccupancyStatus\"G\n\x11VehicleStopStatus\x12\x0f\n\x0bINCOMING_AT\x10\x00\x12\x0e\n\nSTOPPED_AT\x10\x01\x12\x11\n\rIN_TRANSIT_TO\x10\x02\"}\n\x0f\x43ongestionLevel\x12\x1c\n\x18UNKNOWN_CONGESTION_LEVEL\x10\x00\x12\x14\n\x10RUNNING_SMOOTHLY\x10\x01\x12\x0f\n\x0bSTOP_AND_GO\x10\x02\x12\x0e\n\nCONGESTION\x10\x03\x12\x15\n\x11SEVERE_CONGESTION\x10\x04\"\xaf\x01\n\x0fOccupancyStatus\x12\t\n\x05\x45MPTY\x10\x00\x12\x18\n\x14MANY_SEATS_AVAILABLE\x10\x01\x12\x17\n\x13\x46\x45W_SEATS_AVAILABLE\x10\x02\x12\x16\n\x12STANDING_ROOM_ONLY\x10\x03\x12\x1e\n\x1a\x43RUSHED_STANDING_ROOM_ONLY\x10\x04\x12\x08\n\x04\x46ULL\x10\x05\x12\x1c\n\x18NOT_ACCEPTING_PASSENGERS\x10\x06*\x06\x08\xe8\x07\x10\xd0\x0f\"\xb6\x06\n\x05\x41lert\x12\x32\n\ractive_period\x18\x01 \x03(\x0b\x32\x1b.transit_realtime.TimeRange\x12\x39\n\x0finformed_entity\x18\x05 \x03(\x0b\x32 .transit_realtime.EntitySelector\x12;\n\x05\x63\x61use\x18\x06 \x01(\x0e\x32\x1d.transit_realtime.Alert.Cause:\rUNKNOWN_CAUSE\x12>\n\x06\x65\x66\x66\x65\x63t\x18\x07 \x01(\x0e\x32\x1e.transit_realtime.Alert.Effect:\x0eUNKNOWN_EFFECT\x12/\n\x03url\x18\x08 \x01(\x0b\x32\".transit_realtime.TranslatedString\x12\x37\n\x0bheader_text\x18\n \x01(\x0b\x32\".transit_realtime.TranslatedString\x12<\n\x10\x64\x65scription_text\x18\x0b \x01(\x0b\x32\".transit_realtime.TranslatedString\"\xd8\x01\n\x05\x43\x61use\x12\x11\n\rUNKNOWN_CAUSE\x10\x01\x12\x0f\n\x0bOTHER_CAUSE\x10\x02\x12\x15\n\x11TECHNICAL_PROBLEM\x10\x03\x12\n\n\x06STRIKE\x10\x04\x12\x11\n\rDEMONSTRATION\x10\x05\x12\x0c\n\x08\x41\x43\x43IDENT\x10\x06\x12\x0b\n\x07HOLIDAY\x10\x07\x12\x0b\n\x07WEATHER\x10\x08\x12\x0f\n\x0bMAINTENANCE\x10\t\x12\x10\n\x0c\x43ONSTRUCTION\x10\n\x12\x13\n\x0fPOLICE_ACTIVITY\x10\x0b\x12\x15\n\x11MEDICAL_EMERGENCY\x10\x0c\"\xb5\x01\n\x06\x45\x66\x66\x65\x63t\x12\x0e\n\nNO_SERVICE\x10\x01\x12\x13\n\x0fREDUCED_SERVICE\x10\x02\x12\x16\n\x12SIGNIFICANT_DELAYS\x10\x03\x12\n\n\x06\x44\x45TOUR\x10\x04\x12\x16\n\x12\x41\x44\x44ITIONAL_SERVICE\x10\x05\x12\x14\n\x10MODIFIED_SERVICE\x10\x06\x12\x10\n\x0cOTHER_EFFECT\x10\x07\x12\x12\n\x0eUNKNOWN_EFFECT\x10\x08\x12\x0e\n\nSTOP_MOVED\x10\t*\x06\x08\xe8\x07\x10\xd0\x0f\"/\n\tTimeRange\x12\r\n\x05start\x18\x01 \x01(\x04\x12\x0b\n\x03\x65nd\x18\x02 \x01(\x04*\x06\x08\xe8\x07\x10\xd0\x0f\"i\n\x08Position\x12\x10\n\x08latitude\x18\x01 \x02(\x02\x12\x11\n\tlongitude\x18\x02 \x02(\x02\x12\x0f\n\x07\x62\x65\x61ring\x18\x03 \x01(\x02\x12\x10\n\x08odometer\x18\x04 \x01(\x01\x12\r\n\x05speed\x18\x05 \x01(\x02*\x06\x08\xe8\x07\x10\xd0\x0f\"\xa0\x02\n\x0eTripDescriptor\x12\x0f\n\x07trip_id\x18\x01 \x01(\t\x12\x10\n\x08route_id\x18\x05 \x01(\t\x12\x14\n\x0c\x64irection_id\x18\x06 \x01(\r\x12\x12\n\nstart_time\x18\x02 \x01(\t\x12\x12\n\nstart_date\x18\x03 \x01(\t\x12T\n\x15schedule_relationship\x18\x04 \x01(\x0e\x32\x35.transit_realtime.TripDescriptor.ScheduleRelationship\"O\n\x14ScheduleRelationship\x12\r\n\tSCHEDULED\x10\x00\x12\t\n\x05\x41\x44\x44\x45\x44\x10\x01\x12\x0f\n\x0bUNSCHEDULED\x10\x02\x12\x0c\n\x08\x43\x41NCELED\x10\x03*\x06\x08\xe8\x07\x10\xd0\x0f\"M\n\x11VehicleDescriptor\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05label\x18\x02 \x01(\t\x12\x15\n\rlicense_plate\x18\x03 \x01(\t*\x06\x08\xe8\x07\x10\xd0\x0f\"\x92\x01\n\x0e\x45ntitySelector\x12\x11\n\tagency_id\x18\x01 \x01(\t\x12\x10\n\x08route_id\x18\x02 \x01(\t\x12\x12\n\nroute_type\x18\x03 \x01(\x05\x12.\n\x04trip\x18\x04 \x01(\x0b\x32 .transit_realtime.TripDescriptor\x12\x0f\n\x07stop_id\x18\x05 \x01(\t*\x06\x08\xe8\x07\x10\xd0\x0f\"\x96\x01\n\x10TranslatedString\x12\x43\n\x0btranslation\x18\x01 \x03(\x0b\x32..transit_realtime.TranslatedString.Translation\x1a\x35\n\x0bTranslation\x12\x0c\n\x04text\x18\x01 \x02(\t\x12\x10\n\x08language\x18\x02 \x01(\t*\x06\x08\xe8\x07\x10\xd0\x0f*\x06\x08\xe8\x07\x10\xd0\x0f\"\xbe\x01\n\x16TfnswVehicleDescriptor\x12\x1e\n\x0f\x61ir_conditioned\x18\x01 \x01(\x08:\x05\x66\x61lse\x12 \n\x15wheelchair_accessible\x18\x02 \x01(\x05:\x01\x30\x12\x15\n\rvehicle_model\x18\x03 \x01(\t\x12$\n\x15performing_prior_trip\x18\x04 \x01(\x08:\x05\x66\x61lse\x12%\n\x1aspecial_vehicle_attributes\x18\x05 \x01(\x05:\x01\x30:p\n\x18tfnsw_vehicle_descriptor\x12#.transit_realtime.VehicleDescriptor\x18\xcf\x0f \x01(\x0b\x32(.transit_realtime.TfnswVehicleDescriptorB\x1d\n\x1b\x63om.google.transit.realtime')
)


TFNSW_VEHICLE_DESCRIPTOR_FIELD_NUMBER = 1999
tfnsw_vehicle_descriptor = _descriptor.FieldDescriptor(
  name='tfnsw_vehicle_descriptor', full_name='transit_realtime.tfnsw_vehicle_descriptor', index=0,
  number=1999, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)

_FEEDHEADER_INCREMENTALITY = _descriptor.EnumDescriptor(
  name='Incrementality',
  full_name='transit_realtime.FeedHeader.Incrementality',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FULL_DATASET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DIFFERENTIAL', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=310,
  serialized_end=362,
)
_sym_db.RegisterEnumDescriptor(_FEEDHEADER_INCREMENTALITY)

_TRIPUPDATE_STOPTIMEUPDATE_SCHEDULERELATIONSHIP = _descriptor.EnumDescriptor(
  name='ScheduleRelationship',
  full_name='transit_realtime.TripUpdate.StopTimeUpdate.ScheduleRelationship',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SCHEDULED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SKIPPED', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NO_DATA', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1165,
  serialized_end=1228,
)
_sym_db.RegisterEnumDescriptor(_TRIPUPDATE_STOPTIMEUPDATE_SCHEDULERELATIONSHIP)

_VEHICLEPOSITION_VEHICLESTOPSTATUS = _descriptor.EnumDescriptor(
  name='VehicleStopStatus',
  full_name='transit_realtime.VehiclePosition.VehicleStopStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INCOMING_AT', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STOPPED_AT', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IN_TRANSIT_TO', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1727,
  serialized_end=1798,
)
_sym_db.RegisterEnumDescriptor(_VEHICLEPOSITION_VEHICLESTOPSTATUS)

_VEHICLEPOSITION_CONGESTIONLEVEL = _descriptor.EnumDescriptor(
  name='CongestionLevel',
  full_name='transit_realtime.VehiclePosition.CongestionLevel',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_CONGESTION_LEVEL', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RUNNING_SMOOTHLY', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STOP_AND_GO', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONGESTION', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SEVERE_CONGESTION', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1800,
  serialized_end=1925,
)
_sym_db.RegisterEnumDescriptor(_VEHICLEPOSITION_CONGESTIONLEVEL)

_VEHICLEPOSITION_OCCUPANCYSTATUS = _descriptor.EnumDescriptor(
  name='OccupancyStatus',
  full_name='transit_realtime.VehiclePosition.OccupancyStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='EMPTY', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MANY_SEATS_AVAILABLE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FEW_SEATS_AVAILABLE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STANDING_ROOM_ONLY', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CRUSHED_STANDING_ROOM_ONLY', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FULL', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOT_ACCEPTING_PASSENGERS', index=6, number=6,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1928,
  serialized_end=2103,
)
_sym_db.RegisterEnumDescriptor(_VEHICLEPOSITION_OCCUPANCYSTATUS)

_ALERT_CAUSE = _descriptor.EnumDescriptor(
  name='Cause',
  full_name='transit_realtime.Alert.Cause',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_CAUSE', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OTHER_CAUSE', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TECHNICAL_PROBLEM', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STRIKE', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEMONSTRATION', index=4, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACCIDENT', index=5, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HOLIDAY', index=6, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WEATHER', index=7, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAINTENANCE', index=8, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONSTRUCTION', index=9, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POLICE_ACTIVITY', index=10, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MEDICAL_EMERGENCY', index=11, number=12,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=2528,
  serialized_end=2744,
)
_sym_db.RegisterEnumDescriptor(_ALERT_CAUSE)

_ALERT_EFFECT = _descriptor.EnumDescriptor(
  name='Effect',
  full_name='transit_realtime.Alert.Effect',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NO_SERVICE', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REDUCED_SERVICE', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SIGNIFICANT_DELAYS', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DETOUR', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ADDITIONAL_SERVICE', index=4, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MODIFIED_SERVICE', index=5, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OTHER_EFFECT', index=6, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_EFFECT', index=7, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STOP_MOVED', index=8, number=9,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=2747,
  serialized_end=2928,
)
_sym_db.RegisterEnumDescriptor(_ALERT_EFFECT)

_TRIPDESCRIPTOR_SCHEDULERELATIONSHIP = _descriptor.EnumDescriptor(
  name='ScheduleRelationship',
  full_name='transit_realtime.TripDescriptor.ScheduleRelationship',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SCHEDULED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ADDED', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNSCHEDULED', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANCELED', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=3296,
  serialized_end=3375,
)
_sym_db.RegisterEnumDescriptor(_TRIPDESCRIPTOR_SCHEDULERELATIONSHIP)


_FEEDMESSAGE = _descriptor.Descriptor(
  name='FeedMessage',
  full_name='transit_realtime.FeedMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='transit_realtime.FeedMessage.header', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='entity', full_name='transit_realtime.FeedMessage.entity', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=True,
  syntax='proto2',
  extension_ranges=[(1000, 2000), ],
  oneofs=[
  ],
  serialized_start=47,
  serialized_end=160,
)


_FEEDHEADER = _descriptor.Descriptor(
  name='FeedHeader',
  full_name='transit_realtime.FeedHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gtfs_realtime_version', full_name='transit_realtime.FeedHeader.gtfs_realtime_version', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='incrementality', full_name='transit_realtime.FeedHeader.incrementality', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='transit_realtime.FeedHeader.timestamp', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _FEEDHEADER_INCREMENTALITY,
  ],
  options=None,
  is_extendable=True,
  syntax='proto2',
  extension_ranges=[(1000, 2000), ],
  oneofs=[
  ],
  serialized_start=163,
  serialized_end=370,
)


_FEEDENTITY = _descriptor.Descriptor(
  name='FeedEntity',
  full_name='transit_realtime.FeedEntity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='transit_realtime.FeedEntity.id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_deleted', full_name='transit_realtime.FeedEntity.is_deleted', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='trip_update', full_name='transit_realtime.FeedEntity.trip_update', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vehicle', full_name='transit_realtime.FeedEntity.vehicle', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='alert', full_name='transit_realtime.FeedEntity.alert', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=True,
  syntax='proto2',
  extension_ranges=[(1000, 2000), ],
  oneofs=[
  ],
  serialized_start=373,
  serialized_end=575,
)


_TRIPUPDATE_STOPTIMEEVENT = _descriptor.Descriptor(
  name='StopTimeEvent',
  full_name='transit_realtime.TripUpdate.StopTimeEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='delay', full_name='transit_realtime.TripUpdate.StopTimeEvent.delay', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time', full_name='transit_realtime.TripUpdate.StopTimeEvent.time', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uncertainty', full_name='transit_realtime.TripUpdate.StopTimeEvent.uncertainty', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=True,
  syntax='proto2',
  extension_ranges=[(1000, 2000), ],
  oneofs=[
  ],
  serialized_start=799,
  serialized_end=872,
)

_TRIPUPDATE_STOPTIMEUPDATE = _descriptor.Descriptor(
  name='StopTimeUpdate',
  full_name='transit_realtime.TripUpdate.StopTimeUpdate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stop_sequence', full_name='transit_realtime.TripUpdate.StopTimeUpdate.stop_sequence', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stop_id', full_name='transit_realtime.TripUpdate.StopTimeUpdate.stop_id', index=1,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='arrival', full_name='transit_realtime.TripUpdate.StopTimeUpdate.arrival', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='departure', full_name='transit_realtime.TripUpdate.StopTimeUpdate.departure', index=3,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='schedule_relationship', full_name='transit_realtime.TripUpdate.StopTimeUpdate.schedule_relationship', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TRIPUPDATE_STOPTIMEUPDATE_SCHEDULERELATIONSHIP,
  ],
  options=None,
  is_extendable=True,
  syntax='proto2',
  extension_ranges=[(1000, 2000), ],
  oneofs=[
  ],
  serialized_start=875,
  serialized_end=1236,
)

_TRIPUPDATE = _descriptor.Descriptor(
  name='TripUpdate',
  full_name='transit_realtime.TripUpdate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='trip', full_name='transit_realtime.TripUpdate.trip', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vehicle', full_name='transit_realtime.TripUpdate.vehicle', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stop_time_update', full_name='transit_realtime.TripUpdate.stop_time_update', index=2,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='transit_realtime.TripUpdate.timestamp', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='delay', full_name='transit_realtime.TripUpdate.delay', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_TRIPUPDATE_STOPTIMEEVENT, _TRIPUPDATE_STOPTIMEUPDATE, ],
  enum_types=[
  ],
  options=None,
  is_extendable=True,
  syntax='proto2',
  extension_ranges=[(1000, 2000), ],
  oneofs=[
  ],
  serialized_start=578,
  serialized_end=1244,
)


_VEHICLEPOSITION = _descriptor.Descriptor(
  name='VehiclePosition',
  full_name='transit_realtime.VehiclePosition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='trip', full_name='transit_realtime.VehiclePosition.trip', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vehicle', full_name='transit_realtime.VehiclePosition.vehicle', index=1,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='position', full_name='transit_realtime.VehiclePosition.position', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='current_stop_sequence', full_name='transit_realtime.VehiclePosition.current_stop_sequence', index=3,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stop_id', full_name='transit_realtime.VehiclePosition.stop_id', index=4,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='current_status', full_name='transit_realtime.VehiclePosition.current_status', index=5,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=2,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='transit_realtime.VehiclePosition.timestamp', index=6,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='congestion_level', full_name='transit_realtime.VehiclePosition.congestion_level', index=7,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='occupancy_status', full_name='transit_realtime.VehiclePosition.occupancy_status', index=8,
      number=9, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _VEHICLEPOSITION_VEHICLESTOPSTATUS,
    _VEHICLEPOSITION_CONGESTIONLEVEL,
    _VEHICLEPOSITION_OCCUPANCYSTATUS,
  ],
  options=None,
  is_extendable=True,
  syntax='proto2',
  extension_ranges=[(1000, 2000), ],
  oneofs=[
  ],
  serialized_start=1247,
  serialized_end=2111,
)


_ALERT = _descriptor.Descriptor(
  name='Alert',
  full_name='transit_realtime.Alert',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='active_period', full_name='transit_realtime.Alert.active_period', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='informed_entity', full_name='transit_realtime.Alert.informed_entity', index=1,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cause', full_name='transit_realtime.Alert.cause', index=2,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='effect', full_name='transit_realtime.Alert.effect', index=3,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=8,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='url', full_name='transit_realtime.Alert.url', index=4,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='header_text', full_name='transit_realtime.Alert.header_text', index=5,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description_text', full_name='transit_realtime.Alert.description_text', index=6,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ALERT_CAUSE,
    _ALERT_EFFECT,
  ],
  options=None,
  is_extendable=True,
  syntax='proto2',
  extension_ranges=[(1000, 2000), ],
  oneofs=[
  ],
  serialized_start=2114,
  serialized_end=2936,
)


_TIMERANGE = _descriptor.Descriptor(
  name='TimeRange',
  full_name='transit_realtime.TimeRange',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start', full_name='transit_realtime.TimeRange.start', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end', full_name='transit_realtime.TimeRange.end', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=True,
  syntax='proto2',
  extension_ranges=[(1000, 2000), ],
  oneofs=[
  ],
  serialized_start=2938,
  serialized_end=2985,
)


_POSITION = _descriptor.Descriptor(
  name='Position',
  full_name='transit_realtime.Position',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='latitude', full_name='transit_realtime.Position.latitude', index=0,
      number=1, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='transit_realtime.Position.longitude', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bearing', full_name='transit_realtime.Position.bearing', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='odometer', full_name='transit_realtime.Position.odometer', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='speed', full_name='transit_realtime.Position.speed', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=True,
  syntax='proto2',
  extension_ranges=[(1000, 2000), ],
  oneofs=[
  ],
  serialized_start=2987,
  serialized_end=3092,
)


_TRIPDESCRIPTOR = _descriptor.Descriptor(
  name='TripDescriptor',
  full_name='transit_realtime.TripDescriptor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='trip_id', full_name='transit_realtime.TripDescriptor.trip_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='route_id', full_name='transit_realtime.TripDescriptor.route_id', index=1,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='direction_id', full_name='transit_realtime.TripDescriptor.direction_id', index=2,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start_time', full_name='transit_realtime.TripDescriptor.start_time', index=3,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start_date', full_name='transit_realtime.TripDescriptor.start_date', index=4,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='schedule_relationship', full_name='transit_realtime.TripDescriptor.schedule_relationship', index=5,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TRIPDESCRIPTOR_SCHEDULERELATIONSHIP,
  ],
  options=None,
  is_extendable=True,
  syntax='proto2',
  extension_ranges=[(1000, 2000), ],
  oneofs=[
  ],
  serialized_start=3095,
  serialized_end=3383,
)


_VEHICLEDESCRIPTOR = _descriptor.Descriptor(
  name='VehicleDescriptor',
  full_name='transit_realtime.VehicleDescriptor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='transit_realtime.VehicleDescriptor.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='label', full_name='transit_realtime.VehicleDescriptor.label', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='license_plate', full_name='transit_realtime.VehicleDescriptor.license_plate', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=True,
  syntax='proto2',
  extension_ranges=[(1000, 2000), ],
  oneofs=[
  ],
  serialized_start=3385,
  serialized_end=3462,
)


_ENTITYSELECTOR = _descriptor.Descriptor(
  name='EntitySelector',
  full_name='transit_realtime.EntitySelector',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='agency_id', full_name='transit_realtime.EntitySelector.agency_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='route_id', full_name='transit_realtime.EntitySelector.route_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='route_type', full_name='transit_realtime.EntitySelector.route_type', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='trip', full_name='transit_realtime.EntitySelector.trip', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stop_id', full_name='transit_realtime.EntitySelector.stop_id', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=True,
  syntax='proto2',
  extension_ranges=[(1000, 2000), ],
  oneofs=[
  ],
  serialized_start=3465,
  serialized_end=3611,
)


_TRANSLATEDSTRING_TRANSLATION = _descriptor.Descriptor(
  name='Translation',
  full_name='transit_realtime.TranslatedString.Translation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='transit_realtime.TranslatedString.Translation.text', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='language', full_name='transit_realtime.TranslatedString.Translation.language', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=True,
  syntax='proto2',
  extension_ranges=[(1000, 2000), ],
  oneofs=[
  ],
  serialized_start=3703,
  serialized_end=3756,
)

_TRANSLATEDSTRING = _descriptor.Descriptor(
  name='TranslatedString',
  full_name='transit_realtime.TranslatedString',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='translation', full_name='transit_realtime.TranslatedString.translation', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_TRANSLATEDSTRING_TRANSLATION, ],
  enum_types=[
  ],
  options=None,
  is_extendable=True,
  syntax='proto2',
  extension_ranges=[(1000, 2000), ],
  oneofs=[
  ],
  serialized_start=3614,
  serialized_end=3764,
)


_TFNSWVEHICLEDESCRIPTOR = _descriptor.Descriptor(
  name='TfnswVehicleDescriptor',
  full_name='transit_realtime.TfnswVehicleDescriptor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='air_conditioned', full_name='transit_realtime.TfnswVehicleDescriptor.air_conditioned', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='wheelchair_accessible', full_name='transit_realtime.TfnswVehicleDescriptor.wheelchair_accessible', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vehicle_model', full_name='transit_realtime.TfnswVehicleDescriptor.vehicle_model', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='performing_prior_trip', full_name='transit_realtime.TfnswVehicleDescriptor.performing_prior_trip', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='special_vehicle_attributes', full_name='transit_realtime.TfnswVehicleDescriptor.special_vehicle_attributes', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=3767,
  serialized_end=3957,
)

_FEEDMESSAGE.fields_by_name['header'].message_type = _FEEDHEADER
_FEEDMESSAGE.fields_by_name['entity'].message_type = _FEEDENTITY
_FEEDHEADER.fields_by_name['incrementality'].enum_type = _FEEDHEADER_INCREMENTALITY
_FEEDHEADER_INCREMENTALITY.containing_type = _FEEDHEADER
_FEEDENTITY.fields_by_name['trip_update'].message_type = _TRIPUPDATE
_FEEDENTITY.fields_by_name['vehicle'].message_type = _VEHICLEPOSITION
_FEEDENTITY.fields_by_name['alert'].message_type = _ALERT
_TRIPUPDATE_STOPTIMEEVENT.containing_type = _TRIPUPDATE
_TRIPUPDATE_STOPTIMEUPDATE.fields_by_name['arrival'].message_type = _TRIPUPDATE_STOPTIMEEVENT
_TRIPUPDATE_STOPTIMEUPDATE.fields_by_name['departure'].message_type = _TRIPUPDATE_STOPTIMEEVENT
_TRIPUPDATE_STOPTIMEUPDATE.fields_by_name['schedule_relationship'].enum_type = _TRIPUPDATE_STOPTIMEUPDATE_SCHEDULERELATIONSHIP
_TRIPUPDATE_STOPTIMEUPDATE.containing_type = _TRIPUPDATE
_TRIPUPDATE_STOPTIMEUPDATE_SCHEDULERELATIONSHIP.containing_type = _TRIPUPDATE_STOPTIMEUPDATE
_TRIPUPDATE.fields_by_name['trip'].message_type = _TRIPDESCRIPTOR
_TRIPUPDATE.fields_by_name['vehicle'].message_type = _VEHICLEDESCRIPTOR
_TRIPUPDATE.fields_by_name['stop_time_update'].message_type = _TRIPUPDATE_STOPTIMEUPDATE
_VEHICLEPOSITION.fields_by_name['trip'].message_type = _TRIPDESCRIPTOR
_VEHICLEPOSITION.fields_by_name['vehicle'].message_type = _VEHICLEDESCRIPTOR
_VEHICLEPOSITION.fields_by_name['position'].message_type = _POSITION
_VEHICLEPOSITION.fields_by_name['current_status'].enum_type = _VEHICLEPOSITION_VEHICLESTOPSTATUS
_VEHICLEPOSITION.fields_by_name['congestion_level'].enum_type = _VEHICLEPOSITION_CONGESTIONLEVEL
_VEHICLEPOSITION.fields_by_name['occupancy_status'].enum_type = _VEHICLEPOSITION_OCCUPANCYSTATUS
_VEHICLEPOSITION_VEHICLESTOPSTATUS.containing_type = _VEHICLEPOSITION
_VEHICLEPOSITION_CONGESTIONLEVEL.containing_type = _VEHICLEPOSITION
_VEHICLEPOSITION_OCCUPANCYSTATUS.containing_type = _VEHICLEPOSITION
_ALERT.fields_by_name['active_period'].message_type = _TIMERANGE
_ALERT.fields_by_name['informed_entity'].message_type = _ENTITYSELECTOR
_ALERT.fields_by_name['cause'].enum_type = _ALERT_CAUSE
_ALERT.fields_by_name['effect'].enum_type = _ALERT_EFFECT
_ALERT.fields_by_name['url'].message_type = _TRANSLATEDSTRING
_ALERT.fields_by_name['header_text'].message_type = _TRANSLATEDSTRING
_ALERT.fields_by_name['description_text'].message_type = _TRANSLATEDSTRING
_ALERT_CAUSE.containing_type = _ALERT
_ALERT_EFFECT.containing_type = _ALERT
_TRIPDESCRIPTOR.fields_by_name['schedule_relationship'].enum_type = _TRIPDESCRIPTOR_SCHEDULERELATIONSHIP
_TRIPDESCRIPTOR_SCHEDULERELATIONSHIP.containing_type = _TRIPDESCRIPTOR
_ENTITYSELECTOR.fields_by_name['trip'].message_type = _TRIPDESCRIPTOR
_TRANSLATEDSTRING_TRANSLATION.containing_type = _TRANSLATEDSTRING
_TRANSLATEDSTRING.fields_by_name['translation'].message_type = _TRANSLATEDSTRING_TRANSLATION
DESCRIPTOR.message_types_by_name['FeedMessage'] = _FEEDMESSAGE
DESCRIPTOR.message_types_by_name['FeedHeader'] = _FEEDHEADER
DESCRIPTOR.message_types_by_name['FeedEntity'] = _FEEDENTITY
DESCRIPTOR.message_types_by_name['TripUpdate'] = _TRIPUPDATE
DESCRIPTOR.message_types_by_name['VehiclePosition'] = _VEHICLEPOSITION
DESCRIPTOR.message_types_by_name['Alert'] = _ALERT
DESCRIPTOR.message_types_by_name['TimeRange'] = _TIMERANGE
DESCRIPTOR.message_types_by_name['Position'] = _POSITION
DESCRIPTOR.message_types_by_name['TripDescriptor'] = _TRIPDESCRIPTOR
DESCRIPTOR.message_types_by_name['VehicleDescriptor'] = _VEHICLEDESCRIPTOR
DESCRIPTOR.message_types_by_name['EntitySelector'] = _ENTITYSELECTOR
DESCRIPTOR.message_types_by_name['TranslatedString'] = _TRANSLATEDSTRING
DESCRIPTOR.message_types_by_name['TfnswVehicleDescriptor'] = _TFNSWVEHICLEDESCRIPTOR
DESCRIPTOR.extensions_by_name['tfnsw_vehicle_descriptor'] = tfnsw_vehicle_descriptor
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FeedMessage = _reflection.GeneratedProtocolMessageType('FeedMessage', (_message.Message,), dict(
  DESCRIPTOR = _FEEDMESSAGE,
  __module__ = 'tfnsw_gtfs_realtime_pb2'
  # @@protoc_insertion_point(class_scope:transit_realtime.FeedMessage)
  ))
_sym_db.RegisterMessage(FeedMessage)

FeedHeader = _reflection.GeneratedProtocolMessageType('FeedHeader', (_message.Message,), dict(
  DESCRIPTOR = _FEEDHEADER,
  __module__ = 'tfnsw_gtfs_realtime_pb2'
  # @@protoc_insertion_point(class_scope:transit_realtime.FeedHeader)
  ))
_sym_db.RegisterMessage(FeedHeader)

FeedEntity = _reflection.GeneratedProtocolMessageType('FeedEntity', (_message.Message,), dict(
  DESCRIPTOR = _FEEDENTITY,
  __module__ = 'tfnsw_gtfs_realtime_pb2'
  # @@protoc_insertion_point(class_scope:transit_realtime.FeedEntity)
  ))
_sym_db.RegisterMessage(FeedEntity)

TripUpdate = _reflection.GeneratedProtocolMessageType('TripUpdate', (_message.Message,), dict(

  StopTimeEvent = _reflection.GeneratedProtocolMessageType('StopTimeEvent', (_message.Message,), dict(
    DESCRIPTOR = _TRIPUPDATE_STOPTIMEEVENT,
    __module__ = 'tfnsw_gtfs_realtime_pb2'
    # @@protoc_insertion_point(class_scope:transit_realtime.TripUpdate.StopTimeEvent)
    ))
  ,

  StopTimeUpdate = _reflection.GeneratedProtocolMessageType('StopTimeUpdate', (_message.Message,), dict(
    DESCRIPTOR = _TRIPUPDATE_STOPTIMEUPDATE,
    __module__ = 'tfnsw_gtfs_realtime_pb2'
    # @@protoc_insertion_point(class_scope:transit_realtime.TripUpdate.StopTimeUpdate)
    ))
  ,
  DESCRIPTOR = _TRIPUPDATE,
  __module__ = 'tfnsw_gtfs_realtime_pb2'
  # @@protoc_insertion_point(class_scope:transit_realtime.TripUpdate)
  ))
_sym_db.RegisterMessage(TripUpdate)
_sym_db.RegisterMessage(TripUpdate.StopTimeEvent)
_sym_db.RegisterMessage(TripUpdate.StopTimeUpdate)

VehiclePosition = _reflection.GeneratedProtocolMessageType('VehiclePosition', (_message.Message,), dict(
  DESCRIPTOR = _VEHICLEPOSITION,
  __module__ = 'tfnsw_gtfs_realtime_pb2'
  # @@protoc_insertion_point(class_scope:transit_realtime.VehiclePosition)
  ))
_sym_db.RegisterMessage(VehiclePosition)

Alert = _reflection.GeneratedProtocolMessageType('Alert', (_message.Message,), dict(
  DESCRIPTOR = _ALERT,
  __module__ = 'tfnsw_gtfs_realtime_pb2'
  # @@protoc_insertion_point(class_scope:transit_realtime.Alert)
  ))
_sym_db.RegisterMessage(Alert)

TimeRange = _reflection.GeneratedProtocolMessageType('TimeRange', (_message.Message,), dict(
  DESCRIPTOR = _TIMERANGE,
  __module__ = 'tfnsw_gtfs_realtime_pb2'
  # @@protoc_insertion_point(class_scope:transit_realtime.TimeRange)
  ))
_sym_db.RegisterMessage(TimeRange)

Position = _reflection.GeneratedProtocolMessageType('Position', (_message.Message,), dict(
  DESCRIPTOR = _POSITION,
  __module__ = 'tfnsw_gtfs_realtime_pb2'
  # @@protoc_insertion_point(class_scope:transit_realtime.Position)
  ))
_sym_db.RegisterMessage(Position)

TripDescriptor = _reflection.GeneratedProtocolMessageType('TripDescriptor', (_message.Message,), dict(
  DESCRIPTOR = _TRIPDESCRIPTOR,
  __module__ = 'tfnsw_gtfs_realtime_pb2'
  # @@protoc_insertion_point(class_scope:transit_realtime.TripDescriptor)
  ))
_sym_db.RegisterMessage(TripDescriptor)

VehicleDescriptor = _reflection.GeneratedProtocolMessageType('VehicleDescriptor', (_message.Message,), dict(
  DESCRIPTOR = _VEHICLEDESCRIPTOR,
  __module__ = 'tfnsw_gtfs_realtime_pb2'
  # @@protoc_insertion_point(class_scope:transit_realtime.VehicleDescriptor)
  ))
_sym_db.RegisterMessage(VehicleDescriptor)

EntitySelector = _reflection.GeneratedProtocolMessageType('EntitySelector', (_message.Message,), dict(
  DESCRIPTOR = _ENTITYSELECTOR,
  __module__ = 'tfnsw_gtfs_realtime_pb2'
  # @@protoc_insertion_point(class_scope:transit_realtime.EntitySelector)
  ))
_sym_db.RegisterMessage(EntitySelector)

TranslatedString = _reflection.GeneratedProtocolMessageType('TranslatedString', (_message.Message,), dict(

  Translation = _reflection.GeneratedProtocolMessageType('Translation', (_message.Message,), dict(
    DESCRIPTOR = _TRANSLATEDSTRING_TRANSLATION,
    __module__ = 'tfnsw_gtfs_realtime_pb2'
    # @@protoc_insertion_point(class_scope:transit_realtime.TranslatedString.Translation)
    ))
  ,
  DESCRIPTOR = _TRANSLATEDSTRING,
  __module__ = 'tfnsw_gtfs_realtime_pb2'
  # @@protoc_insertion_point(class_scope:transit_realtime.TranslatedString)
  ))
_sym_db.RegisterMessage(TranslatedString)
_sym_db.RegisterMessage(TranslatedString.Translation)

TfnswVehicleDescriptor = _reflection.GeneratedProtocolMessageType('TfnswVehicleDescriptor', (_message.Message,), dict(
  DESCRIPTOR = _TFNSWVEHICLEDESCRIPTOR,
  __module__ = 'tfnsw_gtfs_realtime_pb2'
  # @@protoc_insertion_point(class_scope:transit_realtime.TfnswVehicleDescriptor)
  ))
_sym_db.RegisterMessage(TfnswVehicleDescriptor)

tfnsw_vehicle_descriptor.message_type = _TFNSWVEHICLEDESCRIPTOR
VehicleDescriptor.RegisterExtension(tfnsw_vehicle_descriptor)

DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\033com.google.transit.realtime'))