from clickhouse_driver import Client
import time
from datetime import datetime

client = Client(host='localhost')
dbs = client.execute('SHOW DATABASES')

print(dbs)

for itr in dbs :

    if itr[0] !='INFORMATION_SCHEMA' and itr[0] != 'information_schema' and itr[0] != 'system' and itr[0]!= 'default' :
        print(itr)

        cmd1 = 'SHOW TABLES FROM ' + itr[0]

        res_cmd1 = client.execute(cmd1)

        print(res_cmd1)

        # Disk -- is the only correct form to mention according to clickhouse-documentation. DISK /disk doesn't work

        now = datetime.now()

        backup_name = 'script_backup ' + itr[0] + ':' + now.strftime("%d.%m.%YT%H.%M.%S")
        backup_cmd1 = 'BACKUP DATABASE ' + itr[0] + " TO Disk('backups','" + backup_name + "')"

        begin = time.time()
        print(client.execute(backup_cmd1))
        end = time.time()

        # total time taken
        print(f"Total runtime of the program is {end - begin}")