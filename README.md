# Processing-alarm-data-opc-ua-server

Steps to be taken to process alarm data:
(Refer to ticket 785 about where and how alarm files got updated and stored)

1. reads AlarmMessageLog files at a predefined interval
2. checks if the file content changed after the last read
   if contents changed -> continue process
   if contents did not change -> exit process
3. uses a queue mechanism to process the logs
4. publishes alarm messages from the queue to an opcua server based on first in first out principle

Refer to https://github.com/NationalOilwellVarco/oss-opc-ua-mock-server/tree/main for opcuaserver connection







