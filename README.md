# Automated Networking Logs

This project was created in order to help me keep track of system logs in my production enviroment, which for now consists of only one managed switch alongside a router/firewall device in a LAN/WLAN network, with the purpose of being able to scale this as my network grows.

The project will make use of various different components, the core of which are: SQL(mariadb-server), python, Cisco iOS, c++ and Rust.

## Network Topology Design

For this project the created architeture and topology were simlpe, as it only consisted of the Default VLAN (1) and two network devices, as no additional segmentation was required the topology consisted of only one subnet `192.168.1.0/24` in which i grouped the end devices to `192.168.1.1-252` and the network devices used `192.168.1.254` and `192.168.1.253` accordingly,the Network topology is described in the following figure:

![Network Topology](https://github.com/CrescentMnn/network_automation_logs/blob/master/misc/NetworkTopology.png)


## Database Design 

The following SQL schema was designed after the network topology:


![SQL Schema](https://github.com/CrescentMnn/network_automation_logs/blob/master/misc/drawSQL-image-export-2026-08-16.webp)


## Automation Scripts


## Examples of use

## Cheat Sheets

## References
