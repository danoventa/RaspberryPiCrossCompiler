import os
from pathlib import Path

print("**********************************************************************************")
print("*********************** Running Setup Cross Tools Script *************************")
print("**********************************************************************************")

# download crosstool
if not Path("./crosstool-ng-1.23.0.tar.xz").is_file():
    os.system("wget http://crosstool-ng.org/download/crosstool-ng/crosstool-ng-1.23.0.tar.xz")
os.system("tar -xvf crosstool-ng-1.23.0.tar.xz")

os.chdir("./crosstool-ng-1.23.0")
os.system("./configure --prefix=/opt/cross")
os.system("make")
os.system("make install")

os.system("export PATH=$PATH:/opt/cross/bin")

# make dir for toolchain
bazel_dir = Path("/root/crosstools")
if not bazel_dir.is_dir():
    os.system("mkdir /root/crosstools")

os.chdir("/root/crosstools")

# you'll be taken through a journey of settings, follow url for details
# https://www.bootc.net/archives/2012/05/26/how-to-build-a-cross-compiler-for-your-raspberry-pi/
os.system("ct-ng menuconfig")
os.system("ct-ng build")

# This assumes you followed the above url instructions, else you're gonna have to change it.
os.system("export PATH=$PATH:/opt/cross/x-tools/arm-unknown-linux-gnueabi/bin")

print("**********************************************************************************")
print("********************** Completed Setup Cross Tools Script ************************")
print("**********************************************************************************")