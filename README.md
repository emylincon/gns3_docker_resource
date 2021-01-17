## Set Docker Resource in GNS3
Set CPU and Memory Resource for Docker Containers running on GNS3

![](https://github.com/emylincon/gns3_docker_resource/workflows/myaction/badge.svg)

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