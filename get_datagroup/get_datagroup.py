from netmiko.ssh_autodetect import SSHDetect
from netmiko.ssh_dispatcher import ConnectHandler

remote_device = {'device_type': 'f5_ltm',
                 'host': '172.31.200.211',
                 'username': 'ansible-user',
                 'password': 'ansible'}

#guesser = SSHDetect(**remote_device)
#best_match = guesser.autodetect()

#print("device_type: " + best_match)

#remote_device['device_type'] = best_match
connection = ConnectHandler(**remote_device)

file = open('/root/venv/egw-bigip/file/config.scf', 'w')
string = connection.send_command('show running-config ltm data-group')
file.write(string)

connection.disconnect()
