'''
Copyright 2015 Satish Palaniappan

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, 
software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
See the License for the specific language governing permissions and limitations under the License.
'''
__author__ = "Satish Palaniappan"

import os
import os.path
import zipfile
import shutil
from subprocess import Popen
import subprocess
import time

print("APK Decoder:")
print("-by $@T!$#")

print("Decoding")

apk="share.apk"
shutil.copy(apk,"temp.apk")
#copy and rename .zip apk
os.makedirs("Decoded_APK")
shutil.copy(apk,"Decoded_APK/share.apk.zip")
my_zip="Decoded_APK/"+str(apk)+".zip"
my_unziped="Decoded_APK"

print("Unzipping .......................")

#Unziping apk
zip = zipfile.ZipFile(my_zip)
zip.extractall(my_unziped)
zip.close()


#Unzipping dex2jar
zip = zipfile.ZipFile("dex2jar.zip")
zip.extractall(my_unziped)
zip.close()

shutil.copy("jd-gui.exe","Decoded_APK/jd-gui.exe")

print("Parsing data ..................")

#executing dex2jar and del
p = Popen("dex2jar.bat")
stdout, stderr = p.communicate()

p = Popen("jd.bat")
stdout, stderr = p.communicate()


#Unzipping jar classes
zip = zipfile.ZipFile("Decoded_APK/classes_dex2jar.src.zip")
zip.extractall(my_unziped)
zip.close()

#deleting unwanted files
zip = zipfile.ZipFile("dex2jar.zip")
for name in zip.namelist():
    try:
        filename = os.path.basename(name)
        # skip directories
        if not filename:
            shutil.rmtree("Decoded_APK/"+name)
            continue
        os.remove("Decoded_APK/"+name)
    except Exception:
        continue

os.remove("Decoded_APK/classes_dex2jar.jar")
os.remove("Decoded_APK/classes_dex2jar.src.zip")
os.remove("Decoded_APK/jd-gui.exe")

os.makedirs("temp")
shutil.copy("temp.apk","temp/temp.apk")
#Unziping apk tool
zip = zipfile.ZipFile("apktool.zip")
zip.extractall("temp")
zip.close()
shutil.copy("framework-res.apk","temp/framework-res.apk")

#framework-res
p = Popen("apktool.bat")
stdout, stderr = p.communicate()

p = Popen("xml.bat")
stdout, stderr = p.communicate()

#removing unwawnted
os.remove("temp.apk")
os.remove("temp/temp.apk")

zip = zipfile.ZipFile("apktool.zip")
for name in zip.namelist():
    os.remove("temp/"+name)
os.remove("temp/framework-res.apk")

p = Popen("final.bat")
stdout, stderr = p.communicate()

os.rmdir("temp")

print("Decoding completed: enjoy !!! the source code")

print("$@T!$#")

print("Find ur source code in Decoded_APK folder.")
print("Cut it to a diferent location")

print("!! $@T!$# !!")

time.sleep(10)
