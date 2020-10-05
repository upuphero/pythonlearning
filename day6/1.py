#首先我们先导入requests这个包
import requests

#我们来吧百度的index页面的html源码抓取到本地，并用r变量保存
#注意这里，网页前面的 http://一定要写出来，它并不能像真正的浏览器一样帮我们补全http协议
r = requests.get("https://projects.eng.gla.ac.uk/uestc/")


#将下载到的内容打印一下：
print(r.text)