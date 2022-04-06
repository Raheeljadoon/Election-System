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

    form = ElectionForms(request.POST)
    votes = Votes.objects.all().first()

    if request.method == 'POST':

        if form.is_valid():

            # form.save()
            print(form)
            no_of_votes = Votes.objects.filter(candidate_name=int(form.data['candidate_name'])).first().no_of_votes

            after_addition = no_of_votes + int(form.data['no_of_votes']) 


            update_votes = Votes.objects.filter(candidate_name=form.data['candidate_name']).update(no_of_votes=after_addition)
            print(update_votes)


    return render(request, 'election/index.html', {'form': form})


def register(request):

    form_candidate = CandidateForm(request.POST)
    if request.method == 'POST':

        if form_candidate.is_valid():
            form_candidate.save()

    return render(request, 'election/register.html', {'formscandidate': form_candidate})
