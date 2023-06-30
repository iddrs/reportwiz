pure = '''
<table>
    {% if caption is defined %}
        <caption>{{ caption }}</caption>
    {% endif %}
    
    <thead>
        <tr>
        {% for label in labels %}
            <th>{{ label }}</th>
        {% endfor %}
        </tr>
    <thead>
    
    <tbody>
        {% for row in data %}
            <tr>
            {% for column in columns %}
                <td>{{ row[column] }}</td>
            {% endfor %}
            </tr>
        {% endfor %}
    <tbody>
</table>
'''