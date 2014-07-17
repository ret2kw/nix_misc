#!/usr/bin/python

from vboxapi import VirtualBoxManager
from xml.dom import minidom
from random import random
import sys


mgr = VirtualBoxManager(None, None)
vbox = mgr.vbox


template = """
	<openbox_pipe_menu>
		<item label="MACHINENAME">
			<action name="Execute">
				<execute>true</execute>
			</action>
		</item>
	</openbox_pipe_menu>"""

group = """<menu id="RANDOMID" label="GROUPNAME"></menu>"""

dom1 = minidom.parseString(template)
dom2 = minidom.parseString(group)

groups = []

#getting groups into array format so we can pass to getMachinesByGroups()
for group in vbox.getMachineGroups():
    groups.append([group])


for group in groups:
    groupnode = dom2.getElementsByTagName('menu')[0].cloneNode(True)
    groupname = group[0]
    groupnode.setAttribute('label', groupname)
    groupnode.setAttribute('id', str(random()).split('.')[1][:5])

    menunode = dom1.childNodes[-1].appendChild(groupnode)

    for machine in vbox.getMachinesByGroups(group):

        newnode = dom1.getElementsByTagName('item')[0].cloneNode(True)
        execute = newnode.childNodes[1].childNodes[1]

        value = machine.name

        newnode.setAttribute('label', value)

        execute.firstChild.nodeValue = 'vboxmanage startvm %s' % value

        menunode.appendChild(newnode) 

dom1.childNodes[0].removeChild(dom1.childNodes[0].childNodes[1])

print dom1.documentElement.toxml()






