import mariadb
import secrets.py
from netmiko import ConnectHandler

#connect db
connector = mariadb.connect{
        'host': secrets.database_host,
        'port': secrets.database_port,
        'user': secrets.database_user,
        'password': secrets.database_password,
        'database': 'automated_network_config'
}

# create cursor
cursor = connector.cursor()
#cursor.execute("query")
#connector.commit()
#cursor.close()
#connector.close()

cisco_2900 = {
    'device_type' = 'cisco_ios'
    'host' = secrets.cisco_ip
    'username' = secrets.cisco_user
    'password' = secrets.cisco_password
    'port' = secrets.cisco_port
    'secret' = secrets.cisco_secret
}

#DEVICE INFORMATION ***** STATIC FOR NOW FOR ALL DEVICES RUNNING SCRIPT DIFFERENT VALUES
cursor.execute("INSERT INTO source_device (vendor_name, device_name, device_ip) VALUES (?,?,?)", ("ASUS","crescent","192.168.1.2"))

#NETWORK DEVICE INFORMATION ***** STATIC ALWAYS
cursor.execute("INSERT INTO network_device (vendor_name, device_layer, device_ip) VALUES (?,?,?)", ("CISCO","2","192.168.1.253"))

##CREATE CONNECTION

net_connect = ConnectHandler(**cisco_2900)

int_status_command = net_connect.send_command('show int stat')
#print(int_status_command)
cusror.execute("INSERT INTO instance (source_id, net_device_id, command, output_text) VALUES (?,?,?,?)", ())
