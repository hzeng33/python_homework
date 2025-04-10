# Task 1: Diary
import traceback

try:
    with open('diary.txt', 'w') as file:
        line = input("What happened today? \n ")
        while True:
            if(line == "done for now"):
                file.write(line)
                file.close
                break
            file.write(line)
            line = input("What else? \n")
except Exception as e:
   trace_back = traceback.extract_tb(e.__traceback__)
   stack_trace = list()
   for trace in trace_back:
      stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
   print(f"Exception type: {type(e).__name__}")
   message = str(e)
   if message:
      print(f"Exception message: {message}")
   print(f"Stack trace: {stack_trace}")