import xml.etree.ElementTree as ET


tree = ET.parse('search.xml')
root = tree.getroot()

for group in root.findall('group'):
    timing_exbytes = group.find('timingExbytes')
    if timing_exbytes is not None:
        bbo = timing_exbytes.find('bbo')
        if bbo is not None:
            print(f"Group: {group.find('name').text}, bbo: {bbo.text}")
        else:
            print(f"Group: {group.find('name').text}, bbo: not found")
