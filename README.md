# Meshok Toolbox

Desktop automation application for marketplace data analysis, user discovery, filtering and communication workflows.

---

## Overview

**Meshok Toolbox** is a Python desktop application designed to automate marketplace research and workflow management.

The application integrates with the Meshok API, collects marketplace data, applies configurable filtering rules, stores results locally, provides analytical tools, and supports automated communication workflows.

The project demonstrates:

- asynchronous API communication
- desktop application development
- data processing and analysis
- automation workflows
- browser session integration

---

## Features

## 🔎 Marketplace Data Scanner

- ⚡ Asynchronous API processing using `asyncio` and `aiohttp`
- 🖥️ Desktop interface built with Tkinter
- 🧵 Multi-threaded application architecture
- 🔍 Configurable filtering system:
    - User identifiers
    - Activity metrics
    - Registration period
    - Marketplace statistics
    - Review indicators
- 🔄 Automatic request retry handling
- ⏱️ Request throttling and delay management
- 💾 Local dataset storage
- ⚙️ Persistent configuration management
- 📋 Real-time operation logging


---

## 📊 Analytics Module

Built-in tools for analyzing collected marketplace datasets.

Capabilities:

- 👥 User statistics overview
- 🌍 Geographic distribution analysis
- 🏙️ Location-based reports
- 📅 Registration activity analysis
- 📈 Review and activity statistics
- 📊 JSON dataset processing


---

## ✉️ Communication Workflow

Automation module for managing marketplace communication workflows.

Features:

- 🔐 Browser session integration
- 🍪 Secure cookie synchronization
- 👤 Personalized message generation
- ⏱️ Configurable sending parameters
- 🔄 Delivery status tracking


---

## Technologies

- Python 3.x
- Tkinter
- asyncio
- aiohttp
- threading
- HTTP API integration
- JSON data storage
- Local HTTP server
- Browser extension integration


---

## Architecture

```text
                  Browser Extension
                          │
                          ▼
                 Local HTTP Server
                          │
                          ▼
                Session Management
                          │
                          ▼
                 Meshok Toolbox
                          │
       ┌──────────────────┼──────────────────┐
       │                  │                  │
       ▼                  ▼                  ▼

 API Integration    Analytics Engine   Communication
       │                  │                  │
       ▼                  ▼                  ▼

 Marketplace Data   Reports & Metrics   Workflow Automation
```
---

## Architecture

```text
Workflow
Marketplace API
       │
       ▼
Data Collection Layer
       │
       ▼
Filtering Engine
       │
       ▼
Local Dataset
       │
       ├───────────────┐
       │               │
       ▼               ▼

 Desktop GUI      Analytics Module

       │
       ▼

Communication Workflow
---
```

## Screenshots

<p align="center"> <img width="850" alt="Meshok Toolbox Screenshot" src="https://github.com/user-attachments/assets/36c7b8b1-6511-43f1-9402-6608be82314c"> </p> <p align="center"> <img width="700" alt="Analytics Module Screenshot" src="https://github.com/user-attachments/assets/77b98970-31a1-40df-b66a-7531d8a9b33d"> </p>

---

## Project Goals

Demonstrate Python desktop application development
Build asynchronous API-based automation tools
Process and analyze marketplace datasets
Create configurable workflow automation
Integrate desktop applications with browser sessions
