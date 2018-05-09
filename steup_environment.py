import os


print("**********************************************************************************")
print("*********************** Running Setup Environment Script *************************")
print("**********************************************************************************")

try:
    from pathlib import Path
except:
    os.system("pip install pathlib")
    os.system("pip3 install pathlib")

# update packages
os.system('apt-get update')

failed = False
# install python dependencies
os.system('apt-get install -y swig')
os.system('apt-get install -y python3-pip python3-dev python-pip python-numpy python-dev')
os.system('pip install wheel')

os.system('apt-get install -y python-pip python-dev python3-pip python3-numpy python3-dev')
os.system('pip3 install wheel')


# other dependencies
os.system("apt-get install -y automake autoconf curl libtool libpng12-dev zlib1g-dev git wget xz-utils")

# install bazel dependencies
os.system('apt-get install -y pkg-config zip g++ zlib1g-dev unzip openjdk-8-jdk')
os.system('update-alternatives --config java')

# install tensorflow dependencies
os.system('apt-get install -y gcc-4.8 g++-4.8')
os.system('update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc 100')
os.system('update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++ 100')


print("**********************************************************************************")
print("*********************** Completed Setup Environment Script ***********************")
print("**********************************************************************************")