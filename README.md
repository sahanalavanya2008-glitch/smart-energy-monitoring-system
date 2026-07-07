# Smart Energy Monitoring System ⚡

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)
![CI](https://github.com/sahanalavanya2008-glitch/smart-energy-monitoring-system/actions/workflows/ci.yml/badge.svg)

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

- ## API Documentation

### Base Endpoint

GET /

Returns the system status.

Example response:

{
  "message": "Smart Energy Monitoring System API Running"
}


### Add Energy Reading

POST /energy

Parameters:

- device_id
- usage
- battery

Example:

device_id = Powerwall_01
usage = 5.4
battery = 80


### Get Energy Data

GET /energy

Returns stored energy readings.
          IoT Devices
              |
              ↓
     Sensor Simulator
              |
              ↓
       FastAPI Service
              |
              ↓
        Database Layer
              |
              ↓
      Energy Monitoring Data
      Engineering Concepts
REST API design
Data persistence
Containerization
Service architecture
IoT data simulation
## Project Highlights

- Simulates IoT energy devices
- Built REST APIs using FastAPI
- Implements persistent data storage
- Containerized using Docker
- Automated testing using GitHub Actions
- ## Key Features

- Simulated IoT energy devices
- Real-time energy data generation
- REST API using FastAPI
- Persistent data storage
- Docker containerization
- Automated testing with GitHub Actions
- ## Tech Stack

- Python
- FastAPI
- SQLite
- Docker
- GitHub Actions
- IoT Simulation
- ## Future Enhancements

- PostgreSQL integration
- Kubernetes deployment
- Cloud monitoring
- Real-time streaming architecture
