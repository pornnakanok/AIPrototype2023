import subprocess #สำหรับรัน terminal command

if __name__ == "__main__":
    #basic terminal command
    subprocess.run(["ls", "-ltr"])
    subprocess.run(["rm", "-r", "/home/yoke/testfolder1"])
    subprocess.run(["python", "firstpy.py" "--num", "66", "--xx", "90"])
    subprocess.run(["python", "firstpy.py" "--num", "10", "--xx", "50"])
    subprocess.run(["python", "firstpy.py" "--num", "10"])
