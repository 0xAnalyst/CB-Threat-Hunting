# Query 1
regmod:debugger AND -cmdline:GPSvcGroup AND -cmdline:netsvcs AND -path:common7\ide\*  AND -path:app\servicehub\* AND -path:binn\managementstudio\*
# Query 2
process_name:gflags.exe OR regmod:MonitorProcess
