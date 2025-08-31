# 🏢 TechXcel Solutions – Scalable IT Infrastructure & Network Programming

This repository showcases a complete IT infrastructure simulation and network programming suite developed for **TechXcel Solutions**. It integrates enterprise-grade network design, cloud migration strategy, and Python-based socket programming — all tested and validated using **Cisco Packet Tracer** and custom-built Python scripts.

---

## 📦 Project Summary

This project demonstrates how to design, configure, and test a scalable, secure IT framework across two office locations (London & Liverpool). It includes:

- 🔧 High-availability network infrastructure with failover firewalls
- ☁️ Strategic cloud migration planning and disaster recovery
- 🧪 Simulation and stress testing using Cisco Packet Tracer
- 💻 Python socket programming with TCP and UDP protocols

---

## 🖼️ Network Architecture

Two detailed diagrams illustrate the infrastructure:

| Diagram | Description |
|--------|-------------|
| `network_topolog1.png` | Device-level topology across both sites |
| `network_diagram1.png` | VPN-secured inter-site architecture |

These visuals were created using **Cisco Packet Tracer** to simulate real-world connectivity, redundancy, and scalability.

---

## 🔧 Infrastructure Highlights

- Dual-site setup: **London Data Center** and **Liverpool Office**
- Redundant routers and switches for high availability
- DHCP services and segmented LANs
- VoIP configuration with IP phones and QoS
- OSPF dynamic routing for adaptive connectivity
- VPN-secured communication between offices
- Cloud integration for storage and recovery

---

## ☁️ Cloud Migration Strategy

- **Cost Analysis**: Short-term migration vs long-term operational costs
- **Mobility & Remote Access**: Application portability and secure data access
- **Skills Assessment**: Team readiness and training roadmap
- **Scalability & Security**: Modular infrastructure and encryption protocols
- **Disaster Recovery**: Automated backups and recovery testing

---

## 🧪 Testing & Validation

- ✅ Verified inter-office connectivity and VPN stability
- ✅ DHCP and VoIP services tested successfully
- ✅ Firewall failover simulated and validated
- ✅ Stress testing with 100+ concurrent users
- ✅ Security enforcement via ACLs and encryption

---

## 💻 Python Socket Programming

This module demonstrates TCP and UDP communication using Python sockets.

### 📂 Files Included

| File Name       | Description                                      |
|----------------|--------------------------------------------------|
| `tcp_server.py` | TCP server handling single and multiple clients |
| `tcp_client.py` | TCP client sending messages to server           |
| `udp_server.py` | UDP server receiving datagrams and responding   |
| `udp_client.py` | UDP client sending datagrams to server          |

### 🚀 How to Run

#### TCP
```bash
python tcp_server.py
python tcp_client.py
