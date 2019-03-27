import sys
from datetime import datetime, timedelta
from cbapi.response.models import Process, Binary, Sensor, Feed, Watchlist, Investigation
from cbapi.response.rest_api import CbEnterpriseResponseAPI
from cbapi.errors import ObjectNotFoundError
cb=CbEnterpriseResponseAPI()
d = datetime.now() - timedelta(days=1)
opts = d.strftime("%Y-%m-%d")
#process_name:net.exe and cmdline:add*
#process_name:reg.exe and (cmdline:save* or cmdline:export*) 
query = "(parent_name:pcalua.exe or parent_name:forfiles.exe) and -cmdline:logs* -cmdline:del last_update:[" + opts + "T00:00:00 TO *]"
for proc in cb.select(Process).where(query):
    print("%s,%s,%s" % (proc.hostname, proc.username, proc.cmdline))
