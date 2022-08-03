## Set Docker Resource in GNS3
Set CPU and Memory Resource for Docker Containers running on GNS3

![GitHub Workflow Status](https://img.shields.io/github/workflow/status/emylincon/gns3_docker_resource/python?style=for-the-badge)

## To Use
* Modify the below as necessary
```python
self.url = "http://192.168.157.128:5555"
self.ip = "192.168.157.128"
self.username = "gns3"
self.password = "gns3"
```

* To run
```python
Gns3Container().set_resource(image_name='ugwuanyi/mec_open:latest', cpu=0.5, mem='4m')
```
* The above will limit the container to `4 megabytes` of memory & `0.5` of avaliable CPU ([see docs](https://docs.docker.com/config/containers/resource_constraints/#cpu)).
