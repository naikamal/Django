from django.shortcuts import render
from .models import Post

# # Create your views here.
# posts=[
#     {
#         'auther':'Naik amal',
#         'title':'Django Tutorial',
#         'date_posted':'22 dec 2022',
#         'content':'As i a have make all The design By my itself By using pure css and Html since Corey used bootstrap but i am not gonna use i have just inspired from his project and i also pass dummy from veive to template and also use for loop'

#     },
#     {
#         'auther':'Raheem shah',
#         'title':'Medical Tutorial',
#         'date_posted':'04 Mar 2013',
#         'content':'My first mediacal Tutorial In which i will teach you technichian'

#     } 

# ]

def home(request):
    context={
        'posts':Post.objects.all()
    }
    return render(request,'blog/index.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'About'})
