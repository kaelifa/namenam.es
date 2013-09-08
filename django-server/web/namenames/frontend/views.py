from django.http import HttpResponse
from django.views.generic.base import View, TemplateView
from django.template import RequestContext
from django import forms
from django.contrib.auth.models import User, Group, UserManager
from django.db.models import Q

from namenames.frontend.models import SuggestedName, UserToUser

import datetime


class NameForm(forms.Form):
    name = forms.CharField(required = True, max_length = 255)


class FriendForm(forms.Form):
    name = forms.CharField(label = 'Add friend', required = True, max_length = 255)


class Home(TemplateView):
    template_name = 'frontend/index.html'
    
    
    def get_suggested_names(self, request):
        suggested_names = None
        if request.user.is_authenticated():
            suggested_names = SuggestedName.objects.filter(user=request.user)
            friends = UserToUser.objects.filter(user=request.user)
            
            for loop_item in suggested_names:
                loop_item.matched = False
                
                for loop_friend in friends:
                    matched_names = SuggestedName.objects.filter(
                        Q(user=loop_friend.linked_user) &
                        Q(name=loop_item.name)
                    )
                    
                    matched_name_count = len(matched_names)
                    
                    if matched_name_count > 0:
                        loop_item.matched = True
            
        return suggested_names
        
        
    def name_form(self, request):
        view_form = NameForm()
        
        if request.method == 'POST':
            if request.POST.get('delete', None) != None:
                suggested_name = SuggestedName.objects.get(user=request.user, id=int(request.POST.get('delete')))
                suggested_name.delete()
                
                return view_form
            
            view_form = NameForm(request.POST)
            if view_form.is_valid():
                print('adding')
                new_name = view_form.cleaned_data['name']
                
                suggested_name = SuggestedName()
                suggested_name.name = new_name
                suggested_name.user = request.user
                suggested_name.save()
                                                                
                view_form = NameForm()
            
        return view_form
    
    
    def init(self, request, kwargs):
        suggested_names = self.get_suggested_names(request)
        name_form = self.name_form(request)
        suggested_names = self.get_suggested_names(request)
        
        return {
            'time': datetime.datetime.now(),
            'suggested_names': suggested_names,
            'name_form': name_form,
        }
    
    
    def get(self, request, **kwargs):
        return self.render_to_response(
            self.init(request, kwargs),
        )


    def post(self, request, **kwargs ):
        return self.render_to_response(
            self.init(request, kwargs),
        )


class Friend(TemplateView):
    template_name = 'frontend/friend.html'
    
    
    def friend_form(self, request):
        view_form = FriendForm()
        
        if request.method == 'POST':
            if request.POST.get('delete', None) != None:
                friend = UserToUser.objects.get(id=int(request.POST.get('delete')))
                friend.delete()
                
                return view_form
                
            if request.POST.get('add', None) != None:
                friend = User.objects.get(id=int(request.POST.get('add')))
                new_link = UserToUser()
                new_link.user = request.user
                new_link.linked_user = friend
                new_link.save()
                
                return view_form
            
            view_form = FriendForm(request.POST)
            if view_form.is_valid():
                search_name = view_form.cleaned_data['name']
                
                view_form.friend_search = User.objects.filter(
                    ~Q(id=request.user.id),
                    Q(first_name__contains=search_name) | Q(last_name__contains=search_name)
                )
                
                #suggested_name = SuggestedName()
                #suggested_name.name = new_name
                #suggested_name.user = request.user
                #suggested_name.save()
                
        return view_form
    
    def get_friends(self, request):
        friends = None
        
        if request.user.is_authenticated():
            friends = UserToUser.objects.filter(user=request.user)
            
        return friends
    
    
    def init(self, request, kwargs):
        friend_form = self.friend_form(request)
        friends = self.get_friends(request)
        
        return {
            'friends': friends,
            'friend_form': friend_form,
        }
    
    
    def get(self, request, **kwargs):
        return self.render_to_response(
            self.init(request, kwargs),
        )
    
    
    def post(self, request, **kwargs ):
        return self.render_to_response(
            self.init(request, kwargs),
        )