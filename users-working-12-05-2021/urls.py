
from django.contrib import admin
from django.urls import path
from users.views import jobcard_pending_on_engineer, jobcard_assigned_engineer, jobcard_pending_ccn_head, user_submitted_jobcard, update_profile, profile, jobcard_view, job_card_approved, jobcard_approved, jobcard_rejected, job_card_on_user_head, add_jobcard_problem, jobcard_problem_list, jobcard_problem_deactive, jobcard_problem_edit, jobcard_problem_active, UserLogin, add_jobcard, jobcard_list, jobcard_deactive, jobcard_active, home, Dashboard, UserLogOut, MyCustomer, add_division, division_list, division_edit, division_active, division_deactive


app_name = 'users'

urlpatterns = [
    path('', home),
    #path('register/',register.as_view(), name='register'),
  

    path('dashboard/', Dashboard, name='dashboard'),
    path('profile/', profile, name='profile'),
    path('login/', UserLogin, name='login'),
    path('customer/', MyCustomer, name='customer'),
    path('logout/', UserLogOut, name='logout'),
    # path('user-registration/', UserRegistration, name='register'),
    path('register/', update_profile, name='register'),    
    path('division/add-division/',add_division, name='add_division'),
    path('division/division-list/',division_list, name='division_list'),
    path('division/division-list/<int:id>',division_edit, name='division_edit'),
    path('division/division-active/<int:id>',division_active, name='division_active'),
    path('division/division-deactive/<int:id>',division_deactive, name='division_deactive'),



    path('jobcard/add-jobcard-problem/',add_jobcard_problem, name='add-jobcard-problem'),
    path('jobcard/jobcard-problem-list/',jobcard_problem_list, name='jobcard-problem-list'),
    path('jobcard/jobcard-problem-list/<int:id>',jobcard_problem_edit, name='jobcard-problem-l'),
    path('jobcard/jobcard-problem-active/<int:id>',jobcard_problem_active, name='jobcard-problem-active'),
    path('jobcard/jobcard-problem-deactive/<int:id>',jobcard_problem_deactive, name='jobcard-problem-deactivate'),

    
    path('jobcard/jobcard-view/<int:id>',jobcard_view, name='jobcard_view'),
    path('jobcard/job-card-on-user-head',job_card_on_user_head, name='job-card-on-user-head'),
    path('jobcard/user-head-jobcard-approval/<int:id>',jobcard_approved, name='jobcard-approve'),
    path('jobcard/user-head-jobcard-rejected/<int:id>',jobcard_rejected, name='jobcard-rejected'),
    path('jobcard/job-card-approved',job_card_approved, name='job_card_approved'),   



    path('jobcard/add-jobcard/',add_jobcard, name='add_jobcard'),
    path('jobcard/jobcard-list/',jobcard_list, name='jobcard_list'),
    path('jobcard/jobcard-active/<int:id>',jobcard_active, name='jobcard_active'),
    path('jobcard/jobcard-deactive/<int:id>',jobcard_deactive, name='jobcard_deactive'),
    # path('jobcard/jobcard-list/<int:id>',jobcard_edit, name='jobcard_edit'),    

    # User Jobcards urls

    path('jobcard/user-submitted-jobcard', user_submitted_jobcard, name='user_submitted_jobcard'),


    # CCN Head 
    path('jobcard/jobcard-pending-ccn-head', jobcard_pending_ccn_head, name='jobcard_pending_ccn_head'),
    path('jobcard/jobcard-assigned-by-ccn-head-to-engineer/<int:id>', jobcard_assigned_engineer, name='jobcard-assigned-by-ccn-head-to-engineer'),


    # Engineer

    path('jobcard/jobcard-pending-on-engineer', jobcard_pending_on_engineer, name='jobcard_pending_on_engineer'),

    





]
