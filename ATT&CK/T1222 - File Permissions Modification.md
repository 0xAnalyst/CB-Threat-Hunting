# Query 
(process_name:takeown.exe OR process_name:icacls.exe OR process_name:cacls.exe or process_name:attrib.exe) and -parent_name:iwrap.exe AND -cmdline:Adobe*
# Might be noisy and you need to customize for your enviroment
