# -*- coding: UTF-8 -*-

from httplib2 import Http
from json import dumps
import sys


def service_alerte(**kwargs):
    """
    notyficationtype, host,  service, ip, state, serviceoutput, date
    :return:
    """
    url = "put your webhooksurl"
    msg = "Notification Type: *{}* \n service: *{}* \n host: *{}* \n ip: {} \n State: *{}* \n \n date: {}" \
          "Additional Info: {}".format(kwargs['notyf'], kwargs['service'], kwargs['host'], kwargs['ip'],
                                       kwargs['state'], kwargs['date'], kwargs['serviceoutput'])

    bot_message = {
        'text': msg
    }
    try:
        message_headers = {'Content-Type': 'application/json; charset=UTF-8'}
        http_obj = Http()
        response = http_obj.request(
            uri=url,
            method='POST',
            headers=message_headers,
            body=dumps(bot_message),
        )
        print(response)
    except Exception as e:
        raise ValueError(e)


if __name__ == "__main__":

    notif = (sys.argv[1])
    host = (sys.argv[2])
    service = (sys.argv[3])
    ip = (sys.argv[4])
    state = (sys.argv[5])
    serviceoutput = (sys.argv[6])
    date = (sys.argv[7])

    service_alerte(notyf=notif, host=host, service=service, ip=ip, state=state, serviceoutput=serviceoutput, date=date)
