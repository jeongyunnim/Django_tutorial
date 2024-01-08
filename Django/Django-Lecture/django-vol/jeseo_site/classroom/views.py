from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (TemplateView, 
                                  FormView, 
                                  CreateView, 
                                  ListView, 
                                  DetailView, 
                                  UpdateView,
                                  DeleteView)
from classroom.models import Teacher
from classroom.forms import ContactForm

class HomeView(TemplateView):
    template_name = "classroom/home.html"

class ThankYouView(TemplateView):
    template_name = "classroom/thank_you.html"

class TeacherCreateView(CreateView):
    model = Teacher
    # model을 알려주면 Django는 자동으로 teacher_form.html 파일(전부 소문자)을 찾는다.
    # 자동으로 모델에 대한 인스턴스를 하나 생성한다.
    # fields = ['first_name', 'last_name', 'subject']
    fields = "__all__"
    success_url = reverse_lazy('classroom:list_teacher')

class ContactFormview(FormView):
    form_class = ContactForm
    template_name = "classroom/contact.html"
    success_url = reverse_lazy('classroom:thank_you')
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class TeacherListView(ListView):
    model = Teacher
    # default queryset = Teacher.objects.all()
    queryset = Teacher.objects.order_by('first_name')
    context_object_name = 'teacher_list'

class TeacherDetailView(DetailView):
    # RETURN ONLY ONE MODEL ENTRY
    # model_detail.html
    model = Teacher
    # primary key에 대한 특정 Teacher를 HTML에 대한 컨텍스트 객체로 보낸다.

class TeacherUpdateView(UpdateView):
    # model_form.html을 공유한다.
    model = Teacher
    fields = ['first_name']
    success_url = reverse_lazy('classroom:list_teacher')

class TeacherDeleteView(DeleteView):
    # Form -> Confirm Delete Button
    model = Teacher
    success_url = reverse_lazy('classroom:list_teacher')