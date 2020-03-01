# Author:Fuhong Gao
import xml.etree.ElementTree as ET
new_xml = ET.Element("personinfolist")
personinfo = ET.SubElement(new_xml, "personinfo", attrib={"enrolled": "yes"})
name = ET.SubElement(personinfo, "name")
name.text = "Fuhong Gao"
age = ET.SubElement(personinfo, "age", attrib={"checked": "no"})
sex = ET.SubElement(personinfo, "sex")
age.text = '22'
sex.text = 'male'
personinfo2 = ET.SubElement(new_xml, "personinfo", attrib={"enrolled": "no"})
name = ET.SubElement(personinfo2, "name")
name.text = "Xiao Gu"
age = ET.SubElement(personinfo2, "age")
sex = ET.SubElement(personinfo2, "sex")
age.text = '18'
sex.text = 'female'
et = ET.ElementTree(new_xml)  # 生成文档对象
et.write("test.xml", encoding="utf-8", xml_declaration=True)
ET.dump(new_xml)  # 打印生成的格式