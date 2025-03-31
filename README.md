![photo](https://github.com/user-attachments/assets/db30ba15-db2f-4708-9235-1e5936649950)🚀 **Ping Pong Game with Hand Detection – Real-Time Control Using OpenCV & cvzone**

This project is an interactive **Ping Pong game** built using **Python**, **OpenCV**, and **cvzone**, where players control the bats with **hand gestures** instead of a keyboard or mouse. The game offers a fun and intuitive experience with **real-time hand tracking** and dynamically increasing ball speed, making it both challenging and engaging. 🎯



🏓 **Ping Pong Game Using Hand Detection**

📊 **Project Overview**
This project is a **hand-gesture-controlled Ping Pong game** using **OpenCV**, **cvzone**, and **HandDetector**. The game uses your webcam to detect hand movements, allowing you to control the paddles with gestures. The ball speed dynamically increases as both players' scores hit multiples of 5, making the game progressively more challenging.

🚀 **Features**
- 🎯 **Real-time Hand Tracking:** Control the paddles with hand gestures using cvzone's HandDetector.
- ⚡ **Dynamic Speed:** Ball speed increases by **+3 units** in both X and Y directions every time both players' scores are multiples of 5.
- 🎥 **Webcam Integration:** Uses a live webcam feed for an interactive experience.
- 🛑 **Pause and Resume:** Press `P` to pause/resume the game.
- 🔄 **Restart:** Press `R` to restart the game.
- 🎉 **Game Over Screen:** Displays the winner and final scores.

## 🛠️ **Technologies Used**
- Python
- OpenCV
- cvzone
- NumPy

## 📁 **Folder Structure**
```
📂 Resources
 ├── Background.png        # Game background image
 ├── gameOver.png          # Game over screen
 ├── Ball.png              # Ball image
 ├── bat1.png              # Player 1 paddle
 ├── bat2.png              # Player 2 paddle
📄 ping_pong.py             # Main game file
📄 README.md                # Project documentation
📄 requirements.txt         # Dependencies
```

## ▶️ **How to Run**
1. Clone the repository:
   ```bash
   git clone <your-github-repo-link>
   ```

2. Install the required libraries:
   ```bash
   pip install opencv-python cvzone numpy
   ```

3. Run the game:
   ```bash
   python ping_pong.py
   ```

## 🎯 **Game Controls**
- `P` → Pause/Resume the game.
- `R` → Restart the game.
- `Esc` or close window → Exit the game.

## ⚙️ **Game Logic**
- **Hand Detection:** Uses `cvzone.HandDetector()` to track hand positions and control the paddles.
- **Collision Detection:** The ball bounces off the paddles and walls.
- **Speed Increase:** Ball speed increases by **+3 units** in both directions every time **both players’ scores** reach multiples of 5.
- **Game Over:** The game ends if the ball passes a paddle, and the winner is displayed.

## 🎥 **Preview**



https://github.com/user-attachments/assets/d0d4d823-3041-4883-af21-95993f5884f3


## 💡 **Future Enhancements**
- Add **sound effects** for collisions and game-over events.
- Introduce **AI opponent** mode for single-player gameplay.
- Include a **scoreboard** with top scores.

## 🤝 **Contributions**
Contributions and suggestions are welcome! Feel free to fork, create issues, or submit pull requests.

## 📄 **License**
This project is licensed under the MIT License.

---


