{% extends "base.html" %}

{% block announce %}

<div class="admonition warning">
<p class="admonition-title">Unstable release!</p>
You are viewing build based on the latest commit on the <code>main</code> branch. This mean,
that documentation is subject to change. Also certain features can behave
differently in you production deployment. Please, visit
<a href="/latest">/latest</a> for the latest released documentation.
</div>
{% endblock %}
