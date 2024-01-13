# posting-app

## STYLING DJANGO FORMS

## Looping through the form

```html
<style>
  .h-100 {
    min-height: 100vh;
  }
</style>

<div class="w-100 d-flex justiy-content-center align-items-center h-100">
  <form method="POST" class="row" enctype="multipart/form-data">
    {% csrf_token %} {% for field in form %}
    <div class="col-6 text-start">{{field.label}}</div>
    <div class="col-6">{{field}}</div>
    {% endfor %}
    <button type="submit">submit</button>
  </form>
</div>
```

## Use Django’s Built-in CSS Classes

Django automatically adds CSS classes to form elements, making it easy to style them. You can customize these styles in your project’s CSS file.

For example, Django adds the following classes to a form field:

form-control: Applied to most input elements.
form-select: Applied to <select> elements.
form-check-input: Applied to <input type="checkbox"> elements.

## Customize Form Templates

Django allows you to customize the HTML rendering of form widgets by creating custom form templates.
To do this:

```html
<!-- templates/registration/form.html -->
{% for field in form %}
<div class="form-group">
  {{ field.label_tag }} {{ field }} {% if field.help_text %}
  <small class="form-text text-muted">{{ field.help_text }}</small>
  {% endif %}
</div>
{% endfor %} I
```

## Implement Custom CSS

For complete control over the form’s appearance, create custom CSS rules targeting form elements, classes, or IDs. You can add CSS classes to form fields or wrap them in custom HTML elements and apply styles accordingly.

```python
from django import forms

class MyForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'custom-input'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'custom-input'}))
```

## django allauth forms

```html login.html
{% extends "bases/bootstrap-auth.html" %} {% load i18n %} {% load bootstrap4 %}
{% load account socialaccount %} {% block head_title %}{% trans "Sign In" %}{%
endblock %} {% block inner-content %} {% get_providers as
socialaccount_providers %}

<h1 class="text-center">Log In</h1>
<hr />

<div class="row">
  {% if socialaccount_providers %}
  <div class="col-md-5 col-lg-5">
    {% include "allauth/account/provider_panel.html" with process="login" %}
  </div>
  {% endif %}

  <div
    class="{% if socialaccount_providers %}col-md-7 col-lg-7 {% else %} col-md-8 col-md-offset-2 col-lg-6 col-lg-offset-3 {% endif %}"
  >
    <form class="login" method="POST" action="{% url 'account_login' %}">
      <span class="pull-right"
        >Not yet a member? <a href="{% url 'account_signup' %}">Join</a></span
      >
      {% csrf_token %} {% bootstrap_form form %} {% if redirect_field_value %}
      <input
        type="hidden"
        name="{{ redirect_field_name }}"
        value="{{ redirect_field_value }}"
      />
      {% endif %}
      <div class="form-actions">
        <button class="btn btn-primary pull-right" type="submit">
          {% trans "Sign In" %}
        </button>
        <a class="btn" href="{% url 'account_reset_password' %}"
          >{% trans "Forgot Password?" %}</a
        >
      </div>
    </form>
  </div>
</div>

{% endblock %}
```

```html base.html
{% extends "bases/bootstrap-member.html" %} {% load i18n %} {% block content %}

<div class="container">
  <h1>{% trans 'My Account' %}</h1>

  <ul class="nav nav-tabs">
    <li class="{% block account_nav_email %}{% endblock %}">
      <a href="{% url 'account_email' %}">{% trans 'E-mail Addresses' %}</a>
    </li>
    <li class="{% block account_nav_change_password %}{% endblock %}">
      <a href="{% url 'account_change_password' %}"
        >{% trans 'Change Password' %}</a
      >
    </li>
    {% url 'socialaccount_connections' as connections_url %} {% if
    connections_url %}
    <li class="{% block account_nav_socialaccount_connections %}{% endblock %}">
      <a href="{{ connections_url}}">{% trans 'Connected Accounts' %}</a>
    </li>
    {% else %}
    <li>No connections url</li>
    {% endif %}
  </ul>
  {% block account_content %} {% endblock %}
</div>

{% endblock %} {# {% block appjs %}
<script src="//ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>
{% block appjs_jquery %} {% endblock %} {% endblock %} #}
```

```html signup.html
{% extends "bases/bootstrap-auth.html" %} {% load i18n %} {% load bootstrap4 %}
{% load account socialaccount %} {% block head_title %}{% trans "Signup" %}BS{%
endblock %} {% block inner-content %} {% get_providers as
socialaccount_providers %}

<h1>{% trans "Sign Up" %}</h1>

<div class="row">
  {% if socialaccount_providers %}
  <div class="col-md-5 col-lg-5">
    {% include "allauth/account/provider_panel.html" with process="login" %}
  </div>
  {% endif %}

  <div
    class="{% if socialaccount_providers %}col-md-7 col-lg-7 {% else %} col-md-8 col-md-offset-2 col-lg-6 col-lg-offset-3 {% endif %}"
  >
    <p>
      {% blocktrans %}Already have an account? Then please
      <a href="{{ login_url }}">sign in</a>.{% endblocktrans %}
    </p>

    <form id="signup_form" method="post" action="{% url 'account_signup' %}">
      {% csrf_token %} {% bootstrap_form form %} {% if redirect_field_value %}
      <input
        type="hidden"
        name="{{ redirect_field_name }}"
        value="{{ redirect_field_value }}"
      />
      {% endif %}
      <div class="form-actions">
        <button class="btn btn-primary" type="submit">
          {% trans "Sign Up" %}
        </button>
      </div>
    </form>
  </div>
</div>
{% endblock %}
```

## FLASH MESSAGES

message.debug
message.info
message.success
message.warning
message.error

start:-> 6
python django tutorial: full featured web app: login and logout system
