import mariadb
from netmiko import ConnectHandler

#connect db
db_config = {
        'host': 'localhost',
        'port': 3306,
        'user': 'your_username',
        'password': 'your password',
        'database': 'automated_network_config'
}

cisco_2900 = {
    'device_type' = 'cisco_ios'
    'host' = '192.168.1.253'
    'username' = 'admin'
    'password' = 'password'
    'port' = '8022'
    'secret' = 'cisco'
}

net_connect = ConnectHandler(**cisco_2900)

int_brief_output = net_connect.send_command('show interfaces brief')


