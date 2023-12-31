from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver


class Division(models.Model):
    division_name = models.CharField(max_length=50, blank=True, null=True)
    status = models.BooleanField(default=True)

    class Meta: 
        verbose_name = 'Division'
        verbose_name_plural = 'Divisions'

    def __str__(self):
        return self.division_name




class User(AbstractUser):
    is_hod = models.BooleanField(default=False)
    is_ccn_hod = models.BooleanField(default=False)
    is_engineer = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)
    division_name = models.ForeignKey(Division, on_delete=models.CASCADE, null=True, blank=True)



class Profile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)

    # def __str__(self):
    #     return self.user.username    



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()














# class User(AbstractUser):
# 	is_hod = models.BooleanField(default=False)
# 	is_ccn_hod = models.BooleanField(default=False)
# 	is_engineer = models.BooleanField(default=False)
# 	is_user = models.BooleanField(default=True)
# 	first_name = models.CharField(max_length=100, blank=True, null=True)
# 	last_name = models.CharField(max_length=100, blank=True, null=True)


# class UserProfile(models.Model):
# 	user = models.OneToOneField(User, on_delete=models.CASCADE)
# 	address = models.CharField(max_length=100, blank=True, null=True)
# 	def __str__(self):
# 		return self.user.username

# class Employee(models.Model):
#     username = models.CharField(max_length=150)
#     password = models.CharField(max_length=100)
#     first_name = models.CharField(max_length=150)
#     last_name = models.CharField(max_length=150)
#     email= models.EmailField(max_length=254)
#     division_name = models.ForeignKey(Division, on_delete=models.CASCADE) 
#     status = models.BooleanField(default=False)

#     class Meta:
#         verbose_name = "Employee"
#         verbose_name_plural = "Employee"

#     def __str__(self):
#         return("{} {}".format(self.first_name, self.last_name))



# class Accounts(models.Model):
# 	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
# 	name = models.CharField(max_length=200, null=True)
# 	phone = models.CharField(max_length=200, null=True)
# 	email = models.CharField(max_length=200, null=True)
# 	profile_pic = models.ImageField(default="profile1.png", null=True, blank=True)
# 	date_created = models.DateTimeField(auto_now_add=True, null=True)

# 	def __str__(self):
# 		return self.name


# class User(AbstractUser):
# 	is_hod = models.BooleanField(default=False)
# 	is_ccn_hod = models.BooleanField(default=False)
# 	is_engineer = models.BooleanField(default=False)
# 	is_user = models.BooleanField(default=True)
# 	first_name = models.CharField(max_length=100, blank=True, null=True)
# 	last_name = models.CharField(max_length=100, blank=True, null=True)







class CcnJobCard(models.Model):
    jobcard_on = (
		("User Head", "User Head"),
		("CCN Head", "CCN Head"),
		("Engineer", "Engineer"),
		("Cutomer", "Cutomer")
    )
    
    user_no = models.CharField(max_length=10, blank=True)
    type_of_problem = models.CharField(max_length=200, null=True)
    sr_no = models.CharField(max_length=30, null=True)
    model_no = models.CharField(max_length=200, null=True)
    status = models.BooleanField(default=False)
    job_on = models.CharField(max_length=10, choices=jobcard_on, blank=True, default= 'User Head' )
    error_pic = models.ImageField(default="default.png", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    forwareded_to_ccn_head_date = models.DateTimeField(null=True, blank=True)
    ccn_head_to_engg_date = models.DateTimeField(auto_now_add=False, null=True)
    engg_task_complete_date = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.type_of_problem


# class Profiles(models.Model):
# 	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
# 	name = models.CharField(max_length=200, null=True)
# 	phone = models.CharField(max_length=200, null=True)
# 	division = models.CharField(max_length=20, null=True)
# 	email = models.CharField(max_length=200, null=True)
# 	profile_pic = models.ImageField(default="default.png", null=True, blank=True)
# 	date_created = models.DateTimeField(auto_now_add=True, null=True)

# 	def __str__(self):
# 		return self.name





class ProblemCategory(models.Model):
    problem_name = models.CharField(max_length=50)
    status = models.BooleanField(default=True)

    class Meta: 
        verbose_name = 'ProblemCategory'
        verbose_name_plural = 'ProblemCategory'

    def __str__(self):
        return self.problem_name

