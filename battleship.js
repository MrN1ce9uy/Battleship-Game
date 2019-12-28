// This is JavaScript
// This is a game that plays like the game Battleship
// The browser hides ships and you must guess where they are located
// You must place this .js file inside the same folder on your computer as the .html file
// Open the .html file in your web browser to play the game

var randomLoc = Math.floor(Math.random() * 5);
var location1 = randomLoc;
var location2 = location1 + 1;
var location3 = location2 + 1;
var guess;
var hits = 0;
var guesses = 0;
var isSunk = false;

while (isSunk == false) {
    guess = prompt("Ready, aim, fire! (enter a number from 0-6):");
    if (guess < 0 || guess > 6) {
        alert("Please enter a valid cell number!");
    }
    else {
        guesses = guesses + 1;
            
        if (guess == location1 || guess == location2 || guess == location3) {
            alert("HIT!");
            hits = hits + 1;
            if (hits == 3) {
                isSunk = true;
                alert("You sank my battleship!");
            }    
        }
        else {
            alert("MISS");
        }
    }          
} 

var stats = "You took " + guesses + " guesses to sink the battelship, " + "which means your shooting accuracy was " + (3/guesses);
alert(stats);
