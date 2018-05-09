import os
from pathlib import Path


print("**********************************************************************************")
print("************************* Running Setup Bazel Script *****************************")
print("**********************************************************************************")

failed = False
try:
    os.system('mkdir tf')
    os.chdir('./tf')
    os.system('ls')

    # install bazel
    bazel = Path("./bazel-0.13.0-dist.zip)")
    if bazel.is_file() == False:
        os.system('wget https://github.com/bazelbuild/bazel/releases/download/0.13.0/bazel-0.13.0-dist.zip')
        os.system('unzip -d bazel bazel-0.13.0-dist.zip')

    bazel_dir = Path("./bazel")
    if bazel_dir.is_dir():
        os.chdir('./bazel')
        os.system('ls')
        os.system('./compile.sh')
    else:
        failed = True

    os.chdir('..')



    # cleanup if fails
except:
    failed = True

if failed:
    os.system("rm -r tf")
    os.system("rm dep.py")

print("**********************************************************************************")
print("************************* Completed Setup Bazel Script ***************************")
print("**********************************************************************************")
