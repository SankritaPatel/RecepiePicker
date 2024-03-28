# Recipe Picker

This is a simple recipe picker application built using Python's Tkinter library. It allows users to randomly select a recipe from a SQLite database and view its ingredients.

## Features

- **Random Recipe Selection:** Users can shuffle through recipes in the database to get random suggestions.
- **Database Connectivity:** The application connects to a SQLite database to fetch recipe data.
- **Dynamic UI:** The user interface dynamically updates to display the selected recipe and its ingredients.
- **Simple Navigation:** Users can easily navigate between the main menu and recipe details.

## Requirements

- Python 3.x
- Tkinter library
- PIL (Python Imaging Library)
- pyglet library
- SQLite3

## Installation

1. Clone this repository to your local machine:

```
git clone https://github.com/SankritaPatel/RecepiePicker.git
```

2. Navigate to the project directory:

```
cd RecepiePicker
```

3. Install the required dependencies:

```
pip install -r requirements.txt
```

4. Run the application:

```
python recepie_picker.py
```

## Usage

- Upon running the application, users are presented with a main menu.
- Clicking the "SHUFFLE" button randomly selects a recipe and displays its details, including the recipe name and ingredients.
- Users can click the "BACK" button to return to the main menu and select another recipe.

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, feel free to open an issue or create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
