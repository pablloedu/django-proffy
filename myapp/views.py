from django.shortcuts import render
from .models import Proffy
import json


with open("templates/static/estados_cidades.json", 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)

weekdays = ['Segunda-Feira','Terça-Feira','Quarta-Feira','Quinta-Feira','Sexta-Feira','Sábado', 'Domingo']
subjects = ['Matemática', 'Física', 'Química', 'Biologia', 'História do Brasil', 'História Geral', 'Geografia', 'Filosofia e Sociologia', 'Literatura', 'Língua Portuguesa', 'Artes', 'Inglês', 'Espanhol']
# Create your views here.

def index(request):
    return render(request, 'myapp/index.html')


def study(request):

    proffys = Proffy.objects.order_by('fullName').filter(show=False)

    return render(request, 'myapp/study.html', {
        'proffys': proffys,
        'weekdays': weekdays,
        'subjects': subjects,
        'dados': dados
    })

def giveClasses(request):
    proffys = Proffy.objects.all()

    if request.method == 'POST':
        fullName = request.POST['fullName']
        whatsapp = request.POST['whatsapp']
        email = request.POST['email']
        bio = request.POST['bio']
        time_from = request.POST['time_from']
        cost = request.POST['cost']
        subject = request.POST['subject']
        avatar = request.POST['avatar']
        weekday = request.POST['weekday']
        estado = request.POST['estado']
        cidade = request.POST['cidade']



        Proffy(fullName=fullName, whatsapp=whatsapp, email=email, bio=bio, time_from=time_from, cost=cost, avatar=avatar, subject=subject, weekday=weekday, estado=estado, cidade=cidade ).save()
        


        return render(request, 'myapp/index.html')

    return render(request, 'myapp/give-classes.html', {
        'proffys': proffys,
        'subjects': subjects,
        'weekdays': weekdays,
        'dados': dados,

    })
    
def studyFilter(request):
    fWeekday = request.GET.get('weekday')
    fEstado = request.GET.get('estado')
    fSubject = request.GET.get('subject')

    if fSubject == "" and fWeekday=="":
        proffys = Proffy.objects.order_by('fullName').filter(show=False, estado=fEstado )
        return render(request, 'myapp/study.html', {
            'proffys': proffys,
            'weekdays': weekdays,
            'subjects': subjects,
            'dados': dados,

    })

    if fSubject == '':
        proffys = Proffy.objects.order_by('fullName').filter(weekday=fWeekday, estado=fEstado, show=False )
        return render(request, 'myapp/study.html', {
            'proffys': proffys,
            'weekdays': weekdays,
            'subjects': subjects,
            'dados': dados,

    })
    if fWeekday== '':
        proffys = Proffy.objects.order_by('fullName').filter(subject=fSubject, estado=fEstado, show=False )
        return render(request, 'myapp/study.html', {
            'proffys': proffys,
            'weekdays': weekdays,
            'subjects': subjects,
            'dados': dados,

    })
    
    proffys = Proffy.objects.order_by('fullName').filter( show=False, subject=fSubject, weekday=fWeekday, estado=fEstado,)
    return render(request, 'myapp/study.html', {
        'proffys': proffys,
        'weekdays': weekdays,
        'subjects': subjects,
        'dados': dados,

    })