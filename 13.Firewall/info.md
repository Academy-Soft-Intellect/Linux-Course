**Firewall**

 * IPtables was the default firewall tool, supporting only ipv4 address.
 * Firewalld is the new firewall tool. It simplifies firewall management by classifying all network traffic into zones.

**Packet check frequency**
1. IP address is tied to a specific zone => the rules for that zone will be parsed.
2. IP address is not tied to a zone, the zone for the incoming netwotk interface will be used.
3. If the network interface is not associated with a zone, the default zone will be used.

Valid zones: public, trusted, home, dmz, block drop, for more zones 'man firewalld.zones'

**Pre-defined services**
Pre-defined services are bound to ports, so they are easier to cofigure.
ssh, dhcpv6-client, samba-client, for more pre-defined services 'firewall-cmd --get-service'
