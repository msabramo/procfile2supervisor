procfile2supervisor
===================

Tiny utility to convert a Procfile to a supervisor config file.

Example usage
-------------

::

    [marca@marca-mac2 profilesvc]$ ls -l Procfile
    -rw-r--r--+ 1 marca  staff  59 Mar 11 16:40 Procfile

    [marca@marca-mac2 profilesvc]$ procfile2supervisor
    2015-03-11 16:41:24 [51434] [INFO] Writing './profilesvc.conf'

    [marca@marca-mac2 profilesvc]$ cat profilesvc.conf
    [program:profilesvc]
    command                  = gunicorn --bind 0.0.0.0:$PORT --paste development.ini
    user                     = profilesvcuser
    environment              = PORT=8000
    startsecs                = 30
    redirect_stderr          = true
    autorestart              = true
    stopwaitsecs             = 10
    directory                = /opt/webapp/%(program_name)s
    stdout_logfile           = /var/log/sm/%(program_name)s-app-out.log
    stdout_logfile_maxbytes  = 10MB
    stdout_logfile_backups   = 10
    stdout_capture_maxbytes  = 1MB
    stderr_logfile           = /var/log/sm/%(program_name)s-app-err.log
    stderr_logfile_maxbytes  = 10MB
    stderr_logfile_backups   = 10
    stderr_capture_maxbytes  = 1MB
