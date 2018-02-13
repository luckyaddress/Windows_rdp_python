
import os, subnet_ip_data # 將陣列資料，存在subnet_ip_data中

content = subnet_ip_data.host_array # 將陣列資料，指定給一個變數，便於使用

command = ""  # 設定一個全域變數，儲存後續執行的系統指令

for i in range (0, len(content),1): # 取得第一個參數 subnet
    for ip in range(content[i][1], content[i][2]+1,1): # 組出 指令
        command = "xfreerdp " + "-u " + content[i][3] + " -p " + content[i][4] + " --ignore-certificate " + " " +  content[i][0]  + str(ip) + " &" 
        print(command)
        #os.system(command) #執行系統命令
        