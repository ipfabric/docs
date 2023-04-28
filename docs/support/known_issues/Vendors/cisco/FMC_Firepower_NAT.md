# NAT Support for Cisco FMC Firepower

## 7000 & 8000 Series Are Not Supported

Current NAT implementation for Firepower appliances supports only **Threat Defense NAT** policies.

**Firepower NAT** policies for 7000 & 8000 Series are not supported due to lack of API endpoints

## PAT Port Allocation

When Firepower PAT performs a port translation, it tries to use the same port number as the real source. However, if the real port is already in use, it selects a mapped port from the same range as the real port. The ranges are: 1-511, 512-1023, and 1024-65535.

IP Fabric's end-to-end path-lookup does not follow this behaviour. It can use any port from the matching range for simulation purposes.
