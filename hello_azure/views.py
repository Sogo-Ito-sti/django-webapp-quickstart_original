from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from hello_azure.utils import decode_id_token

def index(request):
    # Azure から提供されるヘッダーから ID トークンを取得
    id_token = request.META.get('HTTP_X_MS_TOKEN_GOOGLE_ID_TOKEN')
    if id_token:
        # user_id = id_token
        user_id = decode_id_token(id_token)
    else:
        user_id = 'None'
        
    context = {'user_id': user_id}
    print('Request for index page received')
    return render(request, 'hello_azure/index.html', context)

@csrf_exempt
def hello(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        
        if name is None or name == '':
            print("Request for hello page received with no name or blank name -- redirecting")
            return redirect('index')
        else:
            print("Request for hello page received with name=%s" % name)
            context = {'name': name }
            return render(request, 'hello_azure/hello.html', context)
    else:
        return redirect('index')
