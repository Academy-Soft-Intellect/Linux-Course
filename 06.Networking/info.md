- Networking is 
  * IP Address  => numerical label assigned to each device using the Internet Protocol for communication.
  * Subnet Mask => to which network a computer belongs.
  * DNS => to translate IP addresses into Fully Qualified Domain Names(FQDNs).

- Networking interface name parts
  * en => ethernet interface.
  * wl => WLAN interface.
  * o => onboard (built in).
  * s => hot plog plug spot.
  * p => PCI location (externally attached).

- Get networking info
  * ip addr show => show current network settings.
  * ip route show => show the routing table.
  * ss => get services information.

- Set networking
  * nmcli
  * nmtui

- Set hostname
  * hostnamctl 

- Important files
  * /etc/nsswitch.conf => which file from the below to query first.
  * /etc/hosts => adding important local nodes.
  * /etc/resolv.conf => set global internet DNS servers.

