from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.views.generic import list_detail
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from poster import forms
from poster.models import Language, Code, Tag

def add_code(request):
    """
    Template::
        poster/add_code_form.html
    """
    parent_id = request.GET.get('oid', None)

    if request.method == 'POST':
        form = forms.AddCodeForm(request.POST)
        if form.is_valid():
            new_code = Code(title=form.cleaned_data['title'],
                                  description=form.cleaned_data['description'],
                                  source=form.cleaned_data['source'],
                                  tag_list=form.cleaned_data['tag_list'],
                                  language_id=form.cleaned_data['language'],
                                  author=request.user)
            if parent_id:
                new_code.parent_id = parent_id
            new_code.save()
            return HttpResponseRedirect(new_code.get_absolute_url())
    else:
        form = forms.AddCodeForm()
    return render_to_response('poster/add_code_form.html',
                              { 'form': form },
                              context_instance=RequestContext(request))
add_code = login_required(add_code)


def edit_code(request, code_id):
    """
    Context::
        form
            The form to add the Code.
        original
            The Code being edited.
    Template::
        poster/edit_code_form.html
    """
    code = get_object_or_404(Code,
                                pk=code_id,
                                author__pk=request.user.id)
    if request.method == 'POST':
        form = forms.EditCodeForm(request.POST)
        if form.is_valid():
            for field in ['title', 'description', 'source', 'tag_list']:
                setattr(code, field, form.cleaned_data[field])
            code.save()
            return HttpResponseRedirect(code.get_absolute_url())
    else:
        form = forms.EditCodeForm(code.__dict__)
    return render_to_response('poster/edit_code_form.html',
                              { 'form': form,
                                'original': code },
                              context_instance=RequestContext(request))
edit_code = login_required(edit_code)


def code_by_language(request, slug):
    """
    Context::
    Same as the generic ``list_detail.object_list`` view, with
    one extra variable:
        object
            The Language
    Template::
        poster/language_detail.html
    """
    language = get_object_or_404(Language, slug__exact=slug)
    return list_detail.object_list(request,
                                   queryset=Code.objects.get_by_language(slug),
                                   extra_context={ 'object': language },
                                   template_name='poster/language_detail.html',
                                   **base_generic_dict)


def code_detail(request, code_id):
    """
    Context::
        object
            The Code object.
    Template::
        poster/code_detail.html
    """
    code = get_object_or_404(Code, pk=code_id)
    return render_to_response('poster/code_detail.html',
                              { 'object': code },
                              context_instance=RequestContext(request))

