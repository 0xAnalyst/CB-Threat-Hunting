(((process_name:schtasks.exe and cmdline:/create) or (process_name:at.exe) or (process_name:wmic.exe  and (cmdline:job or cmdline:create))) and -cmdline:WSqmUploaderTask.xml* -cmdline:ClickToRun* and  -parent_name:supportassistagent.exe -cmdline:Heartbeat* -cmdline:OfficeTelemetry* -cmdline:Lenovo*)

Would generate false positives exclude with -cmdline
