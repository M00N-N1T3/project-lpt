import subprocess
import os

# rewritng the parameter_generator.sh in python

# technically we still using bash but I am scriptinng it as a .py file for better compatibality

print(f"Printing cwd: {os.getcwd()}")
print("\nChanging current dir ...")
os.chdir('/tmp/test')
print(f"Printing cwd: {os.getcwd()}")

# listing the cwd
listing = subprocess.run(f"ls",shell=True,capture_output=True,text=True)
print(f"\nThings currenly here: \n{listing.stdout}")

# making the lpt folder
try:
    os.mkdir("/tmp/lpt")
except FileExistsError:
    pass


s = ["great-lowly-apple.txt","real-goofy-visit.txt","testy-far-sell.txt"] 
list_s = []
for name in s:
    print(name)
    list_s.append((f"sample-{name}").replace(".txt",""))
print(list_s)

s_count = 0
for names in list_s:
    print(s_count)
    print(names)
    with open(f".{names}.txt","w") as f:
        p1 = subprocess.run(f'(cat "{s[s_count]}" | grep -w "Submission" | cut -f3 -d " ")', shell = True, stdout = f,text=True)
        p2 = subprocess.run(f'(cat "{s[s_count]}" | grep -w "Module")',shell=True,stdout = f,text=True)
        p3 = subprocess.run(f'(cat "{s[s_count]}" | grep -w "Topic")',shell=True,stdout = f,text=True)
        p4 = subprocess.run(f'(cat "{s[s_count]}" | grep -w "Problem")',shell=True,stdout = f,text=True)
        p5 = subprocess.run(f'(cat "{s[s_count]}" | grep -w "add_comment" | cut -f3 -d " ")', shell = True, stdout = subprocess.PIPE,text=True)
        f.write(f"UUID: {p5.stdout}")
    s_count = s_count + 1
subprocess.run(f"mv .s* /tmp/lpt",shell = True)


# process = [p1,p2,p3,p4,p5]; index = 0
# for processes in process:
#     index  = index +1
#     print(f"Process number: P{index}")
#     print(f"Arguments: \n{processes.args} \nstdout: {processes.stdout} \nreturncode: {processes.returncode}")
#     print("\n\n")