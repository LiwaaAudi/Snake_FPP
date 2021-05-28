let userScore = 0;
let computerScore = 0;
const userScore_span = document.getElementById("user-score");
const computerScore_span = document.getElementById("computer-score");
const scoreBoard_div = document.querySelector(".score-board");
const result_p = document.querySelector(".result > p");
const rock_div = document.getElementById("r");
const paper_div = document.getElementById("p");
const scissors_div = document.getElementById("s");

function getComputerChoice() {
    const choices = ['r', 'p', 's'];
    const randomNumber = Math.floor(Math.random() * 3);
    return choices[randomNumber];
}

function convertToWord(letter) {
    if (letter === "r") return "Rock";
    if (letter === "p") return "Paper";
    return "Scissors";
}

function win(userchoice, computerchoice) {
    const userSmallWord = "(user)".fontsize(3).sup();
    const compSmallWord = "(comp)".fontsize(3).sup();
    const uc = document.getElementById(userchoice);
    userScore++;
    userScore_span.innerHTML = userScore;
    computerScore_span.innerHTML = computerScore;
    result_p.innerHTML = `${convertToWord(userchoice)}${userSmallWord} beats ${convertToWord(computerchoice)}${compSmallWord}. You won! 🔥`;
    uc.classList.add('green-glow');
    setTimeout( () => { uc.classList.remove('green-glow') }, 1000);
}

function lose(userchoice, computerchoice) {
    const userSmallWord = "(user)".fontsize(3).sup();
    const compSmallWord = "(comp)".fontsize(3).sup();
    const uc = document.getElementById(userchoice);
    computerScore++;
    computerScore_span.innerHTML = computerScore;
    userScore_span.innerHTML = userScore;
    result_p.innerHTML = `${convertToWord(userchoice)}${userSmallWord} loses to ${convertToWord(computerchoice)}${compSmallWord}. You lost... 😥`;
    uc.classList.add('red-glow');
    setTimeout( () => { uc.classList.remove('red-glow') }, 1000);
}

function draw(userchoice, computerchoice) {
    const userSmallWord = "(user)".fontsize(3).sup();
    const compSmallWord = "(comp)".fontsize(3).sup();
    const uc = document.getElementById(userchoice);
    result_p.innerHTML = `${convertToWord(userchoice)}${userSmallWord} equals ${convertToWord(computerchoice)}${compSmallWord}. It's a draw 😑`;
    uc.classList.add('gray-glow');
    setTimeout( () => { uc.classList.remove('gray-glow') }, 1000);
}

function game(userChoice) {
    const computerChoice = getComputerChoice();
    switch (userChoice + computerChoice) {
        case "rs":
        case "pr":
        case "sp":
            win(userChoice, computerChoice)
            break;
        case "rp":
        case "ps":
        case "sr":
            lose(userChoice, computerChoice);
            break;
        case "rr":
        case "pp":
        case "ss":
            draw(userChoice, computerChoice);
            break;

    }
}

function main() {
    rock_div.addEventListener('click', () => {
        game("r");
    });

    paper_div.addEventListener('click', () => {
        game("p");
    });

    scissors_div.addEventListener('click', () => {
        game("s");
    });
}

main();