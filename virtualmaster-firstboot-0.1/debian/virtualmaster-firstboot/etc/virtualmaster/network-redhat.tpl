#
# autogenerated by virtualmaster on _virtualmaster_timestamp_
# 
DEVICE=eth0
ONBOOT=yes
BOOTPROTO=static
IPADDR=_virtualmaster_ipv4_address_
NETMASK=_virtualmaster_ipv4_netmask_
GATEWAY=_virtualmaster_ipv4_gateway_
ETHTOOL_OPTIONS='-K eth0 tx off'
#
# The line above will disable TCP checksumming which
# might resolve problems for some users.
#
# See http://www.shorewall.net/XenMyWay-Routed.html and search for
# ethtool -K eth0 tx off
#