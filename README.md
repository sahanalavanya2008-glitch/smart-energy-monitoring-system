# Smart Energy Monitoring System ⚡

A simulated IoT-based energy monitoring platform inspired by renewable energy systems.

## Features
- Simulates energy devices
- Generates real-time energy readings
- Tracks battery percentage
- Provides foundation for backend API integration

## Technologies
- Python
- IoT Simulation
- REST API (upcoming)
- PostgreSQL (upcoming)
- Docker (upcoming)

## Goal
Build a scalable energy monitoring system similar to real-world IoT platforms.

## Backend API

The system includes a FastAPI backend that:
- Receives energy readings
- Stores device information
- Provides API endpoints for monitoring

Endpoints:
- GET / → Check system status
- POST /energy → Add energy data
- GET /energy → View energy readings
