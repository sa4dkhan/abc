from django.shortcuts import render, redirect
from .models import Lawyer
from dashboard.models import Client
from django.shortcuts import render
from .forms import SearchForm
# import operator
# from django.db.models import Q
from .forms import LawyerForm
# from django.http import HttpResponseRedirect

# Create your views here.


# @render('search.html')
def search(request):
    form = SearchForm(request.GET or {})
    if form.is_valid():
        results = form.get_queryset()
    else:
        results = Lawyer.objects.none(), Client.objects.none()
    return render(request, 'search.html', {'form': form, 'results': results})
    # return {
    #     'form': form,
    #     'results': results,
    # }


def index(request):
    return render(request, 'lawyer/lawyer-home.html')


def create_lawyer(request):
    return render(request, 'lawyer/create_lawyer.html')


def store_lawyer(request):
    if request.method == "POST":
        data = Lawyer.objects.create()
        data.lawyer_pic = request.FILES['lawyer_pic']
        data.first_name = request.POST['first_name']
        data.last_name = request.POST['last_name']
        data.speciality = request.POST['speciality']
        data.mobile_number = request.POST['mobile_number']
        data.email_address = request.POST['email_address']
        data.save()
        return redirect('create_lawyer')


def lawyer_list(request):
    lawyer = Lawyer.objects.all()
    return render(request, 'lawyer/lawyer_list.html', {'lawyer': lawyer})


def view_lawyer_update(request, id):
    lawyer = Lawyer.objects.get(id=id)
    form = LawyerForm(request.POST or None, instance=lawyer)

    if form.is_valid():
        form.save()
        return redirect('lawyer_list')

    return render(request, 'lawyer/update-lawyer.html', {'form': form, 'lawyer': lawyer})


def delete_lawyer(request, id):

    try:
        results = Lawyer.objects.get(id=id).delete()
        return HttpResponse('success')
    except Exception as e:
        return redirect('lawyer_list')


def update_form_action_lawyer(request,id):
    lawyer = Lawyer.objects.get(id=id)
    form = LawyerForm(request.POST or None, instance=lawyer)
    if request.method == "POST":
        lawyer.lawyer_pic = request.FILES['lawyer_pic']
        lawyer.first_name = request.POST['first_name']
        lawyer.last_name = request.POST['last_name']
        lawyer.speciality = request.POST['speciality']
        lawyer.mobile_number = request.POST['mobile_number']
        lawyer.email_address = request.POST['email_address']
        lawyer.save()
        return redirect('lawyer_list')

    return render(request, 'lawyer/update-lawyer.html', {'form': form, 'lawyer': lawyer})



# class BlogSearchListView(BlogListView):
#     """
#     Display a Blog List page filtered by the search query.
#     """
#     paginate_by = 10
#
#     def get_queryset(self):
#         result = super(BlogSearchListView, self).get_queryset()
#
#         query = self.request.GET.get('q')
#         if query:
#             query_list = query.split()
#             result = result.filter(
#                 reduce(operator.and_,
#                        (Q(title__icontains=q) for q in query_list)) |
#                 reduce(operator.and_,
#                        (Q(content__icontains=q) for q in query_list))
#             )
#
#         return result
