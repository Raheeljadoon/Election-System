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
    namelist = []
    candidate_vote = []

    form = ElectionForms(request.POST)
    total_votes = Votes.objects.all()
    for name in total_votes :

        namelist.append(name.candidate_name.name)
        candidate_vote.append(name.no_of_votes)
        # candidate_vote = name.no_of_votes


    if request.method == 'POST':

        # total_votes = Votes.objects.all()

        try:
            no_of_votes = Votes.objects.filter(candidate_name=int(form.data['candidate_name'])).first().no_of_votes

            after_addition = no_of_votes + int(form.data['no_of_votes']) 


            update_votes = Votes.objects.filter(candidate_name=form.data['candidate_name']).update(no_of_votes=after_addition)
            print(update_votes)
        except Exception as ex:
            print(ex)

    return render(request, 'election/index.html', {'form': form,'total_votes':total_votes,"namelist":namelist,"canditate_vote":candidate_vote})


def register(request):

    form_candidate = CandidateForm(request.POST)
    if request.method == 'POST':

        if form_candidate.is_valid():
            form_candidate.save()

    return render(request, 'election/register.html', {'formscandidate': form_candidate})


def submit(request):

    print("yes i am here")
    if request.method == 'POST':
        print(request.POST)
        candidate_name = request.POST['candidate_name']
        votes = request.POST['votes']

        # total_votes = Votes.objects.all()

        try:
            candidate_id = Candidates.objects.filter(name=candidate_name).first().id
            
            no_of_votes = Votes.objects.filter(candidate_name=int(candidate_id)).first().no_of_votes

            after_addition = no_of_votes + int(votes) 


            update_votes = Votes.objects.filter(candidate_name=int(candidate_id)).update(no_of_votes=after_addition)
            print(update_votes)
        except Exception as ex:
            print(ex)

    return render(request,'election/index.html') 