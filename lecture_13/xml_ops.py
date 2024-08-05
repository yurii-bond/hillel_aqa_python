import xml.etree.ElementTree as ET


tree = ET.parse('data.xml')
root = tree.getroot()

for child in root:
    print(child.tag, child.attrib)
    for subchild in child:
        print(subchild.tag, subchild.attrib)
        for subsubchild in subchild:
            print(subsubchild.tag, subsubchild.attrib)


root = ET.Element('data')
child1 = ET.SubElement(root, 'child1')
child1.text = 'Data 1'
child1.attrib = {'name': 'child1'}
child2 = ET.SubElement(root, 'child2')
child2.text = 'Data 2'

tree = ET.ElementTree(root)

tree.write('output.xml')


