<div>
<h3>Category</h3>
<ul>
    {% for category in category_list %}
    <li>
    <a href="{{ category.get_absolute_url }}">
        {{ category.title }}
        {% if category.blog.show_category_count %}
            ({{ category.count }})
        {% endif %}
    </a>
    </li>
    {% endfor %}
</ul>
</div>
