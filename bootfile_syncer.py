import paramiko
import shlex
import time

hostname = '10.68.3.75'
username = "kipr"
password = 'botball'

local_file = './sync_files/control.py'
remote_file = '/home/kipr/control.py'

last_stamp = ""
print("Start listening..")
while True:
    time.sleep(0.5)
    for i in range(3):
        try:
            file_data = open(local_file).read()
            break
        except Exception:
            file_data = last_stamp
    
    if last_stamp != file_data:
        last_stamp = file_data

        client = paramiko.SSHClient()

        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            client.connect(hostname, username=username, password=password)
        
            with open(local_file, 'r') as file:
                file_content = file.read()

            escaped_content = shlex.quote(file_content)

            command = f'echo {escaped_content} > {remote_file}'

            stdin, stdout, stderr = client.exec_command(command)

        except Exception as e:
            print(f"Critical Error: {e}")

        finally:
            client.close()
