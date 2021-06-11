# T1016 - Atomic Test #1 - System Network Configuration Discovery on Windows
## Search Query 
`cmdline:"ipconfig /all" OR (cmdline:"netsh" and cmdline:"show interface") OR (cmdline:"arp -a") OR (cmdline:nbtstat -n") OR (cmdline:"net config")`

# T1016 - Atomic Test #2 - List Windows Firewall Rules
## Search Query 
`cmdline:"netsh" AND (cmdline:"advfirewall" OR cmdline:"show rule" OR cmdline:"name=all")


# T1016 - Atomic Test #4 - System Network Configuration Discovery (TrickBot Style)
## Search Query 
cmdline:"net config workstation" OR (cmdline:"net view" and cmdline:"/all /domain") OR (cmdline:"nltest" AND cmdline:"domain_trusts")
