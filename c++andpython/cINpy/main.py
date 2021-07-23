import subprocess  
import os  
main = "./main"  
if os.path.exists(main):  
    rc, out = subprocess.getstatusoutput(main)  
    print('rc = %d, out = %s' % (rc, out))
  
f = os.popen(main)    
data = f.readlines()    
f.close()    
print(data)
  
os.system(main)