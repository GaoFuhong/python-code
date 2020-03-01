# Author:Fuhong Gao
import xml.etree.ElementTree as ET
tree = ET.parse("xmltest.xml") #要处理的xml程序
root = tree.getroot()
print(root.tag) #打印xmltest.xml的根标签

#遍历xml文档
for child in root:
    print(child.tag,child.attrib) #tag:标签名； attrib:属性
    for i in child:
        print(i.tag,i.text,i.attrib) #text：标签之间的内容

#只遍历year
for node in root.iter("year"):
    print(node.tag,node.text)