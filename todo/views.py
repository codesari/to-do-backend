from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)
from .models import Todo
from .forms import TodoForm
from django.urls import reverse_lazy


class TodoListView(ListView):
    model=Todo
    template_name = 'todo/list.html'

# ? create ve update işlemlerinde form gerekli oduğundan form_class=TodoForm satırını bu fonksiyonlarda çağırdık
class TodoCreateView(CreateView):
    model=Todo
    form_class=TodoForm
    template_name = 'todo/add.html'
    # todo/todo_form.html
    success_url=reverse_lazy('todo_list')
    
class TodoUpdateView(UpdateView):
    model = Todo
    form_class = TodoForm
    template_name = 'todo/update.html'
    # todo/todo_update.html
    success_url = reverse_lazy('todo_list')
    
class TodoDeleteView(DeleteView):
    model=Todo
    template_name = 'todo/delete.html'
    # todo/todo_confirm_delete.html
    success_url = reverse_lazy('todo_list')
class TodoDetailView(DetailView):
    model = Todo
    template_name = 'todo/detail.html'
    # todo/todo_detail.html
    success_url = reverse_lazy('todo_list')
        