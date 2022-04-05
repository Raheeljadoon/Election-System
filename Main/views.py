from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse


# Create your views here.
from .models import Votes, Candidates
from .forms import ElectionForms, CandidateForm


def elections(request):

    all_candidates = Candidates.objects.all().first()
    votes = Votes.objects.filter(
        candidate_name=all_candidates).first().no_of_votes
    print(all_candidates)

    return render(request, 'election/index.html', {'all_candidates': all_candidates, 'votes': votes})


def updates_votes(request):

    if request.method == 'POST':

        form = ElectionForms(request.POST)
        form_candidate = CandidateForm(request.POST)

        if form:
            if form.is_valid():
                form.save()
        elif form_candidate:
            if form_candidate.is_valid():
                form_candidate.save()
        

    else:
        form = ElectionForms()
        form_candidate = CandidateForm()

    return render(request, 'election/index.html', {'form': form, 'formscandidate': form_candidate})


def register(request):

    form_candidate = CandidateForm(request.POST)
    if request.method == 'POST':
        
        if form_candidate.is_valid():
            form_candidate.save()

    return render(request, 'election/register.html', {'formscandidate': form_candidate})