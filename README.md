# Sending notifications status using webhooks google


* requirements python 2.7

![#f03c15](https://placehold.it/15/f03c15/000000?text=+) **before using this scripts please change url webkooks line 13**


## Declare host notify in centreon:
**host-notify-by-bot**

/usr/bin/python /usr/lib64/nagios/plugins/notify_webhooks_for_host.py "$NOTIFICATIONTYPE$" "$HOSTNAME$" "$SERVICEDESC$" "$HOSTADDRESS$" "$SERVICESTATE$" "$SERVICEOUTPUT$" "$LONGDATETIME$"


## Declare service notify in centreon:
**service-notify-by-bot**

/usr/bin/python /usr/lib64/nagios/plugins/notify_webhooks_for_service.py "$NOTIFICATIONTYPE$" "$HOSTNAME$" "$SERVICEDESC$" "$HOSTADDRESS$" "$SERVICESTATE$" "$SERVICEOUTPUT$" "$LONGDATETIME$"

