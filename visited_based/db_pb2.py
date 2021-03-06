# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: db.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='db.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x08\x64\x62.proto\"\x10\n\x02Id\x12\n\n\x02id\x18\x01 \x01(\t\"S\n\x06\x41\x64\x44\x61ta\x12\x0c\n\x04tags\x18\x01 \x03(\t\x12\x13\n\x0b\x63lickers_id\x18\x02 \x03(\t\x12\x10\n\x08pub_date\x18\x03 \x01(\t\x12\x14\n\x0cpublisher_id\x18\x04 \x01(\t\"g\n\x08PostData\x12\x0c\n\x04tags\x18\x01 \x03(\t\x12\x12\n\nviewers_id\x18\x02 \x03(\t\x12\x11\n\tlikers_id\x18\x03 \x03(\t\x12\x10\n\x08pub_date\x18\x04 \x01(\t\x12\x14\n\x0cpublisher_id\x18\x05 \x01(\t\"P\n\x08UserData\x12\x15\n\rclicked_ad_id\x18\x01 \x03(\t\x12\x16\n\x0eviewed_post_id\x18\x02 \x03(\t\x12\x15\n\rliked_post_id\x18\x03 \x03(\t\"\x12\n\x03Tag\x12\x0b\n\x03tag\x18\x01 \x01(\t\"\x19\n\x05Posts\x12\x10\n\x08posts_id\x18\x01 \x03(\t\"\x15\n\x03\x41\x64s\x12\x0e\n\x06\x61\x64s_id\x18\x01 \x03(\t2\xdd\x01\n\x08\x64\x62handle\x12\x1c\n\nAdIdToData\x12\x03.Id\x1a\x07.AdData\"\x00\x12 \n\x0cPostIdtoData\x12\x03.Id\x1a\t.PostData\"\x00\x12 \n\x0cUserIdtoData\x12\x03.Id\x1a\t.UserData\"\x00\x12\x1b\n\tTagToPost\x12\x04.Tag\x1a\x06.Posts\"\x00\x12\x17\n\x07TagToAd\x12\x04.Tag\x1a\x04.Ads\"\x00\x12\x1e\n\rAuthorToPosts\x12\x03.Id\x1a\x06.Posts\"\x00\x12\x19\n\nAuthorToAd\x12\x03.Id\x1a\x04.Ads\"\x00\x62\x06proto3'
)




_ID = _descriptor.Descriptor(
  name='Id',
  full_name='Id',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Id.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=12,
  serialized_end=28,
)


_ADDATA = _descriptor.Descriptor(
  name='AdData',
  full_name='AdData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tags', full_name='AdData.tags', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='clickers_id', full_name='AdData.clickers_id', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pub_date', full_name='AdData.pub_date', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='publisher_id', full_name='AdData.publisher_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=30,
  serialized_end=113,
)


_POSTDATA = _descriptor.Descriptor(
  name='PostData',
  full_name='PostData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tags', full_name='PostData.tags', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='viewers_id', full_name='PostData.viewers_id', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='likers_id', full_name='PostData.likers_id', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pub_date', full_name='PostData.pub_date', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='publisher_id', full_name='PostData.publisher_id', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=115,
  serialized_end=218,
)


_USERDATA = _descriptor.Descriptor(
  name='UserData',
  full_name='UserData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='clicked_ad_id', full_name='UserData.clicked_ad_id', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='viewed_post_id', full_name='UserData.viewed_post_id', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='liked_post_id', full_name='UserData.liked_post_id', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=220,
  serialized_end=300,
)


_TAG = _descriptor.Descriptor(
  name='Tag',
  full_name='Tag',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tag', full_name='Tag.tag', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=302,
  serialized_end=320,
)


_POSTS = _descriptor.Descriptor(
  name='Posts',
  full_name='Posts',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='posts_id', full_name='Posts.posts_id', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=322,
  serialized_end=347,
)


_ADS = _descriptor.Descriptor(
  name='Ads',
  full_name='Ads',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ads_id', full_name='Ads.ads_id', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=349,
  serialized_end=370,
)

DESCRIPTOR.message_types_by_name['Id'] = _ID
DESCRIPTOR.message_types_by_name['AdData'] = _ADDATA
DESCRIPTOR.message_types_by_name['PostData'] = _POSTDATA
DESCRIPTOR.message_types_by_name['UserData'] = _USERDATA
DESCRIPTOR.message_types_by_name['Tag'] = _TAG
DESCRIPTOR.message_types_by_name['Posts'] = _POSTS
DESCRIPTOR.message_types_by_name['Ads'] = _ADS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Id = _reflection.GeneratedProtocolMessageType('Id', (_message.Message,), {
  'DESCRIPTOR' : _ID,
  '__module__' : 'db_pb2'
  # @@protoc_insertion_point(class_scope:Id)
  })
_sym_db.RegisterMessage(Id)

AdData = _reflection.GeneratedProtocolMessageType('AdData', (_message.Message,), {
  'DESCRIPTOR' : _ADDATA,
  '__module__' : 'db_pb2'
  # @@protoc_insertion_point(class_scope:AdData)
  })
_sym_db.RegisterMessage(AdData)

PostData = _reflection.GeneratedProtocolMessageType('PostData', (_message.Message,), {
  'DESCRIPTOR' : _POSTDATA,
  '__module__' : 'db_pb2'
  # @@protoc_insertion_point(class_scope:PostData)
  })
_sym_db.RegisterMessage(PostData)

UserData = _reflection.GeneratedProtocolMessageType('UserData', (_message.Message,), {
  'DESCRIPTOR' : _USERDATA,
  '__module__' : 'db_pb2'
  # @@protoc_insertion_point(class_scope:UserData)
  })
_sym_db.RegisterMessage(UserData)

Tag = _reflection.GeneratedProtocolMessageType('Tag', (_message.Message,), {
  'DESCRIPTOR' : _TAG,
  '__module__' : 'db_pb2'
  # @@protoc_insertion_point(class_scope:Tag)
  })
_sym_db.RegisterMessage(Tag)

Posts = _reflection.GeneratedProtocolMessageType('Posts', (_message.Message,), {
  'DESCRIPTOR' : _POSTS,
  '__module__' : 'db_pb2'
  # @@protoc_insertion_point(class_scope:Posts)
  })
_sym_db.RegisterMessage(Posts)

Ads = _reflection.GeneratedProtocolMessageType('Ads', (_message.Message,), {
  'DESCRIPTOR' : _ADS,
  '__module__' : 'db_pb2'
  # @@protoc_insertion_point(class_scope:Ads)
  })
_sym_db.RegisterMessage(Ads)



_DBHANDLE = _descriptor.ServiceDescriptor(
  name='dbhandle',
  full_name='dbhandle',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=373,
  serialized_end=594,
  methods=[
  _descriptor.MethodDescriptor(
    name='AdIdToData',
    full_name='dbhandle.AdIdToData',
    index=0,
    containing_service=None,
    input_type=_ID,
    output_type=_ADDATA,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='PostIdtoData',
    full_name='dbhandle.PostIdtoData',
    index=1,
    containing_service=None,
    input_type=_ID,
    output_type=_POSTDATA,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UserIdtoData',
    full_name='dbhandle.UserIdtoData',
    index=2,
    containing_service=None,
    input_type=_ID,
    output_type=_USERDATA,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='TagToPost',
    full_name='dbhandle.TagToPost',
    index=3,
    containing_service=None,
    input_type=_TAG,
    output_type=_POSTS,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='TagToAd',
    full_name='dbhandle.TagToAd',
    index=4,
    containing_service=None,
    input_type=_TAG,
    output_type=_ADS,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='AuthorToPosts',
    full_name='dbhandle.AuthorToPosts',
    index=5,
    containing_service=None,
    input_type=_ID,
    output_type=_POSTS,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='AuthorToAd',
    full_name='dbhandle.AuthorToAd',
    index=6,
    containing_service=None,
    input_type=_ID,
    output_type=_ADS,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_DBHANDLE)

DESCRIPTOR.services_by_name['dbhandle'] = _DBHANDLE

# @@protoc_insertion_point(module_scope)
