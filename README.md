# SDN Firewall using Mininet and POX

## 📌 Problem Statement

The objective of this project is to design and implement a Software Defined Networking (SDN) solution using Mininet and an OpenFlow controller (POX). The system demonstrates controller–switch interaction, flow rule installation, and network behavior control using match–action logic.

This project implements an **SDN-based firewall** that selectively blocks traffic between specific hosts while allowing all other communication.

---

## 🎯 Objectives

* Implement SDN architecture using Mininet and POX controller
* Handle `PacketIn` events in the controller
* Design and install OpenFlow match–action rules
* Demonstrate allowed and blocked traffic scenarios
* Observe and analyze flow table entries

---

## 🛠️ Technologies Used

* Mininet (Network Emulator)
* POX Controller (Python-based OpenFlow controller)
* OpenFlow 1.0 Protocol
* Ubuntu Linux (Virtual Machine)

---

## 🧱 Network Topology

* Single switch topology with 3 hosts:

  * h1 → 10.0.0.1
  * h2 → 10.0.0.2
  * h3 → 10.0.0.3
* All hosts are connected to a single OpenFlow switch (s1)

---

## ⚙️ Setup and Execution Steps

### 1. Install Mininet

```bash
sudo apt update
sudo apt install mininet -y
```

### 2. Clone POX Controller

```bash
git clone https://github.com/noxrepo/pox
cd pox
chmod +x pox.py
```

### 3. Create Controller File

```bash
nano firewall.py
```

Paste the controller code and save.

---

### 4. Start POX Controller

```bash
./pox.py firewall
```

---

### 5. Start Mininet (in new terminal)

```bash
sudo mn --topo single,3 --controller=remote,ip=127.0.0.1,port=6633
```

---

## 🧪 Test Scenarios

### ✅ Test Case 1: Allowed Traffic

```bash
h1 ping h2
```

**Expected Output:**

* Successful communication
* Packets transmitted and received

---

### ❌ Test Case 2: Blocked Traffic

```bash
h1 ping h3
```

**Expected Output:**

* 100% packet loss
* Communication blocked

---

## 📊 Flow Table Inspection

```bash
sh ovs-ofctl dump-flows s1
```

### 🔍 Actual Output:

```
cookie=0x0, duration=72.521s, table=0, n_packets=3, n_bytes=294, priority=10,ip,nw_src=10.0.0.1,nw_dst=10.0.0.2 actions=FLOOD
cookie=0x0, duration=72.469s, table=0, n_packets=3, n_bytes=294, priority=10,ip,nw_src=10.0.0.2,nw_dst=10.0.0.1 actions=FLOOD
cookie=0x0, duration=58.151s, table=0, n_packets=10, n_bytes=980, priority=100,ip,nw_src=10.0.0.1,nw_dst=10.0.0.3 actions=drop
```

---

## 🧠 Flow Table Analysis

* **Rule 1 (Allow h1 → h2):**
  Matches traffic from h1 to h2 and forwards packets using FLOOD
  → Demonstrates allowed communication

* **Rule 2 (Allow h2 → h1):**
  Reverse communication is also permitted
  → Ensures bidirectional connectivity

* **Rule 3 (Block h1 → h3):**
  High-priority rule that matches traffic from h1 to h3
  → `actions=drop` ensures packets are discarded
  → Demonstrates firewall behavior

* **Priority Handling:**

  * Block rule has higher priority (100)
  * Allow rules have lower priority (10)
    → Ensures blocking rule overrides forwarding

---

## 🔍 Controller Logic

* The controller listens for `PacketIn` events
* Matches packets based on:

  * Source IP (`nw_src`)
  * Destination IP (`nw_dst`)
  * Ethernet type (`dl_type = IPv4`)
* Installs:

  * **High-priority drop rule** for blocked traffic
  * **Lower-priority forwarding rules** for allowed traffic
* Uses `PacketOut` to forward the first packet

---

## 📸 Proof of Execution

Include the following screenshots:

* Controller logs showing rule installation
* `h1 ping h2` (successful)
* `h1 ping h3` (blocked)
* Flow table output

---

## 📈 Observations

* Initial packets are sent to the controller (`PacketIn`)
* Controller installs flow rules dynamically
* Subsequent packets bypass controller (handled by switch)
* Blocking is enforced via high-priority drop rule
* Packet counters (`n_packets`) confirm rule usage

---

## ✅ Conclusion

This project successfully demonstrates:

* SDN-based traffic control using OpenFlow
* Implementation of firewall policies
* Dynamic flow rule installation
* Efficient packet forwarding and filtering

---

## 📚 References

* https://mininet.org/overview/
* https://github.com/mininet/mininet
* https://github.com/noxrepo/pox
* OpenFlow Switch Specification

---
