# Flatmates Bill Sharing

An app that calculates how much each flatmate has to pay for a given period. The calculation is based on the number of days each flatmate stayed in the house. The app also generates a PDF report with the details of the bill and the amount each flatmate has to pay.

## Getting Started

### Prerequisites

- Python 3.x
- Pip

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/your_username_/Project-Name.git
   ```
2. Install dependencies
   ```sh
   pip install -r requirements.txt
   ```

### Usage

To run the application, execute the `main.py` file:

```sh
python main.py
```

This will generate a PDF report named `flatmates_report.pdf` in the root directory.

## Objects

The application is composed of the following objects:

- **`Flatmate`**: Represents a person who lives in the flat. It contains information like name, last name, and the number of days they stayed in the flat during a specific period.
- **`Flat`**: Represents the flat itself. It contains information about the address, the landlord, and the list of flatmates.
- **`Bill`**: Represents a bill for a specific period. It contains information about the total amount, the period, and the expenses. It also has methods to calculate how much each flatmate has to pay.
- **`Report`**: Represents the PDF report. It has a method to generate a PDF file with the details of the bill and the amount each flatmate has to pay.
