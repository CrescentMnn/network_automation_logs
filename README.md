# Automated Networking Logs

This project was created in order to help me keep track of system logs in my production enviroment, which for now consists of only one managed switch alongside a router/firewall device in a LAN/WLAN network, with the purpose of being able to scale this as my network grows.

The project will make use of various different components, the core of which are: SQL(mariadb-server), python, Cisco iOS, c++ and Rust.

## Network Topology Design

For this project the created architeture and topology were simlpe, as it only consisted of the Default VLAN (VLAN 1) and two network devices, as no additional segmentation was required the topology consisted of only one subnet `192.168.1.0/24` in which i grouped the end devices to `192.168.1.1-192.168.1.252` and the network devices used `192.168.1.254` and `192.168.1.253` accordingly,the Network topology is described in the following figure:

![Network Topology](https://github.com/CrescentMnn/network_automation_logs/blob/master/misc/NetworkTopology.png)


## Database Design 

To ensure scalability and maintain industry-standard network logging practices, the database schema is normalized into three primary tables: *source_device*, *network_device*, and *instance*. The *source_device* table identifies the origin of a request, generating a unique integer ID alongside the manufacturer, device name, and its statically assigned IP address, formatted as comma-separated values (for example, '00001,hp,laptop,192.168.1.1'). Similarly, the *network_device* table catalogs the target infrastructure by assigning a unique ID, vendor, device layer, and the static interface IP address to which the source connected. While IP addresses are currently statically assigned within this topology, future production environments (Version 2) will implement a DHCP-like state to dynamically track and update IP leases. Finally, the *instance* table serves as the primary transaction log, capturing each executed query by linking the foreign keys (source_id and net_device_id) to a unique instance_id. This table records a standard timestamp, the user's text command, the command output, and importantly, the specific firmware version of the network device at the time of execution. Capturing the firmware version directly within the instance log is a deliberate architectural decision for historical auditing; it ensures administrators can accurately track and reconstruct exactly what software environment was running when a specific command was issued, even after the devices undergo future firmware upgrades

![SQL Schema](https://github.com/CrescentMnn/network_automation_logs/blob/master/misc/drawSQL-image-export-2026-08-16.webp)

## Database User Configuration

A dedicated MariaDB user was created for the application rather than using the `root` account, following the principle of least privilege. The user was created scoped to `localhost` (`CREATE USER 'user'@'localhost' IDENTIFIED BY 'password';`), since the database and the connecting application currently run on the same host. Privileges were granted specifically on the `automated_network_config` database (`GRANT SELECT, INSERT, UPDATE ON automated_network_config.* TO 'user'@'localhost';`) rather than granting global access, and `FLUSH PRIVILEGES;` was run to apply the change immediately. The user was intentionally not granted `DELETE` or `DROP` privileges, as the automation script only needs to read and log data, not remove tables or records — restricting permissions to the minimum required reduces the impact of any potential bug or credential leak in the application layer.


## Automation Scripts


## Examples of use

## Cheat Sheets

## References
