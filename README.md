# Meshok Toolbox

A **showcase version** of a desktop application for marketplace data collection, analysis, filtering, and workflow automation.

> **Portfolio Showcase**
>
> This repository contains a simplified version of the original application and is intended to demonstrate the overall architecture, implementation approach, and automation techniques.
>
> The complete production version is maintained in a **private repository** because it contains proprietary business logic, production workflows, and marketplace-specific implementation details.

---

## Overview

Meshok Toolbox is a Python desktop application designed to automate marketplace research and communication workflows.

The application integrates with the marketplace API, collects structured data, applies configurable filtering rules, stores results locally, provides analytical tools, and supports automated communication processes.

The project demonstrates practical implementation of asynchronous programming, desktop application development, API integration, workflow automation, and local data analysis.

---

## Key Features

### 🔎 Marketplace Data Collection

- Asynchronous API communication using `asyncio` and `aiohttp`
- Configurable data collection workflows
- Automatic request retry handling
- Request throttling and delay management
- Persistent local dataset storage
- Configurable filtering rules
- Real-time operation logging

Supported filtering includes:

- User identifiers
- Marketplace activity metrics
- Registration period
- Review statistics
- Marketplace-specific indicators

---

### 📊 Analytics Module

Built-in analytical tools for processing collected marketplace data.

Features include:

- User statistics
- Geographic distribution analysis
- Location-based reports
- Registration activity trends
- Review and activity metrics
- JSON dataset processing

---

### ✉️ Communication Workflow

Automation module for marketplace messaging and communication.

Capabilities include:

- Browser session integration
- Secure cookie synchronization
- Personalized message generation
- Configurable sending parameters
- Delivery status tracking

---

### 🖥️ Desktop Application

The application provides a responsive desktop interface built with Tkinter, featuring:

- Background processing
- Multi-threaded architecture
- Persistent configuration management
- Live progress monitoring
- Dataset management
- Integrated analytics

---

## System Architecture

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
                  Marketplace API
                          │
                          ▼
                Data Collection Layer
                          │
                          ▼
                  Filtering Engine
                          │
                          ▼
                  Local Data Storage
                          │
          ┌───────────────┴───────────────┐
          ▼                               ▼
    Analytics Module             Communication Module
          │                               │
          ▼                               ▼
 Reports & Statistics          Workflow Automation
```

---

## Technologies

- Python
- Tkinter
- asyncio
- aiohttp
- threading
- HTTP API integration
- JSON data storage
- Local HTTP server
- Browser extension integration

---

## Repository Scope

This repository contains only the core components required to demonstrate the project's architecture and implementation.

The complete private version additionally includes:

- production workflow automation
- advanced filtering logic
- extended analytics
- optimized communication workflows
- additional utility modules
- project-specific automation tools

---

## Example Applications

- Marketplace research
- User discovery and analysis
- Dataset collection
- Marketplace analytics
- Workflow automation
- Communication management

---

## Screenshots

<p align="center">
  <img src="https://github.com/user-attachments/assets/36c7b8b1-6511-43f1-9402-6608be82314c"
       width="850"
       alt="Meshok Toolbox Main Interface">
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/77b98970-31a1-40df-b66a-7531d8a9b33d"
       width="600"
       alt="Analytics Module">
</p>

---

## Disclaimer

This repository is provided as part of my software development portfolio.

Some implementation details have been intentionally simplified or omitted, while the complete production version remains private.
