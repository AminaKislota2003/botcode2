import configparser

config = configparser.ConfigParser()

config['program:curator7-project'] = {
    'command': 'python3/home/curatorN/curator7-project/main.py',
    'autostart': 'true',
    'autorestart': 'true',
    'stderr_logfile': '/home/curator7/curator7-project/test.err.log',
    'stdout_logfile': '/home/curator7/curator7-project/test.out.log'
}

with open('curator7-bbotcode.conf', 'w') as configfile:
    config.write(configfile)
