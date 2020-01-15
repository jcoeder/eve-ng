# eve-ng
eve-ng

Linux GNOME telnet handler - https://major.io/2016/07/22/setting-up-a-telnet-handler-in-gnome-3/


## Cisco NX-OSv 9000 VPC
https://techstat.net/cisco-nexus-nx-osv-9000-lacp-vpc-bug-fix/

This post will show you how to fix the LACP “BUG” on the NX-OSv 9000 so that you can LACP to whatever devices you want. Thus you will be able to practice VPC topologies!

If you need the NX-OS 9000 image for GNS3 go here:
https://upw.io/wa/nxosv-final.7.0.3.I7.2.qcow2

For documentation on how to add the NX-OSv 9000 image to GNS3 go here:
https://docs.gns3.com/appliances/cisco-nxosv9k.html

Now once you have your topology running in GNS3 and the images have finally booted run the following script from CONFIG mode.

Once you have added the script you MUST reload for this to work!

```
feature bash-shell
event manager applet HACK
description "HACK"
event syslog pattern "Configured from vty by root"
action 1.0 cli run bash sudo -u root cp /isan/bin/lacp /isan/bin/lacp2
action 2.0 cli run bash sudo -u root echo -e "00098830: 8c5f f7ff 85c0 7442 c685 9cfe ffff 01c6\n00098840: 859d feff ff80 c685 9efe ffff c2c6 859f\n00098850: feff ff00 c685 a0fe ffff 00c6 85a1 feff\n00098860: ff02 8b83 90fe ffff 8d95 9cfe ffff 8b0a" | sudo xxd -r - /isan/bin/lacp2
action 3.0 cli run bash sudo rm /isan/bin/lacp
action 4.0 cli run bash sudo mv /isan/bin/lacp2  /isan/bin/lacp
action 5.0 cli run bash sudo killall -9 lacp
action 6.0 event-default
event manager applet HACK2
description "HACK"
event syslog pattern "Supervisor 1 is active"
action 1.0 cli run bash sudo -u root cp /isan/bin/lacp /isan/bin/lacp2
action 2.0 cli run bash sudo -u root echo -e "00098830: 8c5f f7ff 85c0 7442 c685 9cfe ffff 01c6\n00098840: 859d feff ff80 c685 9efe ffff c2c6 859f\n00098850: feff ff00 c685 a0fe ffff 00c6 85a1 feff\n00098860: ff02 8b83 90fe ffff 8d95 9cfe ffff 8b0a" | sudo xxd -r - /isan/bin/lacp2
action 3.0 cli run bash sudo rm /isan/bin/lacp
action 4.0 cli run bash sudo mv /isan/bin/lacp2  /isan/bin/lacp
action 5.0 cli run bash sudo sleep 30
action 6.0 cli run bash sudo killall -9 lacp
action 7.0 event-default
```
