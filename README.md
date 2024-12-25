# ha_win_wkl
Home Assistant局域网唤醒电脑,目前仅支持开机
因无时间解决shh读取公钥的权限问题,暂时不支持关机功能,建议使用向日葵进行远程关机

**插件安装方法：**

手动下载自定义插件的代码，并将ha_win_wkl其解压缩到 Home Assistant 配置目录的 "custom_components" 文件夹中。请注意，如果 "custom_components" 文件夹不存在，则需要手动创建它。

![image](https://github.com/user-attachments/assets/a1254ac0-8dd9-41f8-9cab-2595827cd074)

如图

![image](https://github.com/user-attachments/assets/d8617e2b-7050-47f2-a418-c3467cb12f26)



例如，如果您要安装的插件名为 "ha_win_wkl"，则您应该将其解压缩到以下路径：/custom_components/ha_win_wkl/。
然后重新启动 Home Assistant，以使新插件加载和生效。
![image](https://github.com/user-attachments/assets/15b1c496-c342-40ad-a394-40ee5b7629f4)

接下来到Home Assistant的web界面，设置-设备与服务中去添加集成
![image](https://github.com/user-attachments/assets/82857d83-71d1-4032-93d7-4de227ef0fe1)
![image](https://github.com/user-attachments/assets/d5796289-e382-4988-aeed-141f5de6751f)



在弹出窗口中选择您要安装的插件，并按照提示进行设置既可。
![image](https://github.com/user-attachments/assets/40809d2b-f68b-4edd-bc0a-45624ad8f02d)
![image](https://github.com/user-attachments/assets/57f16e38-8d76-496d-b7cd-d8d4dbf70b75)

这样就可以在概览中看到电脑状态了
![image](https://github.com/user-attachments/assets/b56d667d-f590-4a8d-90ec-2c75ce4569a9)
