import subprocess #สำหรับรัน terminal command

if __name__ == "__main__":
    #basic terminal command
    subprocess.run(["python", "firstpy.py", "--num", "100", "--xx", "90"])
    subprocess.run([print(f'--------------------------------------------')])
    subprocess.run(["python", "firstpy.py", "--num", "-10", "--xx", "-90"])
    subprocess.run([print(f'--------------------------------------------')])
    subprocess.run(["python", "firstpy.py", "--num", "0"])
    subprocess.run([print(f'--------------------------------------------')])
