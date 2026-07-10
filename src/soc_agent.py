from langchain_ollama import OllamaLLM

# 1. إعداد الـ Brain
llm = OllamaLLM(model="llama3")

# 2. قراءة ملف اللوج الحقيقي (تأكد إن الملف موجود في نفس الفولدر)
try:
    with open("system.log", "r") as f:
        log_content = f.read()
except FileNotFoundError:
    print("Error: system.log file not found!")
    exit()

# 3. الـ System Prompt (بنمرر له log_content اللي قريناه من الملف)
prompt = f"""
You are an expert SOC Analyst. Analyze the logs provided below and:
1. Identify the type of attack (e.g., Brute Force, Path Traversal, SQL Injection).
2. Determine the Severity (Low, Medium, High, Critical).
3. Provide a brief "Action Plan" for the analyst.

Logs to analyze:
{log_content}

Analysis:
"""

# 4. تشغيل الـ AI وطباعة النتيجة
print("--- AI Agent is analyzing the logs... ---")
response = llm.invoke(prompt)
print(response)
