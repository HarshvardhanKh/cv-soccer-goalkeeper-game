# ⚽ Computer Vision Soccer Goalkeeper Game  

An **interactive computer vision–based soccer game** built with **Python, OpenCV, and Mediapipe** where you play as a **virtual goalkeeper** using just your body movements tracked via webcam. The project also features a **Tkinter startup GUI** and a **MySQL-powered leaderboard** to make gameplay engaging and competitive.  

---

## 🎮 Gameplay Overview
- The game starts with a countdown timer.  
- A soccer ball is shot toward random positions in the goal.  
- Move your body (tracked via webcam) to block the ball.  
- Each successful save increases your score; missed saves add mistakes.  
- Game ends when you miss 3 shots (Lose screen) or achieve enough saves (Win screen).  
- After finishing, enter your name to save your score to the leaderboard.  

---

## ✨ Features
- 🖥️ **Hands-free Gameplay** – Control using body movements (pose detection).  
- 🎯 **Penalty Shootout Mechanism** – Randomized ball direction with increasing difficulty.  
- 📊 **Leaderboard System** – Stores and displays top scores using MySQL.  
- 🎨 **Graphics Overlay** – Ball, goalkeeper, win/lose banners via `cvzone`.  
- ⚡ **Real-time Performance** – FPS counter for smooth gameplay.  
- 🖼️ **Startup Menu** – Tkinter GUI to play game or refresh leaderboard.  

---

## 🛠️ Tech Stack
- **Python 3**  
- **OpenCV** – Video processing  
- **Mediapipe** – Pose estimation  
- **cvzone** – Overlay images on frames  
- **Tkinter** – GUI menu and leaderboard  
- **MySQL** – Score storage and retrieval  
- **Pillow (PIL)** – Image processing for GUI  

---

## 📂 Project Structure

📦 CV-Soccer-Goalkeeper-Game
 - 📜 GameProj.py       # Main game logic (OpenCV + Mediapipe + cvzone)
 - 📜 rUN.py            # Tkinter startup GUI + leaderboard integration
 - 📜 SoccerGame.py     # Game runner script (called from GUI)
 - 📜 BG1.png           # Game background
 - 📜 soccerBall.png    # Ball sprite
 - 📜 goalkeeper.png    # Goalkeeper sprite
 - 📜 Winning.png       # Win screen
 - 📜 Losing.png        # Lose screen
 - 📜 correct.png       # Correct save indicator
 - 📜 wrong.png         # Missed save indicator
 - 📜 README.md         # Documentation

