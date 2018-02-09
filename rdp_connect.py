## 將要執行遠端桌面的主機，以及相關參數列在下方二維陣列中
## 一維陣列參數為 ["子網域", "ip起點", "ip終點" ,"帳號" ,"密碼"] 

import os 

host_array = [
    ["subnet.", 222 , 222, "admin", "1234"],
    ["subnet2.", 111 , 111, "admin", "1234"]
]

command = ""

for i in range (0, len(host_array),1): # 取得第一個參數 subnet
    for ip in range(host_array[i][1], host_array[i][2]+1,1): # 組出 指令
        command = "xfreerdp " + "-u " + host_array[i][3] + " -p " + host_array[i][4] + " --ignore-certificate " + " " +  host_array[i][0]  + str(ip) + " &" 
        print(command)
        #os.system(command) #執行系統命令
