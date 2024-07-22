from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from todo.models import Task

# Create your views here.


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    template_name = "tasks/task_list.html"
    context_object_name = "tasks"

    def get_context_data(self: ListView, *args: str, **kwargs: dict) -> dict:
        context = super().get_context_data(**kwargs)
        context["tasks"] = context["tasks"].filter(user=self.request.user)
        context["count"] = context["tasks"].filter(complete=False).count()
        search_input = self.request.GET.get("search") or ""
        if search_input:
            context["tasks"] = context["tasks"].filter(title__startswith=search_input)
        context["search_input"] = search_input
        return context


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    template_name = "tasks/task_detail.html"
    context_object_name = "task"


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "tasks/task_create.html"
    fields = ["title", "description", "complete"]
    success_url = reverse_lazy("task-list")

    def form_valid(self: CreateView, form: Task) -> Task:
        form.instance.user = self.request.user
        return super().form_valid(form=form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = "tasks/task_create.html"
    fields = ["title", "description", "complete"]
    success_url = reverse_lazy("task-list")


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = "task"
    template_name = "tasks/task_delete.html"
    success_url = reverse_lazy("task-list")


class AboutView(TemplateView):
    template_name = "about.html"
