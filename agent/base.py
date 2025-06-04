from memory.sqlite_memory import SQLiteMemory

class Agent:
    def __init__(self, name, analyzer):
        self.name = name
        self.analyzer = analyzer
        self.memory = SQLiteMemory()

    def receive_task(self, task, status="completed"):
        print(f"[{self.name}] Received task: {task}")
        tool_func = self.analyzer.identify_tool(task)
        if tool_func:
            result = tool_func(task)
            print(f"[{self.name}] Result: {result}")
        else:
            result = "No result"
            print(f"[{self.name}] No tool found for this task.")
            if status == "completed":
                status = "failed"
        self.memory.save_task(task, result, status)


    def show_memory(self):
        records = self.memory.get_all_tasks()
        print(f"\n[{self.name}] Memory:")
        for r in records:
            print(f"- Task: {r[0]} => Result: {r[1]} | Status: {r[3]} at {r[2]}")