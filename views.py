from django.http import HttpResponse

def main(request):
    return HttpResponse("root")

def home(request):
    return HttpResponse("home page")

def about(request):
    return HttpResponse("about page")

def contact(request):
    return HttpResponse("contact page")

def login(request):
    form = """
        <form method="post">
            <input type="text" name="username" placeholder="Username"><br>
            <input type="password" name="password" placeholder="Password"><br>
            <button type="submit">Login</button>
        </form>
    """
    return HttpResponse(form)

def regiter(request):
    form = """
        <form method="post">
            <input type="text" name="username" placeholder="Username"><br>
            <input type="password" name="password" placeholder="Password"><br>
            <input type="password" name="confirm_password" placeholder="Confirm Password"><br>
            <input type="email" name="email" placeholder="Email"><br>
            <button type="submit">Register</button>
        </form>
        """
    
    return HttpResponse(form)

def profile(request):
    return HttpResponse("profile page")

def calculate(request, num1, num2, oper):
    if oper == 'plus':
        answer = num1 + num2
        return HttpResponse(answer)
    if oper == 'minus':
        answer = num1 - num2
        return HttpResponse(answer)
    if oper == 'multiply':
        answer = num1 * num2
        return HttpResponse(answer)
    if oper == 'divade':
        answer = num1 / num2
        return HttpResponse(answer)
    
def write_calculation_form(num1, num2, oper):
    form = f"""
        <form method="get">
            <input type="number" name="num1" value="{num1}" placeholder="First Number"><br>
            <input type="number" name="num2" value="{num2}" placeholder="Second Number"><br>
            <select name="oper">
                <option value="plus">+</option>
                <option value="minus">-</option>
                <option value="multiply">x</option>
                <option value="divade">÷</option>
            </select><br>
            <button type="submit">Calculate</button>
        </form>
    """
    return form

def calculate_query(request):
    num1 = int(request.GET.get('num1'))
    num2 = int(request.GET.get('num2'))
    oper = request.GET.get('oper')
    
    if oper == 'plus':
        answer = num1 + num2
        return HttpResponse(answer)
    if oper == 'minus':
        answer = num1 - num2
        return HttpResponse(answer)
    if oper == 'multiply':
        answer = num1 * num2
        return HttpResponse(answer)
    if oper == 'divade':
        answer = num1 / num2
        return HttpResponse(answer)