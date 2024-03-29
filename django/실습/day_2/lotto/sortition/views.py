from django.shortcuts import render
import random
# Create your views here.

def draw(request): 

    number1 = random.sample(range(1,46),6)
    number2 = random.sample(range(1,46),6)
    number3 = random.sample(range(1,46),6)
    number4 = random.sample(range(1,46),6)
    number5 = random.sample(range(1,46),6)


    context = {
        'number1': number1,
        'number2': number2,
        'number3': number3,
        'number4': number4,
        'number5': number5,
        
    }
    return render(request,'draw.html',context)

def version2(request):
    
    number_list = []
    
    for _ in range(5):
        number = random.sample(range(1,46),6)
        number_list.append(number)
    
    context = {
        'lotto': number_list,
    }
    
    return render(request, 'version2.html',context)