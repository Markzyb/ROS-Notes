# ROS-Notes
study notes of ROS



day1

## markdown用法
基本语法
* #第一个标题
* ##第二个标题
* 超链接
* [Markdown](//www.markdown.cn/)



##ros基础
运行话题
roscore
rosrun

rostopic list 显示正在执行的话题

rostopic info 显示订阅者和发布者

rostopic echo 显示话题消息

rosfind 寻找特定话题种类的话题

rospub 虚拟实例下指令
rostopic pub /turtle1/cmd_vel geometry_msgs/Twist "linear:
  x: 100.0
  y: 100.0
  z: 0.0
angular:
  x: 10.0
  y: 10.0
  z: 00.0" 


ros机器人实际常用指令

启动底盘：
roslaunch mx_bringup rbc_mini_start.launch 

下指令：rostopic pub /cmd_vel geometry_msgs/Twist "linear:
  x: 100.0
  y: 100.0
  z: 0.0
angular:
  x: 10.0
  y: 10.0
  z: 00.0" 



##linux base

# ls指令：查看文件列表
默认路径：HOME （files）
和computer中的home不同。home为linux的一个文件夹
但intel中的home和files的HOME相同，因为登录的帐号为intel



# cd指令：进入目录
进入用户目录
cd /home/intel/

回到桌面：
cd Desktop/

返回上一级目录：
cd ..

从某目录直接跳到另一个目录：
ex：跳到demo
 cd /home/intel/Desktop/Demo


#tab用法：输入文件第一个字母，然后按tab
ex：
cd r，按tab
出现全称



#进入用户目录快捷方法
cd ～
直接输入cd

从某文件夹返回用户目录快捷方法再进入别的文件夹

 cd ~/Pictures/



#mkdir指令： 创建目录

mkdir 目录名

#mkdir-p Desktop/Demo 嵌套

 mkdir 1 2 3 4 5 一次性创建多个目录


#touch指令 创建文件 
 touch 1 2 3 4 5 

#gedit指令 编辑文件

gedit 1/


#man指令： 查看指令的手册

man mkdir


#git

git status 查看仓库文件

如有未跟踪文件

git add





git commit -am "hejwj"

get push





