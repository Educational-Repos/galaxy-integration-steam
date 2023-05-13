# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: steammessages_clientserver_login.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import steammessages_base_pb2 as steammessages__base__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&steammessages_clientserver_login.proto\x1a\x18steammessages_base.proto\")\n\x13\x43MsgClientHeartBeat\x12\x12\n\nsend_reply\x18\x01 \x01(\x08\"D\n CMsgClientServerTimestampRequest\x12 \n\x18\x63lient_request_timestamp\x18\x01 \x01(\x04\"b\n!CMsgClientServerTimestampResponse\x12 \n\x18\x63lient_request_timestamp\x18\x01 \x01(\x04\x12\x1b\n\x13server_timestamp_ms\x18\x02 \x01(\x04\"a\n\x10\x43MsgClientSecret\x12\x0f\n\x07version\x18\x01 \x01(\r\x12\r\n\x05\x61ppid\x18\x02 \x01(\r\x12\x10\n\x08\x64\x65viceid\x18\x03 \x01(\r\x12\r\n\x05nonce\x18\x04 \x01(\x06\x12\x0c\n\x04hmac\x18\x05 \x01(\x0c\"+\n\x0f\x43MsgClientHello\x12\x18\n\x10protocol_version\x18\x01 \x01(\r\"\xd3\x0c\n\x0f\x43MsgClientLogon\x12\x18\n\x10protocol_version\x18\x01 \x01(\r\x12*\n\"deprecated_obfustucated_private_ip\x18\x02 \x01(\r\x12\x0f\n\x07\x63\x65ll_id\x18\x03 \x01(\r\x12\x17\n\x0flast_session_id\x18\x04 \x01(\r\x12\x1e\n\x16\x63lient_package_version\x18\x05 \x01(\r\x12\x17\n\x0f\x63lient_language\x18\x06 \x01(\t\x12\x16\n\x0e\x63lient_os_type\x18\x07 \x01(\r\x12\'\n\x18should_remember_password\x18\x08 \x01(\x08:\x05\x66\x61lse\x12\x14\n\x0cwine_version\x18\t \x01(\t\x12\x15\n\rdeprecated_10\x18\n \x01(\r\x12-\n\x15obfuscated_private_ip\x18\x0b \x01(\x0b\x32\x0e.CMsgIPAddress\x12\x1c\n\x14\x64\x65precated_public_ip\x18\x14 \x01(\r\x12\x11\n\tqos_level\x18\x15 \x01(\r\x12 \n\x18\x63lient_supplied_steam_id\x18\x16 \x01(\x06\x12!\n\tpublic_ip\x18\x17 \x01(\x0b\x32\x0e.CMsgIPAddress\x12\x12\n\nmachine_id\x18\x1e \x01(\x0c\x12\x18\n\rlauncher_type\x18\x1f \x01(\r:\x01\x30\x12\x12\n\x07ui_mode\x18  \x01(\r:\x01\x30\x12\x14\n\tchat_mode\x18! \x01(\r:\x01\x30\x12\x1a\n\x12steam2_auth_ticket\x18) \x01(\x0c\x12\x15\n\remail_address\x18* \x01(\t\x12 \n\x18rtime32_account_creation\x18+ \x01(\x07\x12\x14\n\x0c\x61\x63\x63ount_name\x18\x32 \x01(\t\x12\x10\n\x08password\x18\x33 \x01(\t\x12\x19\n\x11game_server_token\x18\x34 \x01(\t\x12\x11\n\tlogin_key\x18< \x01(\t\x12+\n\x1cwas_converted_deprecated_msg\x18\x46 \x01(\x08:\x05\x66\x61lse\x12%\n\x1d\x61non_user_target_account_name\x18P \x01(\t\x12\x1e\n\x16resolved_user_steam_id\x18Q \x01(\x06\x12\x1a\n\x12\x65result_sentryfile\x18R \x01(\x05\x12\x16\n\x0esha_sentryfile\x18S \x01(\x0c\x12\x11\n\tauth_code\x18T \x01(\t\x12\x10\n\x08otp_type\x18U \x01(\x05\x12\x11\n\totp_value\x18V \x01(\r\x12\x16\n\x0eotp_identifier\x18W \x01(\t\x12\x1d\n\x15steam2_ticket_request\x18X \x01(\x08\x12\x17\n\x0fsony_psn_ticket\x18Z \x01(\x0c\x12\x1b\n\x13sony_psn_service_id\x18[ \x01(\t\x12\x36\n\'create_new_psn_linked_account_if_needed\x18\\ \x01(\x08:\x05\x66\x61lse\x12\x15\n\rsony_psn_name\x18] \x01(\t\x12\x1a\n\x12game_server_app_id\x18^ \x01(\x05\x12)\n!steamguard_dont_remember_computer\x18_ \x01(\x08\x12\x14\n\x0cmachine_name\x18` \x01(\t\x12\x1f\n\x17machine_name_userchosen\x18\x61 \x01(\t\x12\x18\n\x10\x63ountry_override\x18\x62 \x01(\t\x12\x14\n\x0cis_steam_box\x18\x63 \x01(\x08\x12\x1a\n\x12\x63lient_instance_id\x18\x64 \x01(\x04\x12\x17\n\x0ftwo_factor_code\x18\x65 \x01(\t\x12$\n\x1csupports_rate_limit_response\x18\x66 \x01(\x08\x12\x17\n\x0fweb_logon_nonce\x18g \x01(\t\x12\x17\n\x0fpriority_reason\x18h \x01(\x05\x12\x31\n\x16\x65mbedded_client_secret\x18i \x01(\x0b\x32\x11.CMsgClientSecret\x12\"\n\x1a\x64isable_partner_autogrants\x18j \x01(\x08\x12\x15\n\ris_steam_deck\x18k \x01(\x08\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18l \x01(\t\x12\x14\n\x0cis_chrome_os\x18m \x01(\x08\x12\x10\n\x08is_tesla\x18n \x01(\x08\"\x98\x06\n\x17\x43MsgClientLogonResponse\x12\x12\n\x07\x65result\x18\x01 \x01(\x05:\x01\x32\x12,\n$legacy_out_of_game_heartbeat_seconds\x18\x02 \x01(\x05\x12\x19\n\x11heartbeat_seconds\x18\x03 \x01(\x05\x12\x1c\n\x14\x64\x65precated_public_ip\x18\x04 \x01(\r\x12\x1b\n\x13rtime32_server_time\x18\x05 \x01(\x07\x12\x15\n\raccount_flags\x18\x06 \x01(\r\x12\x0f\n\x07\x63\x65ll_id\x18\x07 \x01(\r\x12\x14\n\x0c\x65mail_domain\x18\x08 \x01(\t\x12\x15\n\rsteam2_ticket\x18\t \x01(\x0c\x12\x18\n\x10\x65result_extended\x18\n \x01(\x05\x12&\n\x1ewebapi_authenticate_user_nonce\x18\x0b \x01(\t\x12\x1e\n\x16\x63\x65ll_id_ping_threshold\x18\x0c \x01(\r\x12\x1b\n\x13\x64\x65precated_use_pics\x18\r \x01(\x08\x12\x12\n\nvanity_url\x18\x0e \x01(\t\x12!\n\tpublic_ip\x18\x0f \x01(\x0b\x32\x0e.CMsgIPAddress\x12\x1f\n\x17\x63lient_supplied_steamid\x18\x14 \x01(\x06\x12\x17\n\x0fip_country_code\x18\x15 \x01(\t\x12\x19\n\x11parental_settings\x18\x16 \x01(\x0c\x12\"\n\x1aparental_setting_signature\x18\x17 \x01(\x0c\x12&\n\x1e\x63ount_loginfailures_to_migrate\x18\x18 \x01(\x05\x12$\n\x1c\x63ount_disconnects_to_migrate\x18\x19 \x01(\x05\x12#\n\x1bogs_data_report_time_window\x18\x1a \x01(\x05\x12\x1a\n\x12\x63lient_instance_id\x18\x1b \x01(\x04\x12!\n\x19\x66orce_client_update_check\x18\x1c \x01(\x08\x12\x1d\n\x15\x61greement_session_url\x18\x1d \x01(\t\x12\x10\n\x08token_id\x18\x1e \x01(\x04\"F\n,CMsgClientRequestWebAPIAuthenticateUserNonce\x12\x16\n\ntoken_type\x18\x01 \x01(\x05:\x02-1\"\x8a\x01\n4CMsgClientRequestWebAPIAuthenticateUserNonceResponse\x12\x12\n\x07\x65result\x18\x01 \x01(\x05:\x01\x32\x12&\n\x1ewebapi_authenticate_user_nonce\x18\x0b \x01(\t\x12\x16\n\ntoken_type\x18\x03 \x01(\x05:\x02-1\"\x12\n\x10\x43MsgClientLogOff\")\n\x13\x43MsgClientLoggedOff\x12\x12\n\x07\x65result\x18\x01 \x01(\x05:\x01\x32\"=\n\x15\x43MsgClientNewLoginKey\x12\x11\n\tunique_id\x18\x01 \x01(\r\x12\x11\n\tlogin_key\x18\x02 \x01(\t\"2\n\x1d\x43MsgClientNewLoginKeyAccepted\x12\x11\n\tunique_id\x18\x01 \x01(\r\"\xc7\x02\n\x15\x43MsgClientAccountInfo\x12\x14\n\x0cpersona_name\x18\x01 \x01(\t\x12\x12\n\nip_country\x18\x02 \x01(\t\x12\x1e\n\x16\x63ount_authed_computers\x18\x05 \x01(\x05\x12\x15\n\raccount_flags\x18\x07 \x01(\r\x12\x13\n\x0b\x66\x61\x63\x65\x62ook_id\x18\x08 \x01(\x04\x12\x15\n\rfacebook_name\x18\t \x01(\t\x12+\n#steamguard_machine_name_user_chosen\x18\x0f \x01(\t\x12\x19\n\x11is_phone_verified\x18\x10 \x01(\x08\x12\x18\n\x10two_factor_state\x18\x11 \x01(\r\x12\x1c\n\x14is_phone_identifying\x18\x12 \x01(\x08\x12!\n\x19is_phone_needing_reverify\x18\x13 \x01(\x08\"-\n\x1a\x43MsgClientChallengeRequest\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\"0\n\x1b\x43MsgClientChallengeResponse\x12\x11\n\tchallenge\x18\x01 \x01(\x06\x42\x05H\x01\x90\x01\x00')



_CMSGCLIENTHEARTBEAT = DESCRIPTOR.message_types_by_name['CMsgClientHeartBeat']
_CMSGCLIENTSERVERTIMESTAMPREQUEST = DESCRIPTOR.message_types_by_name['CMsgClientServerTimestampRequest']
_CMSGCLIENTSERVERTIMESTAMPRESPONSE = DESCRIPTOR.message_types_by_name['CMsgClientServerTimestampResponse']
_CMSGCLIENTSECRET = DESCRIPTOR.message_types_by_name['CMsgClientSecret']
_CMSGCLIENTHELLO = DESCRIPTOR.message_types_by_name['CMsgClientHello']
_CMSGCLIENTLOGON = DESCRIPTOR.message_types_by_name['CMsgClientLogon']
_CMSGCLIENTLOGONRESPONSE = DESCRIPTOR.message_types_by_name['CMsgClientLogonResponse']
_CMSGCLIENTREQUESTWEBAPIAUTHENTICATEUSERNONCE = DESCRIPTOR.message_types_by_name['CMsgClientRequestWebAPIAuthenticateUserNonce']
_CMSGCLIENTREQUESTWEBAPIAUTHENTICATEUSERNONCERESPONSE = DESCRIPTOR.message_types_by_name['CMsgClientRequestWebAPIAuthenticateUserNonceResponse']
_CMSGCLIENTLOGOFF = DESCRIPTOR.message_types_by_name['CMsgClientLogOff']
_CMSGCLIENTLOGGEDOFF = DESCRIPTOR.message_types_by_name['CMsgClientLoggedOff']
_CMSGCLIENTNEWLOGINKEY = DESCRIPTOR.message_types_by_name['CMsgClientNewLoginKey']
_CMSGCLIENTNEWLOGINKEYACCEPTED = DESCRIPTOR.message_types_by_name['CMsgClientNewLoginKeyAccepted']
_CMSGCLIENTACCOUNTINFO = DESCRIPTOR.message_types_by_name['CMsgClientAccountInfo']
_CMSGCLIENTCHALLENGEREQUEST = DESCRIPTOR.message_types_by_name['CMsgClientChallengeRequest']
_CMSGCLIENTCHALLENGERESPONSE = DESCRIPTOR.message_types_by_name['CMsgClientChallengeResponse']
CMsgClientHeartBeat = _reflection.GeneratedProtocolMessageType('CMsgClientHeartBeat', (_message.Message,), {
  'DESCRIPTOR' : _CMSGCLIENTHEARTBEAT,
  '__module__' : 'steammessages_clientserver_login_pb2'
  # @@protoc_insertion_point(class_scope:CMsgClientHeartBeat)
  })
_sym_db.RegisterMessage(CMsgClientHeartBeat)

CMsgClientServerTimestampRequest = _reflection.GeneratedProtocolMessageType('CMsgClientServerTimestampRequest', (_message.Message,), {
  'DESCRIPTOR' : _CMSGCLIENTSERVERTIMESTAMPREQUEST,
  '__module__' : 'steammessages_clientserver_login_pb2'
  # @@protoc_insertion_point(class_scope:CMsgClientServerTimestampRequest)
  })
_sym_db.RegisterMessage(CMsgClientServerTimestampRequest)

CMsgClientServerTimestampResponse = _reflection.GeneratedProtocolMessageType('CMsgClientServerTimestampResponse', (_message.Message,), {
  'DESCRIPTOR' : _CMSGCLIENTSERVERTIMESTAMPRESPONSE,
  '__module__' : 'steammessages_clientserver_login_pb2'
  # @@protoc_insertion_point(class_scope:CMsgClientServerTimestampResponse)
  })
_sym_db.RegisterMessage(CMsgClientServerTimestampResponse)

CMsgClientSecret = _reflection.GeneratedProtocolMessageType('CMsgClientSecret', (_message.Message,), {
  'DESCRIPTOR' : _CMSGCLIENTSECRET,
  '__module__' : 'steammessages_clientserver_login_pb2'
  # @@protoc_insertion_point(class_scope:CMsgClientSecret)
  })
_sym_db.RegisterMessage(CMsgClientSecret)

CMsgClientHello = _reflection.GeneratedProtocolMessageType('CMsgClientHello', (_message.Message,), {
  'DESCRIPTOR' : _CMSGCLIENTHELLO,
  '__module__' : 'steammessages_clientserver_login_pb2'
  # @@protoc_insertion_point(class_scope:CMsgClientHello)
  })
_sym_db.RegisterMessage(CMsgClientHello)

CMsgClientLogon = _reflection.GeneratedProtocolMessageType('CMsgClientLogon', (_message.Message,), {
  'DESCRIPTOR' : _CMSGCLIENTLOGON,
  '__module__' : 'steammessages_clientserver_login_pb2'
  # @@protoc_insertion_point(class_scope:CMsgClientLogon)
  })
_sym_db.RegisterMessage(CMsgClientLogon)

CMsgClientLogonResponse = _reflection.GeneratedProtocolMessageType('CMsgClientLogonResponse', (_message.Message,), {
  'DESCRIPTOR' : _CMSGCLIENTLOGONRESPONSE,
  '__module__' : 'steammessages_clientserver_login_pb2'
  # @@protoc_insertion_point(class_scope:CMsgClientLogonResponse)
  })
_sym_db.RegisterMessage(CMsgClientLogonResponse)

CMsgClientRequestWebAPIAuthenticateUserNonce = _reflection.GeneratedProtocolMessageType('CMsgClientRequestWebAPIAuthenticateUserNonce', (_message.Message,), {
  'DESCRIPTOR' : _CMSGCLIENTREQUESTWEBAPIAUTHENTICATEUSERNONCE,
  '__module__' : 'steammessages_clientserver_login_pb2'
  # @@protoc_insertion_point(class_scope:CMsgClientRequestWebAPIAuthenticateUserNonce)
  })
_sym_db.RegisterMessage(CMsgClientRequestWebAPIAuthenticateUserNonce)

CMsgClientRequestWebAPIAuthenticateUserNonceResponse = _reflection.GeneratedProtocolMessageType('CMsgClientRequestWebAPIAuthenticateUserNonceResponse', (_message.Message,), {
  'DESCRIPTOR' : _CMSGCLIENTREQUESTWEBAPIAUTHENTICATEUSERNONCERESPONSE,
  '__module__' : 'steammessages_clientserver_login_pb2'
  # @@protoc_insertion_point(class_scope:CMsgClientRequestWebAPIAuthenticateUserNonceResponse)
  })
_sym_db.RegisterMessage(CMsgClientRequestWebAPIAuthenticateUserNonceResponse)

CMsgClientLogOff = _reflection.GeneratedProtocolMessageType('CMsgClientLogOff', (_message.Message,), {
  'DESCRIPTOR' : _CMSGCLIENTLOGOFF,
  '__module__' : 'steammessages_clientserver_login_pb2'
  # @@protoc_insertion_point(class_scope:CMsgClientLogOff)
  })
_sym_db.RegisterMessage(CMsgClientLogOff)

CMsgClientLoggedOff = _reflection.GeneratedProtocolMessageType('CMsgClientLoggedOff', (_message.Message,), {
  'DESCRIPTOR' : _CMSGCLIENTLOGGEDOFF,
  '__module__' : 'steammessages_clientserver_login_pb2'
  # @@protoc_insertion_point(class_scope:CMsgClientLoggedOff)
  })
_sym_db.RegisterMessage(CMsgClientLoggedOff)

CMsgClientNewLoginKey = _reflection.GeneratedProtocolMessageType('CMsgClientNewLoginKey', (_message.Message,), {
  'DESCRIPTOR' : _CMSGCLIENTNEWLOGINKEY,
  '__module__' : 'steammessages_clientserver_login_pb2'
  # @@protoc_insertion_point(class_scope:CMsgClientNewLoginKey)
  })
_sym_db.RegisterMessage(CMsgClientNewLoginKey)

CMsgClientNewLoginKeyAccepted = _reflection.GeneratedProtocolMessageType('CMsgClientNewLoginKeyAccepted', (_message.Message,), {
  'DESCRIPTOR' : _CMSGCLIENTNEWLOGINKEYACCEPTED,
  '__module__' : 'steammessages_clientserver_login_pb2'
  # @@protoc_insertion_point(class_scope:CMsgClientNewLoginKeyAccepted)
  })
_sym_db.RegisterMessage(CMsgClientNewLoginKeyAccepted)

CMsgClientAccountInfo = _reflection.GeneratedProtocolMessageType('CMsgClientAccountInfo', (_message.Message,), {
  'DESCRIPTOR' : _CMSGCLIENTACCOUNTINFO,
  '__module__' : 'steammessages_clientserver_login_pb2'
  # @@protoc_insertion_point(class_scope:CMsgClientAccountInfo)
  })
_sym_db.RegisterMessage(CMsgClientAccountInfo)

CMsgClientChallengeRequest = _reflection.GeneratedProtocolMessageType('CMsgClientChallengeRequest', (_message.Message,), {
  'DESCRIPTOR' : _CMSGCLIENTCHALLENGEREQUEST,
  '__module__' : 'steammessages_clientserver_login_pb2'
  # @@protoc_insertion_point(class_scope:CMsgClientChallengeRequest)
  })
_sym_db.RegisterMessage(CMsgClientChallengeRequest)

CMsgClientChallengeResponse = _reflection.GeneratedProtocolMessageType('CMsgClientChallengeResponse', (_message.Message,), {
  'DESCRIPTOR' : _CMSGCLIENTCHALLENGERESPONSE,
  '__module__' : 'steammessages_clientserver_login_pb2'
  # @@protoc_insertion_point(class_scope:CMsgClientChallengeResponse)
  })
_sym_db.RegisterMessage(CMsgClientChallengeResponse)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'H\001\220\001\000'
  _CMSGCLIENTHEARTBEAT._serialized_start=68
  _CMSGCLIENTHEARTBEAT._serialized_end=109
  _CMSGCLIENTSERVERTIMESTAMPREQUEST._serialized_start=111
  _CMSGCLIENTSERVERTIMESTAMPREQUEST._serialized_end=179
  _CMSGCLIENTSERVERTIMESTAMPRESPONSE._serialized_start=181
  _CMSGCLIENTSERVERTIMESTAMPRESPONSE._serialized_end=279
  _CMSGCLIENTSECRET._serialized_start=281
  _CMSGCLIENTSECRET._serialized_end=378
  _CMSGCLIENTHELLO._serialized_start=380
  _CMSGCLIENTHELLO._serialized_end=423
  _CMSGCLIENTLOGON._serialized_start=426
  _CMSGCLIENTLOGON._serialized_end=2045
  _CMSGCLIENTLOGONRESPONSE._serialized_start=2048
  _CMSGCLIENTLOGONRESPONSE._serialized_end=2840
  _CMSGCLIENTREQUESTWEBAPIAUTHENTICATEUSERNONCE._serialized_start=2842
  _CMSGCLIENTREQUESTWEBAPIAUTHENTICATEUSERNONCE._serialized_end=2912
  _CMSGCLIENTREQUESTWEBAPIAUTHENTICATEUSERNONCERESPONSE._serialized_start=2915
  _CMSGCLIENTREQUESTWEBAPIAUTHENTICATEUSERNONCERESPONSE._serialized_end=3053
  _CMSGCLIENTLOGOFF._serialized_start=3055
  _CMSGCLIENTLOGOFF._serialized_end=3073
  _CMSGCLIENTLOGGEDOFF._serialized_start=3075
  _CMSGCLIENTLOGGEDOFF._serialized_end=3116
  _CMSGCLIENTNEWLOGINKEY._serialized_start=3118
  _CMSGCLIENTNEWLOGINKEY._serialized_end=3179
  _CMSGCLIENTNEWLOGINKEYACCEPTED._serialized_start=3181
  _CMSGCLIENTNEWLOGINKEYACCEPTED._serialized_end=3231
  _CMSGCLIENTACCOUNTINFO._serialized_start=3234
  _CMSGCLIENTACCOUNTINFO._serialized_end=3561
  _CMSGCLIENTCHALLENGEREQUEST._serialized_start=3563
  _CMSGCLIENTCHALLENGEREQUEST._serialized_end=3608
  _CMSGCLIENTCHALLENGERESPONSE._serialized_start=3610
  _CMSGCLIENTCHALLENGERESPONSE._serialized_end=3658
# @@protoc_insertion_point(module_scope)
