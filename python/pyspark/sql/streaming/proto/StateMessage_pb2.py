#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: org/apache/spark/sql/execution/streaming/StateMessage.proto
# Protobuf Python Version: 5.28.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    3,
    "",
    "org/apache/spark/sql/execution/streaming/StateMessage.proto",
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n;org/apache/spark/sql/execution/streaming/StateMessage.proto\x12.org.apache.spark.sql.execution.streaming.state"\x84\x05\n\x0cStateRequest\x12\x18\n\x07version\x18\x01 \x01(\x05R\x07version\x12}\n\x15statefulProcessorCall\x18\x02 \x01(\x0b\x32\x45.org.apache.spark.sql.execution.streaming.state.StatefulProcessorCallH\x00R\x15statefulProcessorCall\x12z\n\x14stateVariableRequest\x18\x03 \x01(\x0b\x32\x44.org.apache.spark.sql.execution.streaming.state.StateVariableRequestH\x00R\x14stateVariableRequest\x12\x8c\x01\n\x1aimplicitGroupingKeyRequest\x18\x04 \x01(\x0b\x32J.org.apache.spark.sql.execution.streaming.state.ImplicitGroupingKeyRequestH\x00R\x1aimplicitGroupingKeyRequest\x12\x62\n\x0ctimerRequest\x18\x05 \x01(\x0b\x32<.org.apache.spark.sql.execution.streaming.state.TimerRequestH\x00R\x0ctimerRequest\x12\x62\n\x0cutilsRequest\x18\x06 \x01(\x0b\x32<.org.apache.spark.sql.execution.streaming.state.UtilsRequestH\x00R\x0cutilsRequestB\x08\n\x06method"i\n\rStateResponse\x12\x1e\n\nstatusCode\x18\x01 \x01(\x05R\nstatusCode\x12"\n\x0c\x65rrorMessage\x18\x02 \x01(\tR\x0c\x65rrorMessage\x12\x14\n\x05value\x18\x03 \x01(\x0cR\x05value"x\n\x1cStateResponseWithLongTypeVal\x12\x1e\n\nstatusCode\x18\x01 \x01(\x05R\nstatusCode\x12"\n\x0c\x65rrorMessage\x18\x02 \x01(\tR\x0c\x65rrorMessage\x12\x14\n\x05value\x18\x03 \x01(\x03R\x05value"z\n\x1eStateResponseWithStringTypeVal\x12\x1e\n\nstatusCode\x18\x01 \x01(\x05R\nstatusCode\x12"\n\x0c\x65rrorMessage\x18\x02 \x01(\tR\x0c\x65rrorMessage\x12\x14\n\x05value\x18\x03 \x01(\tR\x05value"\xa0\x01\n\x18StateResponseWithListGet\x12\x1e\n\nstatusCode\x18\x01 \x01(\x05R\nstatusCode\x12"\n\x0c\x65rrorMessage\x18\x02 \x01(\tR\x0c\x65rrorMessage\x12\x14\n\x05value\x18\x03 \x03(\x0cR\x05value\x12*\n\x10requireNextFetch\x18\x04 \x01(\x08R\x10requireNextFetch"\xa8\x01\n StateResponseWithMapKeysOrValues\x12\x1e\n\nstatusCode\x18\x01 \x01(\x05R\nstatusCode\x12"\n\x0c\x65rrorMessage\x18\x02 \x01(\tR\x0c\x65rrorMessage\x12\x14\n\x05value\x18\x03 \x03(\x0cR\x05value\x12*\n\x10requireNextFetch\x18\x04 \x01(\x08R\x10requireNextFetch"9\n\x0fKeyAndValuePair\x12\x10\n\x03key\x18\x01 \x01(\x0cR\x03key\x12\x14\n\x05value\x18\x02 \x01(\x0cR\x05value"\xe7\x01\n\x1cStateResponseWithMapIterator\x12\x1e\n\nstatusCode\x18\x01 \x01(\x05R\nstatusCode\x12"\n\x0c\x65rrorMessage\x18\x02 \x01(\tR\x0c\x65rrorMessage\x12W\n\x06kvPair\x18\x03 \x03(\x0b\x32?.org.apache.spark.sql.execution.streaming.state.KeyAndValuePairR\x06kvPair\x12*\n\x10requireNextFetch\x18\x04 \x01(\x08R\x10requireNextFetch"\xa0\x05\n\x15StatefulProcessorCall\x12h\n\x0esetHandleState\x18\x01 \x01(\x0b\x32>.org.apache.spark.sql.execution.streaming.state.SetHandleStateH\x00R\x0esetHandleState\x12h\n\rgetValueState\x18\x02 \x01(\x0b\x32@.org.apache.spark.sql.execution.streaming.state.StateCallCommandH\x00R\rgetValueState\x12\x66\n\x0cgetListState\x18\x03 \x01(\x0b\x32@.org.apache.spark.sql.execution.streaming.state.StateCallCommandH\x00R\x0cgetListState\x12\x64\n\x0bgetMapState\x18\x04 \x01(\x0b\x32@.org.apache.spark.sql.execution.streaming.state.StateCallCommandH\x00R\x0bgetMapState\x12o\n\x0etimerStateCall\x18\x05 \x01(\x0b\x32\x45.org.apache.spark.sql.execution.streaming.state.TimerStateCallCommandH\x00R\x0etimerStateCall\x12j\n\x0e\x64\x65leteIfExists\x18\x06 \x01(\x0b\x32@.org.apache.spark.sql.execution.streaming.state.StateCallCommandH\x00R\x0e\x64\x65leteIfExistsB\x08\n\x06method"\xd5\x02\n\x14StateVariableRequest\x12h\n\x0evalueStateCall\x18\x01 \x01(\x0b\x32>.org.apache.spark.sql.execution.streaming.state.ValueStateCallH\x00R\x0evalueStateCall\x12\x65\n\rlistStateCall\x18\x02 \x01(\x0b\x32=.org.apache.spark.sql.execution.streaming.state.ListStateCallH\x00R\rlistStateCall\x12\x62\n\x0cmapStateCall\x18\x03 \x01(\x0b\x32<.org.apache.spark.sql.execution.streaming.state.MapStateCallH\x00R\x0cmapStateCallB\x08\n\x06method"\x83\x02\n\x1aImplicitGroupingKeyRequest\x12h\n\x0esetImplicitKey\x18\x01 \x01(\x0b\x32>.org.apache.spark.sql.execution.streaming.state.SetImplicitKeyH\x00R\x0esetImplicitKey\x12q\n\x11removeImplicitKey\x18\x02 \x01(\x0b\x32\x41.org.apache.spark.sql.execution.streaming.state.RemoveImplicitKeyH\x00R\x11removeImplicitKeyB\x08\n\x06method"\x81\x02\n\x0cTimerRequest\x12q\n\x11timerValueRequest\x18\x01 \x01(\x0b\x32\x41.org.apache.spark.sql.execution.streaming.state.TimerValueRequestH\x00R\x11timerValueRequest\x12t\n\x12\x65xpiryTimerRequest\x18\x02 \x01(\x0b\x32\x42.org.apache.spark.sql.execution.streaming.state.ExpiryTimerRequestH\x00R\x12\x65xpiryTimerRequestB\x08\n\x06method"\xf6\x01\n\x11TimerValueRequest\x12s\n\x12getProcessingTimer\x18\x01 \x01(\x0b\x32\x41.org.apache.spark.sql.execution.streaming.state.GetProcessingTimeH\x00R\x12getProcessingTimer\x12\x62\n\x0cgetWatermark\x18\x02 \x01(\x0b\x32<.org.apache.spark.sql.execution.streaming.state.GetWatermarkH\x00R\x0cgetWatermarkB\x08\n\x06method"B\n\x12\x45xpiryTimerRequest\x12,\n\x11\x65xpiryTimestampMs\x18\x01 \x01(\x03R\x11\x65xpiryTimestampMs"\x13\n\x11GetProcessingTime"\x0e\n\x0cGetWatermark"\x8b\x01\n\x0cUtilsRequest\x12q\n\x11parseStringSchema\x18\x01 \x01(\x0b\x32\x41.org.apache.spark.sql.execution.streaming.state.ParseStringSchemaH\x00R\x11parseStringSchemaB\x08\n\x06method"+\n\x11ParseStringSchema\x12\x16\n\x06schema\x18\x01 \x01(\tR\x06schema"\xc7\x01\n\x10StateCallCommand\x12\x1c\n\tstateName\x18\x01 \x01(\tR\tstateName\x12\x16\n\x06schema\x18\x02 \x01(\tR\x06schema\x12\x30\n\x13mapStateValueSchema\x18\x03 \x01(\tR\x13mapStateValueSchema\x12K\n\x03ttl\x18\x04 \x01(\x0b\x32\x39.org.apache.spark.sql.execution.streaming.state.TTLConfigR\x03ttl"\xa7\x02\n\x15TimerStateCallCommand\x12[\n\x08register\x18\x01 \x01(\x0b\x32=.org.apache.spark.sql.execution.streaming.state.RegisterTimerH\x00R\x08register\x12U\n\x06\x64\x65lete\x18\x02 \x01(\x0b\x32;.org.apache.spark.sql.execution.streaming.state.DeleteTimerH\x00R\x06\x64\x65lete\x12P\n\x04list\x18\x03 \x01(\x0b\x32:.org.apache.spark.sql.execution.streaming.state.ListTimersH\x00R\x04listB\x08\n\x06method"\x92\x03\n\x0eValueStateCall\x12\x1c\n\tstateName\x18\x01 \x01(\tR\tstateName\x12P\n\x06\x65xists\x18\x02 \x01(\x0b\x32\x36.org.apache.spark.sql.execution.streaming.state.ExistsH\x00R\x06\x65xists\x12G\n\x03get\x18\x03 \x01(\x0b\x32\x33.org.apache.spark.sql.execution.streaming.state.GetH\x00R\x03get\x12n\n\x10valueStateUpdate\x18\x04 \x01(\x0b\x32@.org.apache.spark.sql.execution.streaming.state.ValueStateUpdateH\x00R\x10valueStateUpdate\x12M\n\x05\x63lear\x18\x05 \x01(\x0b\x32\x35.org.apache.spark.sql.execution.streaming.state.ClearH\x00R\x05\x63learB\x08\n\x06method"\xdf\x04\n\rListStateCall\x12\x1c\n\tstateName\x18\x01 \x01(\tR\tstateName\x12P\n\x06\x65xists\x18\x02 \x01(\x0b\x32\x36.org.apache.spark.sql.execution.streaming.state.ExistsH\x00R\x06\x65xists\x12\x62\n\x0clistStateGet\x18\x03 \x01(\x0b\x32<.org.apache.spark.sql.execution.streaming.state.ListStateGetH\x00R\x0clistStateGet\x12\x62\n\x0clistStatePut\x18\x04 \x01(\x0b\x32<.org.apache.spark.sql.execution.streaming.state.ListStatePutH\x00R\x0clistStatePut\x12_\n\x0b\x61ppendValue\x18\x05 \x01(\x0b\x32;.org.apache.spark.sql.execution.streaming.state.AppendValueH\x00R\x0b\x61ppendValue\x12\\\n\nappendList\x18\x06 \x01(\x0b\x32:.org.apache.spark.sql.execution.streaming.state.AppendListH\x00R\nappendList\x12M\n\x05\x63lear\x18\x07 \x01(\x0b\x32\x35.org.apache.spark.sql.execution.streaming.state.ClearH\x00R\x05\x63learB\x08\n\x06method"\xc2\x06\n\x0cMapStateCall\x12\x1c\n\tstateName\x18\x01 \x01(\tR\tstateName\x12P\n\x06\x65xists\x18\x02 \x01(\x0b\x32\x36.org.apache.spark.sql.execution.streaming.state.ExistsH\x00R\x06\x65xists\x12V\n\x08getValue\x18\x03 \x01(\x0b\x32\x38.org.apache.spark.sql.execution.streaming.state.GetValueH\x00R\x08getValue\x12_\n\x0b\x63ontainsKey\x18\x04 \x01(\x0b\x32;.org.apache.spark.sql.execution.streaming.state.ContainsKeyH\x00R\x0b\x63ontainsKey\x12_\n\x0bupdateValue\x18\x05 \x01(\x0b\x32;.org.apache.spark.sql.execution.streaming.state.UpdateValueH\x00R\x0bupdateValue\x12V\n\x08iterator\x18\x06 \x01(\x0b\x32\x38.org.apache.spark.sql.execution.streaming.state.IteratorH\x00R\x08iterator\x12J\n\x04keys\x18\x07 \x01(\x0b\x32\x34.org.apache.spark.sql.execution.streaming.state.KeysH\x00R\x04keys\x12P\n\x06values\x18\x08 \x01(\x0b\x32\x36.org.apache.spark.sql.execution.streaming.state.ValuesH\x00R\x06values\x12Y\n\tremoveKey\x18\t \x01(\x0b\x32\x39.org.apache.spark.sql.execution.streaming.state.RemoveKeyH\x00R\tremoveKey\x12M\n\x05\x63lear\x18\n \x01(\x0b\x32\x35.org.apache.spark.sql.execution.streaming.state.ClearH\x00R\x05\x63learB\x08\n\x06method""\n\x0eSetImplicitKey\x12\x10\n\x03key\x18\x01 \x01(\x0cR\x03key"\x13\n\x11RemoveImplicitKey"\x08\n\x06\x45xists"\x05\n\x03Get"=\n\rRegisterTimer\x12,\n\x11\x65xpiryTimestampMs\x18\x01 \x01(\x03R\x11\x65xpiryTimestampMs";\n\x0b\x44\x65leteTimer\x12,\n\x11\x65xpiryTimestampMs\x18\x01 \x01(\x03R\x11\x65xpiryTimestampMs",\n\nListTimers\x12\x1e\n\niteratorId\x18\x01 \x01(\tR\niteratorId"(\n\x10ValueStateUpdate\x12\x14\n\x05value\x18\x01 \x01(\x0cR\x05value"\x07\n\x05\x43lear".\n\x0cListStateGet\x12\x1e\n\niteratorId\x18\x01 \x01(\tR\niteratorId"L\n\x0cListStatePut\x12\x14\n\x05value\x18\x01 \x03(\x0cR\x05value\x12&\n\x0e\x66\x65tchWithArrow\x18\x02 \x01(\x08R\x0e\x66\x65tchWithArrow"#\n\x0b\x41ppendValue\x12\x14\n\x05value\x18\x01 \x01(\x0cR\x05value"J\n\nAppendList\x12\x14\n\x05value\x18\x01 \x03(\x0cR\x05value\x12&\n\x0e\x66\x65tchWithArrow\x18\x02 \x01(\x08R\x0e\x66\x65tchWithArrow"$\n\x08GetValue\x12\x18\n\x07userKey\x18\x01 \x01(\x0cR\x07userKey"\'\n\x0b\x43ontainsKey\x12\x18\n\x07userKey\x18\x01 \x01(\x0cR\x07userKey"=\n\x0bUpdateValue\x12\x18\n\x07userKey\x18\x01 \x01(\x0cR\x07userKey\x12\x14\n\x05value\x18\x02 \x01(\x0cR\x05value"*\n\x08Iterator\x12\x1e\n\niteratorId\x18\x01 \x01(\tR\niteratorId"&\n\x04Keys\x12\x1e\n\niteratorId\x18\x01 \x01(\tR\niteratorId"(\n\x06Values\x12\x1e\n\niteratorId\x18\x01 \x01(\tR\niteratorId"%\n\tRemoveKey\x12\x18\n\x07userKey\x18\x01 \x01(\x0cR\x07userKey"c\n\x0eSetHandleState\x12Q\n\x05state\x18\x01 \x01(\x0e\x32;.org.apache.spark.sql.execution.streaming.state.HandleStateR\x05state"+\n\tTTLConfig\x12\x1e\n\ndurationMs\x18\x01 \x01(\x03R\ndurationMs*n\n\x0bHandleState\x12\x0c\n\x08PRE_INIT\x10\x00\x12\x0b\n\x07\x43REATED\x10\x01\x12\x0f\n\x0bINITIALIZED\x10\x02\x12\x12\n\x0e\x44\x41TA_PROCESSED\x10\x03\x12\x13\n\x0fTIMER_PROCESSED\x10\x04\x12\n\n\x06\x43LOSED\x10\x05\x62\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "pyspark.sql.streaming.proto.StateMessage_pb2", _globals
)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals["_HANDLESTATE"]._serialized_start = 7159
    _globals["_HANDLESTATE"]._serialized_end = 7269
    _globals["_STATEREQUEST"]._serialized_start = 112
    _globals["_STATEREQUEST"]._serialized_end = 756
    _globals["_STATERESPONSE"]._serialized_start = 758
    _globals["_STATERESPONSE"]._serialized_end = 863
    _globals["_STATERESPONSEWITHLONGTYPEVAL"]._serialized_start = 865
    _globals["_STATERESPONSEWITHLONGTYPEVAL"]._serialized_end = 985
    _globals["_STATERESPONSEWITHSTRINGTYPEVAL"]._serialized_start = 987
    _globals["_STATERESPONSEWITHSTRINGTYPEVAL"]._serialized_end = 1109
    _globals["_STATERESPONSEWITHLISTGET"]._serialized_start = 1112
    _globals["_STATERESPONSEWITHLISTGET"]._serialized_end = 1272
    _globals["_STATERESPONSEWITHMAPKEYSORVALUES"]._serialized_start = 1275
    _globals["_STATERESPONSEWITHMAPKEYSORVALUES"]._serialized_end = 1443
    _globals["_KEYANDVALUEPAIR"]._serialized_start = 1445
    _globals["_KEYANDVALUEPAIR"]._serialized_end = 1502
    _globals["_STATERESPONSEWITHMAPITERATOR"]._serialized_start = 1505
    _globals["_STATERESPONSEWITHMAPITERATOR"]._serialized_end = 1736
    _globals["_STATEFULPROCESSORCALL"]._serialized_start = 1739
    _globals["_STATEFULPROCESSORCALL"]._serialized_end = 2411
    _globals["_STATEVARIABLEREQUEST"]._serialized_start = 2414
    _globals["_STATEVARIABLEREQUEST"]._serialized_end = 2755
    _globals["_IMPLICITGROUPINGKEYREQUEST"]._serialized_start = 2758
    _globals["_IMPLICITGROUPINGKEYREQUEST"]._serialized_end = 3017
    _globals["_TIMERREQUEST"]._serialized_start = 3020
    _globals["_TIMERREQUEST"]._serialized_end = 3277
    _globals["_TIMERVALUEREQUEST"]._serialized_start = 3280
    _globals["_TIMERVALUEREQUEST"]._serialized_end = 3526
    _globals["_EXPIRYTIMERREQUEST"]._serialized_start = 3528
    _globals["_EXPIRYTIMERREQUEST"]._serialized_end = 3594
    _globals["_GETPROCESSINGTIME"]._serialized_start = 3596
    _globals["_GETPROCESSINGTIME"]._serialized_end = 3615
    _globals["_GETWATERMARK"]._serialized_start = 3617
    _globals["_GETWATERMARK"]._serialized_end = 3631
    _globals["_UTILSREQUEST"]._serialized_start = 3634
    _globals["_UTILSREQUEST"]._serialized_end = 3773
    _globals["_PARSESTRINGSCHEMA"]._serialized_start = 3775
    _globals["_PARSESTRINGSCHEMA"]._serialized_end = 3818
    _globals["_STATECALLCOMMAND"]._serialized_start = 3821
    _globals["_STATECALLCOMMAND"]._serialized_end = 4020
    _globals["_TIMERSTATECALLCOMMAND"]._serialized_start = 4023
    _globals["_TIMERSTATECALLCOMMAND"]._serialized_end = 4318
    _globals["_VALUESTATECALL"]._serialized_start = 4321
    _globals["_VALUESTATECALL"]._serialized_end = 4723
    _globals["_LISTSTATECALL"]._serialized_start = 4726
    _globals["_LISTSTATECALL"]._serialized_end = 5333
    _globals["_MAPSTATECALL"]._serialized_start = 5336
    _globals["_MAPSTATECALL"]._serialized_end = 6170
    _globals["_SETIMPLICITKEY"]._serialized_start = 6172
    _globals["_SETIMPLICITKEY"]._serialized_end = 6206
    _globals["_REMOVEIMPLICITKEY"]._serialized_start = 6208
    _globals["_REMOVEIMPLICITKEY"]._serialized_end = 6227
    _globals["_EXISTS"]._serialized_start = 6229
    _globals["_EXISTS"]._serialized_end = 6237
    _globals["_GET"]._serialized_start = 6239
    _globals["_GET"]._serialized_end = 6244
    _globals["_REGISTERTIMER"]._serialized_start = 6246
    _globals["_REGISTERTIMER"]._serialized_end = 6307
    _globals["_DELETETIMER"]._serialized_start = 6309
    _globals["_DELETETIMER"]._serialized_end = 6368
    _globals["_LISTTIMERS"]._serialized_start = 6370
    _globals["_LISTTIMERS"]._serialized_end = 6414
    _globals["_VALUESTATEUPDATE"]._serialized_start = 6416
    _globals["_VALUESTATEUPDATE"]._serialized_end = 6456
    _globals["_CLEAR"]._serialized_start = 6458
    _globals["_CLEAR"]._serialized_end = 6465
    _globals["_LISTSTATEGET"]._serialized_start = 6467
    _globals["_LISTSTATEGET"]._serialized_end = 6513
    _globals["_LISTSTATEPUT"]._serialized_start = 6515
    _globals["_LISTSTATEPUT"]._serialized_end = 6591
    _globals["_APPENDVALUE"]._serialized_start = 6593
    _globals["_APPENDVALUE"]._serialized_end = 6628
    _globals["_APPENDLIST"]._serialized_start = 6630
    _globals["_APPENDLIST"]._serialized_end = 6704
    _globals["_GETVALUE"]._serialized_start = 6706
    _globals["_GETVALUE"]._serialized_end = 6742
    _globals["_CONTAINSKEY"]._serialized_start = 6744
    _globals["_CONTAINSKEY"]._serialized_end = 6783
    _globals["_UPDATEVALUE"]._serialized_start = 6785
    _globals["_UPDATEVALUE"]._serialized_end = 6846
    _globals["_ITERATOR"]._serialized_start = 6848
    _globals["_ITERATOR"]._serialized_end = 6890
    _globals["_KEYS"]._serialized_start = 6892
    _globals["_KEYS"]._serialized_end = 6930
    _globals["_VALUES"]._serialized_start = 6932
    _globals["_VALUES"]._serialized_end = 6972
    _globals["_REMOVEKEY"]._serialized_start = 6974
    _globals["_REMOVEKEY"]._serialized_end = 7011
    _globals["_SETHANDLESTATE"]._serialized_start = 7013
    _globals["_SETHANDLESTATE"]._serialized_end = 7112
    _globals["_TTLCONFIG"]._serialized_start = 7114
    _globals["_TTLCONFIG"]._serialized_end = 7157
# @@protoc_insertion_point(module_scope)
