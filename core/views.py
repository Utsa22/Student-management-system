from django.contrib import messages

from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)

from django.contrib.auth.views import (
    LoginView,
    LogoutView,
)

from django.urls import reverse_lazy

from django.views.generic import (
    TemplateView,
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)

from .forms import (
    RegisterForm,
    StudentForm,
)

from .models import Student


class HomeView(TemplateView):

    template_name = 'core/home.html'

class RegisterView(CreateView):

    form_class = RegisterForm

    template_name = 'core/register.html'

    success_url = reverse_lazy('login')


    def form_valid(self, form):

        response = super().form_valid(form)

        messages.success(
            self.request,
            'Account created successfully. Please login.'
        )

        return response


class UserLoginView(LoginView):

    template_name = 'core/login.html'


class UserLogoutView(LogoutView):

    next_page = reverse_lazy('home')


class StudentListView(LoginRequiredMixin, ListView):

    model = Student

    template_name = 'core/student_list.html'

    context_object_name = 'students'


    def get_queryset(self):

        if self.request.user.is_superuser:

            queryset = Student.objects.all()

        else:

            queryset = Student.objects.filter(
                owner=self.request.user
            )


        search_query = self.request.GET.get(
            'search',
            ''
        ).strip()


        if search_query:

            queryset = queryset.filter(
                name__icontains=search_query
            )


        return queryset.order_by('roll')



class StudentCreateView(LoginRequiredMixin, CreateView):

    model = Student

    form_class = StudentForm

    template_name = 'core/student_form.html'

    success_url = reverse_lazy('student_list')


    def form_valid(self, form):

        form.instance.owner = self.request.user

        response = super().form_valid(form)

        messages.success(
            self.request,
            'Student added successfully.'
        )

        return response

class StudentPermissionMixin(
    LoginRequiredMixin,
    UserPassesTestMixin
):


    def test_func(self):

        student = self.get_object()

        return (
            student.owner == self.request.user
            or
            self.request.user.is_superuser
        )


    def handle_no_permission(self):

        if self.request.user.is_authenticated:

            return self.permission_denied()

        return super().handle_no_permission()


class StudentDetailView(StudentPermissionMixin, DetailView):

    model = Student

    template_name = 'core/student_detail.html'

    context_object_name = 'student'

    raise_exception = True



class StudentUpdateView(StudentPermissionMixin, UpdateView):

    model = Student

    form_class = StudentForm

    template_name = 'core/student_form.html'

    success_url = reverse_lazy('student_list')

    raise_exception = True


    def form_valid(self, form):

        response = super().form_valid(form)

        messages.success(
            self.request,
            'Student updated successfully.'
        )

        return response


class StudentDeleteView(StudentPermissionMixin, DeleteView):

    model = Student

    template_name = 'core/student_confirm_delete.html'

    success_url = reverse_lazy('student_list')

    raise_exception = True


    def form_valid(self, form):

        response = super().form_valid(form)

        messages.success(
            self.request,
            'Student deleted successfully.'
        )

        return response