from main.forms import UserRegistrationForm


class UserRegistrationService:
    @classmethod
    def create_user(cls, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            cd = form.cleaned_data
            user.email = cd['email']
            user.username = cd['username']
            user.set_password(cd['password'])
            user.save()
