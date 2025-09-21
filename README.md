# Furniture Management System

A Python-based console application for managing furniture inventory, orders, and sales for BRJ Furniture Stores.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technical Architecture](#technical-architecture)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Data Format](#data-format)
- [API Reference](#api-reference)
- [Configuration](#configuration)
- [Dependencies](#dependencies)
- [Development](#development)
- [Contributing](#contributing)
- [License](#license)

## 🏢 Overview

The Furniture Management System is a comprehensive inventory management solution designed for furniture retail operations. It provides functionality for ordering furniture from manufacturers, selling to customers, and maintaining real-time inventory tracking.

**Company Details:**
- **Store Name:** BRJ Furniture Stores
- **Email:** brjfurniture@gmail.com
- **Phone:** 9876543210

## ✨ Features

### Core Functionality
- **Inventory Management**: Real-time tracking of furniture stock levels
- **Order Processing**: Order furniture from manufacturers with automatic inventory updates
- **Sales Management**: Process customer sales with VAT calculation and shipping costs
- **Invoice Generation**: Automatic generation of detailed invoices for both orders and sales
- **Data Persistence**: File-based storage system for inventory data

### Business Features
- **Multi-item Transactions**: Support for ordering/selling multiple furniture items in a single transaction
- **Tax Calculation**: Automatic 13% VAT calculation on sales
- **Shipping Costs**: Fixed Rs. 50 shipping cost per sale
- **Employee Tracking**: Track which employee placed orders
- **Customer Management**: Track customer information for sales

## 🏗️ Technical Architecture

### System Design
The application follows a modular architecture with clear separation of concerns:

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   main.py       │    │  operation.py   │    │ messages_display│
│   (Entry Point) │───▶│  (Business      │───▶│     .py         │
│                  │    │   Logic)        │    │  (UI Messages)  │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         │                       ▼                       │
         │              ┌─────────────────┐             │
         │              │    read.py      │             │
         │              │  (Data Access)  │             │
         │              └─────────────────┘             │
         │                       │                       │
         │                       ▼                       │
         │              ┌─────────────────┐             │
         └─────────────▶│    write.py     │◀────────────┘
                        │ (Data Persistence│
                        │  & File I/O)    │
                        └─────────────────┘
```

### Data Flow
1. **Initialization**: System loads furniture data from `furniture.txt`
2. **User Interaction**: Menu-driven interface for operation selection
3. **Data Processing**: Business logic processes user inputs
4. **Inventory Updates**: Real-time updates to stock quantities
5. **File Persistence**: Changes saved to `furniture.txt`
6. **Invoice Generation**: Transaction details saved to timestamped files

## 🚀 Installation

### Prerequisites
- Python 3.10.0 or higher (but less than 3.12)
- Poetry (for dependency management)

### Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd Furniture-Management-System
   ```

2. **Install dependencies using Poetry:**
   ```bash
   poetry install
   ```

3. **Activate the virtual environment:**
   ```bash
   poetry shell
   ```

4. **Run the application:**
   ```bash
   python main.py
   ```

### Alternative Installation (without Poetry)
```bash
pip install tf-encrypted==0.9.1
python main.py
```

## 💻 Usage

### Starting the Application
```bash
python main.py
```

### Main Menu Options
The application presents a menu with four options:

1. **Order Furniture from Manufacturer**
   - Add new inventory from manufacturers
   - Update stock quantities
   - Generate purchase invoices

2. **Sell Furniture to Customer**
   - Process customer sales
   - Calculate VAT (13%) and shipping costs
   - Generate sales invoices

3. **Display Inventory**
   - View current stock levels
   - Check product availability

4. **Exit**
   - Safely terminate the application

### Example Workflow

#### Ordering Furniture
```
1. Select option 1 from main menu
2. Enter employee name
3. View available furniture catalog
4. Select furniture by ID number
5. Enter quantity to order
6. Repeat for additional items
7. Review and confirm order
8. Invoice automatically generated
```

#### Selling Furniture
```
1. Select option 2 from main menu
2. Enter customer name
3. View current inventory
4. Select furniture by ID number
5. Enter quantity to sell
6. System validates stock availability
7. Repeat for additional items
8. Review order with tax calculations
9. Invoice automatically generated
```

## 📁 File Structure

```
Furniture-Management-System/
├── main.py                 # Application entry point
├── operation.py            # Core business logic
├── read.py                 # Data reading operations
├── write.py                # Data writing and file operations
├── messages_display.py     # User interface messages
├── furniture.txt           # Inventory data storage
├── pyproject.toml          # Poetry configuration
├── poetry.lock             # Dependency lock file
└── README.md               # This documentation
```

### File Descriptions

- **`main.py`**: Application entry point with main menu loop
- **`operation.py`**: Contains core business logic for ordering and selling
- **`read.py`**: Handles reading furniture data from files
- **`write.py`**: Manages data persistence and invoice generation
- **`messages_display.py`**: Centralized user interface messages
- **`furniture.txt`**: CSV-formatted inventory database

## 📊 Data Format

### Inventory Data Structure
The `furniture.txt` file uses CSV format with the following structure:

```csv
ID,Manufacturer,Product Name,Quantity,Price
1,HNI Corporation,Bunk Bed,110,400
2,Haworth Inc.,Twin Bed,643,600
```

**Field Descriptions:**
- **ID**: Unique furniture identifier (integer)
- **Manufacturer**: Company name (string)
- **Product Name**: Furniture item name (string)
- **Quantity**: Available stock (integer)
- **Price**: Unit price in rupees (integer)

### Invoice File Format
Invoices are saved as timestamped text files:
- **Order Invoices**: `{EmployeeName}_{HH-MM-SS}.txt`
- **Sales Invoices**: `{CustomerName}_{HH-MM-SS}.txt`

## 🔧 API Reference

### Core Functions

#### `main.py`
- **Main Loop**: Handles user input and menu navigation
- **Input Validation**: Ensures proper integer input for menu selection

#### `operation.py`
- **`order_from_manufacturer()`**: Processes manufacturer orders
- **`sell_to_customer()`**: Handles customer sales transactions
- **`display_inventory()`**: Shows current inventory status

#### `read.py`
- **`file(furniture_dict, furniture_id)`**: Loads inventory data into memory
- **`file_read()`**: Displays formatted inventory table

#### `write.py`
- **`value(furniture_dict)`**: Saves inventory changes to file
- **`print_invoice_order()`**: Generates purchase invoices
- **`print_invoice_sale()`**: Generates sales invoices

#### `messages_display.py`
- **`welcome_text()`**: Displays company header
- **`option()`**: Shows main menu options
- **`table()`**: Formats inventory display header
- **Error Messages**: Various validation and error messages

## ⚙️ Configuration

### Poetry Configuration (`pyproject.toml`)
```toml
[tool.poetry]
name = "python-template"
version = "0.1.0"
description = ""
authors = ["Your Name <you@example.com>"]

[tool.poetry.dependencies]
python = ">=3.10.0,<3.12"
tf-encrypted = "^0.9.1"
```

### Code Quality Tools
- **Pyright**: Type checking configuration
- **Ruff**: Linting and code formatting
  - Selected rules: E, W, F, I, B, C4, ARG, SIM
  - Ignored: W291, W292, W293 (whitespace rules)

## 📦 Dependencies

### Core Dependencies
- **Python**: >=3.10.0, <3.12
- **tf-encrypted**: ^0.9.1 (TensorFlow Encrypted for secure computations)

### Development Dependencies
- **Poetry**: Dependency management and packaging
- **Pyright**: Static type checking
- **Ruff**: Fast Python linter and formatter

## 🛠️ Development

### Code Style
The project follows Python best practices with:
- Modular design with clear separation of concerns
- Comprehensive error handling
- Input validation for user interactions
- Consistent naming conventions

### Error Handling
- **ValueError**: Handles non-integer inputs
- **Range Validation**: Ensures valid menu selections and quantities
- **Stock Validation**: Prevents overselling inventory
- **File Operations**: Proper file handling with automatic closure

### Debugging Features
- Debug output for availability checking
- Detailed error messages for invalid inputs
- Transaction logging through invoice generation

## 🤝 Contributing

### Development Setup
1. Fork the repository
2. Create a feature branch
3. Install development dependencies
4. Make your changes
5. Run linting: `ruff check .`
6. Submit a pull request

### Code Standards
- Follow PEP 8 style guidelines
- Add appropriate error handling
- Include input validation
- Maintain modular architecture
- Update documentation for new features

## 📄 License

This project is part of a furniture management system for BRJ Furniture Stores. Please contact the development team for licensing information.

---

**Contact Information:**
- **Email**: brjfurniture@gmail.com
- **Phone**: 9876543210

**Last Updated**: December 2024
