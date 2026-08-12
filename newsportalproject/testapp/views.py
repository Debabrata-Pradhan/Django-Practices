from django.shortcuts import render
def movies(request):
    msg='Movies Information'
    msg1='TOXIC movie by Yash is going to release on 26th August 2026.'
    msg2="I'M GAME movie by Dulquer Salman is going to release on 20th August 2026."
    msg3="SARDAR 2 By Karthi is going to release on 10th September 2026."
    type='movies'
    d={
        "msg":msg,"msg1":msg1,"msg2":msg2,"msg3":msg3,"type":type
    }
    return render(request,'testapp/index.html',d)
def sports(request):
    msg = 'Sports Information'
    msg1 = 'The FIFA World Cup draws a larger global television audience than any other single sporting event.'
    msg2 = "The Indian Premier League(IPL) ranks among the most-watched domestic sports leagues in World."
    msg3 = "Field hockey has roots stretching back to ancient eras, while ice hockey dominates North America and North Europe."
    type = 'sports'
    d = {
        "msg": msg, "msg1": msg1, "msg2": msg2, "msg3": msg3, "type": type
    }
    return render(request, 'testapp/index.html', d)
def politics(request):
    msg = 'Politics Information'
    msg1 = "The legislation grants Vande Mataram the same legal status and protection previously reserved only for the national anthem."
    msg2 = "Israeli Prime Minister Benjamin Netanyahu publicly rejected U.S. President Donald Trump's 15-point Gaza peace proposal. "
    msg3 = "The U.S. military engaged in active exchanges and targeted strikes after commercial shipping came under attack in the Strait of Hormuz. "
    type = 'politics'
    d = {
        "msg": msg, "msg1": msg1, "msg2": msg2, "msg3": msg3, "type": type
    }
    return render(request, 'testapp/index.html', d)