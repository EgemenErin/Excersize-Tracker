# Exercise Tracker

This project is a Python script that allows you to track your exercises and automatically log them into a Google Sheet using the Nutritionix API.

## Features

- Track various exercises by providing a description of the exercise.
- Calculate calories burned based on your weight, height, gender, and age.
- Log exercise data (name, duration, calories burned) into a Google Sheet.

## Requirements

- Python 3.x
- `requests` library

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/exercise-tracker.git
   cd exercise-tracker
   ```

2. Install the required Python packages:
   ```bash
   pip install requests
   ```

3. Set up environment variables:

   Create a `.env` file in the root of your project directory and add the following variables:

   ```bash
   SHEET_ENDPOINT=<Your Google Sheet API Endpoint>
   APP_ID=<Your Nutritionix App ID>
   API_KEY=<Your Nutritionix API Key>
   ```

   Replace the placeholders with your actual API credentials and endpoint.

## Usage

1. Run the script:

   ```bash
   python exercise_tracker.py
   ```

2. When prompted, enter the exercise you did:

   ```bash
   Tell me which exercise you did? 
   ```

3. The script will calculate the calories burned and log the exercise details (date, time, exercise name, duration, and calories) into your Google Sheet.

## Example

```
Tell me which exercise you did? Ran 5 kilometers
{
    'exercises': [
        {
            'name': 'running',
            'duration_min': 30,
            'nf_calories': 300,
        }
    ]
}
```

The above data will be logged into the Google Sheet with the current date and time.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
