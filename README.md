# Snake_FPP
A snake-game with it's website

| ![Homepage](snake.jpeg) | ![Homepage](scissors.png) |
| ------------- | ------------- |

## 📖 Installation

1. Make sure you have [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed.
1. Make sure you have [Python](https://www.python.org/) installed.
1. Clone the repository:
    ```bash
    git clone https://github.com/LiwaaAudi/Snake_FPP.git
    cd ~/Snake_FPP
    ```
1. Create the virtual environment:
    ```bash
    make venv
    ```
1. Activate the virtual environment:
    ```bash
    source venv/bin/activate
    ```
1. Install dependencies:
    ```bash
    make dependencies
    ```

## 🚀 Setup

1. Make necessary migrations:
    ```bash
    make migrations
    ```
    ```bash
    make migrate
    ```
1. Run the server:
    ```bash
    make server
    # Now you can Load the site at http://127.0.0.1:8000
    ```

## 🏁 Play
1. Make sure to keep the first server terminal running
1. Open a new terminal
    ```bash
    cd ~/Snake_FPP
    ```
1. Run the game:
    ```bash
    make play
    ```
    You will see a shop item in the main menu which allows you to 
    Visit the game website, make sure you are on localhost port 8000
    Or change it in the [snake.py file](https://github.com/LiwaaAudi/Snake_FPP/blob/master/snake.py) line 45
    
