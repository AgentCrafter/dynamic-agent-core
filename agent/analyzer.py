from tools import file_ops

tool_map = {
    "copy": file_ops.copy_file,
    "backup": file_ops.copy_file,
}

class Analyzer:
    def identify_tool(self, task):
        task_lower = task.lower()
        for keyword, func in tool_map.items():
            if keyword in task_lower:
                return func
        return None
    
class SimpleAnalyzer:
    def analyze(self, task):
        from .analyzer import Analyzer
        tool_name = Analyzer().identify_tool(task)
        return tool_name, {"task": task}
