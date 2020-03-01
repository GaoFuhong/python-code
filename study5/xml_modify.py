# Author:Fuhong Gao
import xml.etree.ElementTree as ET
tree = ET.parse("xmltest.xml")
root = tree.getroot()

#修改xmltest.xml中的year
'''
for node in root.iter("year"): #找到year标签
    new_year = int(node.text) + 1 #将year中的字符串转换成int型
    node.text = str(new_year) #重新赋值
    node.set("update_by","GFH") #增加属性
tree.write("xmltest.xml") #重新写回原文件
'''

#删除
for country in root.findall("country"): #找到所有的country
    rank = int(country.find("rank").text) #找到每个country的rank并赋值
    if rank > 50:
        root.remove(country) #删除
tree.write("output.xml") #将删除后的内容写到新的文件
