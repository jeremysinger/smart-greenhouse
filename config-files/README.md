
# data collection
The cron file controls the data collection service, which runs every couple
of minutes or so. Edit your crontab file with `crontab -e`

# sensor service
The Flask web application runs as a systemd service. The service file must
be installed in /etc/systemd/system/
and it can be enabled for running at boot time with a command like
`sudo systemctl enable lionsgate-sensor`


