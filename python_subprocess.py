import subprocess #สำหรับรัน terminal command

if __name__ == "__main__":
    #basic terminal command
    print(f'first run num=100 xx=90')
    subprocess.run(["python", "firstpy.py", "--num", "100", "--xx", "90"])
    print(f'-------------------------------------------------------------')
    print(f'second run num=-10 xx=-90')
    subprocess.run(["python", "firstpy.py", "--num", "-10", "--xx", "-90"])
    print(f'-------------------------------------------------------------')
    print(f'third run num=0')
    subprocess.run(["python", "firstpy.py", "--num", "0"])
    print(f'-------------------------------------------------------------')
