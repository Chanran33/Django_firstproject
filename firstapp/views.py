from django.shortcuts import render

# Create your views here.
def welcome(request):
    return render(request, "welcome.html")

def hello(request):
    userName = request.GET['name'] #input박스안의 name이 name인 부분을 가져온다
    return render(request, 'hello.html', {'userName':userName}) #가져온 값을 render함수에 넘겨주면된다.
    #세번째 인자에 딕셔너리 자료형으로 넘겨줄 데이터를 입력하면 hello.html로 정보가 넘어가게 된다.