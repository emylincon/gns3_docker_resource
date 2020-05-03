import docker
import paramiko
import time


class Gns3Container:
    def __init__(self):
        self.url = "http://192.168.157.128:5555"
        self.ip = "192.168.157.128"
        self.username = "gns3"
        self.password = "gns3"

    @staticmethod
    def format_data(msg):
        out = ''
        for i in msg:
            out += i
        return out

    def send_command(self, cmd):
        c = paramiko.SSHClient()

        c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        c.connect(self.ip, 22, self.username, self.password)
        # cmd = "curl http://localhost:5555/images/json"

        stdin, stdout, stderr = c.exec_command(cmd)
        return {'stdout': self.format_data(stdout), 'stderr': self.format_data(stderr)}

    def set_resource(self, con_name=None, image_name=None, cpu=0, mem=0):
        client = docker.DockerClient(base_url=self.url)
        data = client.containers.list()
        log = []
        # docker inspect e6d1 | grep -e NanoCpus -e '"Memory":'
        for con in data:
            if con.attrs['Config']['Image'] == image_name:
                con_id = con.attrs['Id']
                cmd = f'docker update --cpus="{cpu}" --memory="{mem}" {con_id}'
                log.append(con_id)
                self.send_command(cmd)
        time.sleep(1)
        for _id in log:
            inspect = f"docker inspect {_id} | grep -e NanoCpus -e '" + '"Memory":' + "'"
            print(f"{_id} => {self.send_command(inspect)}")


# Gns3Container().set_resource(image_name='ugwuanyi/mec_open:latest', cpu=0.5, mem='4m')
