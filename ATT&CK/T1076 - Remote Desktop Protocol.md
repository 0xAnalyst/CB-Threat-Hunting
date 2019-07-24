process_name:svchost.exe AND ipaddr:127.0.0.1/24 AND (cmdline:term* or ipport:3389)

Has false positives but helps in detecting SSH tunneling
