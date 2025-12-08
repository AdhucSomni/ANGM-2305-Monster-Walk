# Monster-Walk

## Demo
Demo Video: <URL>

## GitHub Repository
GitHub Repo: <https://github.com/AdhucSomni/ANGM-2305-Monster-Walk.git>

## Description
Monster-Walk is a 2D side-scrolling project. The work features a character that players can control using keyboard inputs to walk left or right across the window screen. The project features fundamental game development concepts including sprite animation, camera systems, and rendering.

The main game loop runs at 60 frames per second and handles player input through the A and D keys for left and right movement respectively. The player character is composed of multiple sprites that are cycled through based on the direction of movement, with separate frames for idling, walking left, and walking right, while a camera system follows the player and scrolls the background to give the illusion of travel through a continuous world.

The project consists of the following files and folders:
    •	project.py: The main file containing all the code for the game logic, including the Player class for  character control and animation, the Camera class to track the player, and the main game loop.
    
    •	background: A folder containing the background image asset used. The sunny_day.png file provides the backdrop that repeats as the player moves around.
    
    •	Sprite pngs: A folder containing all the character sprite images. This includes: 
        o	S1.png: An idle stance
        o	S2.png and S3.png: Right-facing walking frames
        o	S4.png and S5.png: Left-facing walking frames
The sprite assets are organized in a separate folder for easy management and potential future expansion with additional character sprites.

The main design decision was implementing a scrolling background that seamlessly tiles as the player moves. The camera offset system ensures smooth tracking of the player while the background continuously loads by finding tile position using modulo. The game runs Fullscreen mode and automatically scales the background to match the screen height while maintaining aspect ratio, making sure the game looks appropriate on different display sizes.

As for areas to be improved on, there are several ways to build on this project. Such as additional animation with jumps, running, or generally other forms of movement. Terrian elements such as platforms or obstacles could be added for better interactivity. Other elements that could be added include more frames for the walking cycle, music and sfx, additional backgrounds, or gravity and collision for platforms at different heights. Overall, This project establishes a basic framework that could be expanded into a small platformer or atmospheric piece.


### Resources used to research