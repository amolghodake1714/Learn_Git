import logging
import os
import json


lrt_device_info = {}
data_json = {}

from datetime import datetime
timestr=datetime.now().strftime("_%Y_%m_%d-%H_%M_%S")

with open("lrt_DEB-NUC10i5F-G6FN04300231"+timestr+".json", "w") as json_file:
#    logging.basicConfig(filename = "DEB-NUC10i5F-G6FN04300231"+timestr+".json" , filemode="w") 
    file=open("/opt/scorer/cache/device_id", "r")
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    data_json["device_id"] = file.read()
    data_json["device_id"] = data_json["device_id"].replace("\n"," ")
    json_file.write(str(data_json))


    file = os.popen("hostname -I | awk '{print $1 }' ")
    logger.setLevel(logging.DEBUG)
    data_json["device_ip"] = file.read()
    data_json["device_ip"]=data_json["device_ip"].replace("\n","")
    json_file.write(str(data_json))


    file=open("/opt/scorer/etc/docker-arch", "r")
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    data_json["architecture"] = file.read()
    data_json["architecture"] = data_json["architecture"].replace("\n","")
    arch_details = data_json["architecture"].split(" ")[0].split("DOCKER")[1]
    arch_details = arch_details.split("=")[1]
    data_json["architecture"] = arch_details
    json_file.write(str(data_json))


    file=open("/opt/scorer/etc/scorer-release", "r")
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    data_json["release_tag"] = file.read()
    data_json["release_tag"]=data_json["release_tag"].replace("\n","")
    data_json["release_tag"].split(" ")[1]
    json_file.write(str(data_json))



#Serializing json
json_object=json.dumps(data_json, indent=4)
# Writing to sample.json
with open("lrt_DEB-NUC10i5F-G6FN04300231"+timestr+".json", "w") as outfile:
     data = {"lrt_device_info": data_json} 
     outfile.write(str(data) + "\n")

