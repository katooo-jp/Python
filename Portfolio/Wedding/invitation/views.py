from django.shortcuts import redirect, render
from django.views import View
from .forms import RsvpFrom
from .models import Rsvp

params = {
  'form': RsvpFrom()
}

class InvitationView(View):
  def get(self, request, *args, **kwargs):
    return render(request, 'invitation/index.html', params)

  def post(self, request, *args, **kwargs):
    form = RsvpFrom(request.POST)
    params['form'] = form
    params['guest'] = request.POST.get('guest')
    params['name'] = request.POST.get('name')
    params['furi'] = request.POST.get('furi')
    params['tel'] = request.POST.get('tel')
    params['mail'] = request.POST.get('mail')
    params['post'] = request.POST.get('post')
    params['address'] = request.POST.get('address')
    params['bus'] = request.POST.get('bus')
    params['message'] = request.POST.get('message')
    params['allergy'] = request.POST.get('allergy')
    params['conpanion1'] = request.POST.get('conpanion1') + ' 様'
    params['conpanion2'] = request.POST.get('conpanion2') + ' 様'
    params['conpanion3'] = request.POST.get('conpanion3') + ' 様'
    params['attendance'] = request.POST.get('attendance')
    
    if form.is_valid():
      return redirect('check')
    else:
      return render(request, 'invitation/index.html', params)



class CheckView(View):
  def get(self, request, *args, **kwargs):
    return render(request, 'invitation/check.html', params)

  def post(self, request, *args, **kwargs):
    rsvp = Rsvp(guest=params['guest'], name=params['name'], furi=params['furi'],
    tel=params['tel'], mail=params['mail'], post=params['post'], address=params['address'], 
    bus=params['bus'], message=params['message'], allergy=params['allergy'], conpanion1=params['conpanion1'], 
    conpanion2=params['conpanion2'], conpanion3=params['conpanion3'], attendance=params['attendance'])
    rsvp.save()
    params['form'] = RsvpFrom()
    return redirect('invitation')



invitation = InvitationView.as_view()
check = CheckView.as_view()