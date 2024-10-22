
# 🧠 Daily Planner AI

Welcome to **Daily Planner AI** – your personal AI assistant to help you plan your day effectively! Whether you need to organize tasks by priority, check your progress, or save your plan for the day, this AI-powered planner has got you covered!

## 🚀 Features
- **Add Tasks**: Organize tasks by priority and duration. Choose your priority level (High, Medium, Low) easily.
- **Generate Daily Plan**: Input the available time, and the AI will create a daily plan based on task priorities and duration.
- **Check Task Progress**: Track your progress by marking tasks as completed or not.
- **Save Plan to File**: Export your daily plan to a JSON file and access it anytime.

## 🛠️ How It Works

1. **Add a Task**: Provide a task name, select the priority (1 for high, 2 for medium, 3 for low), and specify the task duration in minutes.
2. **Generate Plan**: Input the total time you have for the day, and the AI will arrange tasks for you based on the time available.
3. **Check Progress**: At the end of the day, review and mark tasks as completed to see your productivity.
4. **Save Your Plan**: Optionally save the plan to a file for later reference.

## 📂 Files

- `main.py` – The main Python script that runs the AI-based daily planner.
- `tests.py` – Unit tests to ensure the planner works correctly.
- `README.md` – This file, explaining the project.

## 📖 Usage

### 1. Clone the Repository

```bash
git clone https://github.com/Elmoumen202a/Python-Projects.git
cd daily_planner_AI
```

### 2. Run the Planner

```bash
python main.py
```

### 3. Interact with the AI

Follow the prompts:

```bash
🧠 Welcome to Daily Planner AI!
1️⃣ Add a Task
2️⃣ Generate Daily Plan
3️⃣ Check Task Progress
4️⃣ Exit
```

### Example Interaction

```bash
Please choose an option (1-4): 1
📌 What's the task name? Finish Python project
🔥 Priority (1=high, 2=medium, 3=low)? 1
⏳ How many minutes will it take? 90
✅ Task 'Finish Python project' added!
```

### 4. Test the Project (Optional)

Run unit tests to ensure everything works as expected:

```bash
python tests.py
```

## 🧪 Example Output

After generating your daily plan:

```bash
📅 Here’s your daily plan:
- Finish Python project (90 minutes)
- Study German (45 minutes)
```

You can also check your progress and save your plan:

```bash
💾 Would you like to save the plan to a file? (yes/no) yes
✅ Daily plan saved to daily_plan.json
```

## 🚩 Future Features
- 🌟 **Interactive Chatbot**: Have a conversation with the AI to refine tasks and plans.
- 📊 **Task Analytics**: Track performance over days or weeks and get insights on productivity trends.

## 🤝 Contributing

Feel free to fork the repository, create a branch, and submit a pull request! We welcome all contributions to make the Daily Planner AI even better.
