# Health_Clock_in
简单，机械而重复的事情，不应该由人类去完成。<br>
每天的健康打卡就是非常无聊的事，还在群里面被催打卡。<br>
刚好有台装着ubuntu 20.04 LTS的服务器24小时不关机，让它每天帮我打卡就好了。
# Description
Gzhu的健康打卡页面直接浏览器就可以打开，不一定要从企业微信进入。<br>
既然能用浏览器打开了，那就用selenium把打卡这事给做了吧。<br>
还有验证码识别这一块，直接套用了pytesseract这个库，先把验证码的图片下载到本地储存，然后用这个库识别验证码。当然我也考虑到可能识别不准，所以我写了一个错误判断的循环，如果没有识别出来那就继续执行识别验证码和登录的操作。<br>
我使用的是系统自带的Firefox浏览器，当然chrome也可以，改一下代码就好。
# Usage
我的系统是Ubuntu 20.04 LTS 带desktop, 其他Linux系统应该也能用，要改代码做适配。<br>
windows装好环境也应该可以用，但是windows电脑24小时不关机真的好吗()<br>
## 环境安装
Python3, pip, selenium, pyautogui, pytesseract, PIL等库都要安装好。我懒得写了，上网查。有些前置需要apt get install，有些pypi的包直接pip install就好。
## 修改代码
10行：`driver = webdriver.Firefox()`<br>
如果是Chrome的话改：`driver = webdriver.Chrome()`<br>
31行：`img = Image.open("../Downloads/captcha.jsp.png")`<br>
路径是相对路径，保存验证码的图片，浏览器默认下载到`/home/user/Downloads`这个文件夹，看着改就好。<br>
36行和38行是账户和密码，写自己的校园学号和密码。<br>
完事后`python3 health_clock_in.py`试试能不能正常运行，不能正常运行就一直debug到能运行为止，前置环境安装有点繁琐，像selenium还要装浏览器的插件什么的。<br>
能正常运行就下一步，添加进自动执行计划。
## crontab
```
sudo service cron start
sudo crontab -e
```
用vim编辑一下，添加执行命令
```
0 7 * * * python3 /home/user/.../health_clock_in.py
```
0代表分，7代表时，意思是每天7点执行一次这个程序进行打卡。<br>
重启crontab：
```
sudo service cron restart
```
# Addition
可以参考下，有用就自己用。<br>
请不要拿来赚钱，也不要传出去，我不打算被太多人知道。万一哪天赵弹打我头上。
