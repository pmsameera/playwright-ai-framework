def countLogs(file):

#Application log file has the below content
#2026-07-14 10:01:12 DEBUG Application started
#2026-07-14 10:01:15 DEBUG Loading configuration
#2026-07-14 10:01:20 ERROR Database connection failed
#2026-07-14 10:01:25 INFO User logged in
#2026-07-14 10:01:30 WARN Disk space low
#2026-07-14 10:01:35 ERROR Timeout occurred
#2026-07-14 10:01:40 INFO Application stopped

    count_Logs = {}
    with open(file, 'r') as f:
       for line in f:
           loglevel = line.split(' ')
           count_Logs[loglevel[2]]= count_Logs.get(loglevel[2], 0) + 1
    return count_Logs
print(countLogs("application.log"))