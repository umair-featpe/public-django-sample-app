from django.http import HttpResponse

def execute_dangerous_command(request):
    user_input = request.GET.get("cmd", "")
    result = eval(user_input)  # Unsafe eval usage
    return HttpResponse(f"Result: {result}")

def divide_numbers(request):
    a = int(request.GET.get("a", 1))
    b = int(request.GET.get("b", 0))
    result = a / b  # No error handling for division by zero
    return HttpResponse(f"Result: {result}")

def duplicate_function_1():
    print("This is duplicate code")

def duplicate_function_2():
    print("This is duplicate code")
