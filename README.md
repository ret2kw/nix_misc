nix_misc
=========

miscellaneous code primarily for linux



###vbox_pipe.py###
Dynamically build menus for virtualbox vms in openbox

Needs something like:

`
<menu id="root-menu-603260" label="vboxVMs" execute="~/.config/openbox/vbox_pipe.py"></menu>
`

in menu.xml, this will generate a list of virtual machines by group.
