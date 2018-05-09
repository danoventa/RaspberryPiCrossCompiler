import os

print("**********************************************************************************")
print("*********************** Running Build Tensorflow Script **************************")
print("**********************************************************************************")

# clean bazel cache
os.system('bazel clean --expunge')

# compile tensorflow
os.system('git clone --recurse-submodules https://github.com/danoventa/tensorflow.git')
os.chdir('./tensorflow')
os.system('git checkout origin/d1.3')

# updates libraries for 32 bit systems
os.system("grep -Rl 'lib64' | xargs sed -i 's/lib64/lib/g'")
os.system("./configure")

os.system('touch WORKSPACE')

# this is for pi3 (pi zero needs v6a?)
os.system('bazel build --crosstool_top="//arm-unknown-linux-gnueabi-gcc:toolchain" --cpu=armeabi-v7a -c opt --copt="-mfpu=neon-vfpv4" --copt="-funsafe-math-optimizations" --copt="-ftree-vectorize" --copt="-fomit-frame-pointer" --local_resources 1024,2.0,1.0 --verbose_failures tensorflow/tools/pip_package:build_pip_package')
os.system('bazel-bin/tensorflow/tools/pip_package/build_pip_package /tmp/tensorflow_pkg')

print("**********************************************************************************")
print("********************** Completed Build Tensorflow Script *************************")
print("**********************************************************************************")