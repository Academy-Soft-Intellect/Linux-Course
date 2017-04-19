- TCP/IP four layer model behind each networking connection. OSI is just a theoretical model, TCP/IP was inspired by it and implemented. [OSI vs TCP/IP](http://stackoverflow.com/questions/9329105/are-we-using-tcp-ip-or-osi-in-internet)

- Networking is 
  * IP Address  => numerical label assigned to each device using the Internet Protocol for communication.
  * Subnet Mask => to which network a computer belongs.
  * DNS => to translate FQDNs(Fully Qualified Domain Names) to IPs, process known as forward lookup and IPs to FQDNs, a process knowns as reverse lookup.
  * Default gateway => A default gateway serves as an access point or IP router that a networked computer uses to send  information to a computer in another network or the Internet. Default simply means that this gateway is used by default, unless an application specifies another gateway.
  
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

- DNS, DNS zones
  * hierarchical naming system that translates IPs to FQDNs(forward lookup) and FQDNs to IPs(reverse loookup).
  * The DNS for a domain is recursively distributed into ZONEs, each zone is responsbile for a specific part of the domain tree.
  * resource record is an entry in a DNS zone file that contain informatino about a particular name or object in the zone.
  
 - Resource record consist of owner-name, TTL(time to live), class(almost always "IN" ( internet )), type ( the sort of information stored by this records, "A" record maps a hosts name ot an IPv4 address ) and data.
  * Example => www.soft-intellect.bg 300 IN A 192.168.0.1
  * Example => \<OWNER-NAME> \<TTL> \<class> \<type> \<data>
