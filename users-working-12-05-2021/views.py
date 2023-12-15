import hashlib
from datetime import datetime
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth  import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, admin_only

from .forms import UserForm, ProfileForm

# Create your views here.


def profile(request):
    return render(request, 'profile.html')


def update_profile(request):
    division_list = Division.objects.all().order_by('division_name')
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        print("hi")
        if user_form.is_valid() and profile_form.is_valid():
            print("hi")
            user_form.save()
            print("hi")
            profile_form.save()
            print("hi")
            messages.info(request, 'Registered Successfully :)')
            print("hi")
            return redirect('users:login')
        else:
            messages.info(request, 'Username or Password is incorrect !!')
    else:
        user_form = UserForm()
        profile_form = ProfileForm()
    return render(request, 'register.html', {
        'user_form': user_form,
        'division_list':division_list,
        'profile_form': profile_form
    })





# def registration_view(request):

#     division_list = Division.objects.all().order_by('division_name')
#     if request.method == 'POST':
#         username = request.POST['username']
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         email = request.POST['email']
#         division_nameId = int(request.POST['division_name'])

#         division_name = Division.objects.get(id=division_nameId)

#         #encripted_pass = hashlib.md5(user_password.encode())
#         #password = encripted_pass.hexdigest() 
#         username_check = User.objects.filter(username =username ) 
#         email_check = User.objects.filter(email =email) 
#         if username_check.exists():
#             messages.error(request, "Username already exists")
#         elif email_check.exists():
#             messages.error(request, "Email already exists")
#         else:
#             messages.error(request, "Email already exists")
#             user = User.objects.create(username=username, password1=password1, password2=password2, first_name=first_name,last_name=last_name, email= email)
#             messages.success(request, "Signup Completed. Please check your email to Activate your account.")
#             return redirect('users:login')
            
#     context = {
#         'division_list':division_list
#     }
#     return render(request,'register.html',context)



# class register(CreateView):
#     model = User
#     form_class = CustomerSignUpForm
#     template_name = 'register.html'
    

#     def get_context_data(self, **kwargs):
#         context = super(register, self).get_context_data(**kwargs)
#         context['division'] = Division.objects.all()
#         return context


#     def form_valid(self, form):
#         user = form.save()
#         return redirect('/login/')

# class employee_register(CreateView):
#     model = User
#     form_class = EmployeeSignUpForm
#     template_name = 'mytemplates/employee_register.html'

#     def form_valid(self, form):
#         user = form.save()
#         login(self.request, user)
#         return redirect('/')









@unauthenticated_user
def UserLogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/dashboard/')
        else:
            messages.info(request, 'Username or Password is incorrect !!')

    return render(request, 'login.html')

def UserLogOut(request):
    logout(request)
    return redirect('/login/')    

def MyCustomer(request):
    return render(request, 'customer.html')


# @unauthenticated_user
# def UserRegistration(request):
#     form = CreateUserForm()
#     if request.method =='POST':
#         form = CreateUserForm(request.POST)
#         if form.is_valid():
#             user = form.save()
            
#             username = form.cleaned_data.get('username')
#             messages.success(request, 'Registered Successfully ! ' + username)
#             return redirect('/login/')
    
#     context = {'form':form}
#     return render(request, 'registration.html', context)

@admin_only
def home(request):
    return render(request, 'index.html')

@login_required
def Dashboard(request):
    return render(request, 'dashboard.html')



@login_required
def add_division(request):
    if request.method == 'POST':
        division = request.POST['division'] 
        Division.objects.create(division_name=division)
        messages.success(request, "division Added Successfully")
    return render(request,'admin/add_division.html')


@login_required
def division_list(request):
    division_list = Division.objects.all().order_by('division_name')
    context = {
        'division_list':division_list
    }
    return render(request, 'admin/division_list.html',context)

@login_required
def division_edit(request, id):
    division = Division.objects.filter(id = id) 
    old_name = division[0].division_name
    if request.method == 'POST':
        division_name = request.POST['division']
        division.update(division_name = division_name)  
        messages.success(request, "division updated uccessfully")
        return redirect("users:division_list") 
    context = {
        'division_name':old_name
    }
    return render(request,'admin/edit_division.html',context)

@login_required
def division_active(request, id):
    division = Division.objects.get(id = id)
    division.status = True
    division.save() 
    messages.success(request, "division status changed uccessfully")
    return redirect("users:division_list") 


@login_required
def division_deactive(request, id):
    division = Division.objects.get(id = id)
    division.status = False
    division.save() 
    messages.success(request, "division status changed uccessfully")
    return redirect("users:division_list")







@login_required
def add_jobcard(request):
    if request.method == 'POST':
        type_of_problem = request.POST['type_of_problem']
        sr_no = request.POST['sr_no']
        model_no = request.POST['model_no']
        user_no = request.user.id
        CcnJobCard.objects.create(user_no=user_no, type_of_problem=type_of_problem, sr_no=sr_no, model_no=model_no)
        messages.success(request, "JobCard Added Successfully")
    return render(request,'jobcard/add_jobcard.html')


@login_required
def jobcard_list(request):
    jobcard_list = CcnJobCard.objects.all().order_by('model_no')
    context = {
        'jobcard_list':jobcard_list
    }
    return render(request, 'jobcard/jobcard_list.html',context)

# @login_required
# def jobcard_edit(request, id):
#     jobcard = CcnJobCard.objects.filter(id = id) 
#     old_name = jobcard[0].jobcard_name
#     if request.method == 'POST':
#         division_name = request.POST['division']
#         division.update(division_name = division_name)  
#         messages.success(request, "jobcard updated uccessfully")
#         return redirect("users:jobcard_list") 
#     context = {
#         'jobcard_name':old_name
#     }
#     return render(request,'admin/edit_jobcard.html',context)


@login_required
def jobcard_active(request, id):
    jobcard = CcnJobCard.objects.get(id = id)
    jobcard.status = True
    jobcard.save() 
    messages.success(request, "jobcard status changed uccessfully")
    return redirect("users:jobcard_list") 


@login_required
def jobcard_deactive(request, id):
    jobcard = CcnJobCard.objects.get(id = id)
    jobcard.status = False
    jobcard.save() 
    messages.success(request, "jobcard status changed uccessfully")
    return redirect("users:jobcard_list")    



@login_required
def add_jobcard_problem(request):
    if request.method == 'POST':
        problem_name = request.POST['problem_name']
        ProblemCategory.objects.create(problem_name=problem_name)
        messages.success(request, "Type of Problem Added Successfully")
    return render(request,'admin/add_jobcard_problem.html')


@login_required
def jobcard_problem_list(request):
    p_list = ProblemCategory.objects.all()
    context = {
        'p_list':p_list
    }
    return render(request, 'admin/jobcard_problem_list.html',context)

@login_required
def jobcard_problem_edit(request, id):
    jobcard = ProblemCategory.objects.filter(id = id) 
    old_name = jobcard[0].jobcard_name
    if request.method == 'POST':
        division_name = request.POST['division']
        division.update(division_name = division_name)  
        messages.success(request, "jobcard updated uccessfully")
        return redirect("users:jobcard_list") 
    context = {
        'jobcard_name':old_name
    }
    return render(request,'admin/jobcard_problem_edit.html',context)



@login_required
def jobcard_problem_active(request, id):
    jobcard = ProblemCategory.objects.get(id = id)
    jobcard.status = True
    jobcard.save() 
    messages.success(request, "Type of Problem status changed successfully")
    return redirect("users:jobcard-problem-list") 


@login_required
def jobcard_problem_deactive(request, id):
    jobcard = ProblemCategory.objects.get(id = id)
    jobcard.status = False
    jobcard.save() 
    messages.success(request, "Type of Problem status changed successfully")
    return redirect("users:jobcard-problem-list")











@login_required
def job_card_on_user_head(request):
    j_list = CcnJobCard.objects.filter(job_on="User Head")
    context = {
        'j_list':j_list
    }
    return render(request,'jobcard/job-card-on-user-head.html',context) 




@login_required
def jobcard_approved(request, id):
    job = CcnJobCard.objects.get(id = id)
    job.job_on = 'CCN Head'
    job.forwareded_to_ccn_head_date = timezone.now()
    job.save() 
    messages.success(request, "Jobcard Approved & forwarded to CCN HEAD successfully !!")
    return redirect("users:job-card-on-user-head")


@login_required
def jobcard_rejected(request, id):
    job = CcnJobCard.objects.get(id = id)
    job.status = True
    job.save() 
    messages.success(request, "Jobcard rejected !!")
    return redirect("users:job-card-on-user-head")
    
@login_required
def job_card_approved(request):
    approved_list = CcnJobCard.objects.all()
    context = {
        'approved_list':approved_list
        }
    return render(request, 'jobcard/jobcard_approved_list.html',context)


@login_required
def jobcard_view(request, id):
    job_view = CcnJobCard.objects.get(id=id)
    context = {
        'job_view':job_view
    }    
    return render(request, 'jobcard/jobcard-view.html',context)




# User Jobcard views

@login_required
def user_submitted_jobcard(request):
    idd = request.user.id
    user_jobcard_list = CcnJobCard.objects.filter(user_no=idd)
    context = {
        'user_jobcard_list':user_jobcard_list
    }
    return render(request,'jobcard/user-submitted-jobcard.html',context) 




# CCN Head 


@login_required
def jobcard_pending_ccn_head(request):
    engineer_list = User.objects.filter(is_engineer=True)
    user_jobcard_list = CcnJobCard.objects.filter(job_on="CCN Head")
    context = {
        'engineer_list':engineer_list,
        'p_ccn_jobcard_list':user_jobcard_list
    }
    return render(request,'jobcard/jobcard-pending-ccn-head.html',context) 



@login_required
def jobcard_assigned_engineer(request, id):
    jobc = CcnJobCard.objects.get(id = id)
    jobc.job_on = 'Engineer'
    jobc.ccn_head_to_engg_date = timezone.now()
    jobc.save() 
    messages.success(request, "Jobcard forwarded to an engineer !!")
    return redirect("users:jobcard_pending_ccn_head")




# Engineer    


@login_required
def jobcard_pending_on_engineer(request):
    pending_to_engineer = CcnJobCard.objects.filter(job_on="Engineer")
    context = {
        'pending_to_engineer':pending_to_engineer
    }
    return render(request,'jobcard/jobcard-pending-on-engineer.html',context) 