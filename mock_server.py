from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

next_id = 1
stored_feedback = []


@app.route('/feedback/', methods=['POST'])
def create_feedback():
    global next_id
    data = request.get_json(silent=True)

    if not data or 'feedback' not in data:
        return jsonify({'error': 'invalid payload'}), 400

    data["id"] = next_id
    next_id += 1

    stored_feedback.append(data)

    return jsonify({"id": data["id"]}), 201



# HTML Template for GETTING the feedbacks in a simple nice format
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Customer Feedback</title>
    <style>
        body { font-family: Arial, sans-serif; padding: 20px; background: #f4f4f7; }
        h1 { text-align: center; }
        table { width: 100%; border-collapse: collapse; margin-top: 25px; }
        th, td { padding: 12px; border-bottom: 1px solid #ddd; }
        th { background: #4CAF50; color: white; text-align: left; }
        tr:hover { background-color: #f1f1f1; }
        .no-data { text-align: center; margin-top: 50px; font-size: 18px; color: #777; }
    </style>
</head>
<body>

<h1>📄 Customer Feedback</h1>

{% if data %}
<table>
    <tr>
        <th>ID</th>
        <th>Title</th>
        <th>Name</th>
        <th>Date</th>
        <th>Feedback</th>
        <th>Source File</th>
    </tr>

    {% for item in data %}
    <tr>
        <td>{{ item.id }}</td>
        <td>{{ item.title }}</td>
        <td>{{ item.name }}</td>
        <td>{{ item.date }}</td>
        <td>{{ item.feedback }}</td>
        <td>{{ item.source_file }}</td>
    </tr>
    {% endfor %}
</table>
{% else %}
<p class="no-data">No feedback available.</p>
{% endif %}

</body>
</html>
"""


@app.route('/feedback/', methods=['GET'])
def get_feedback():
    # If client explicitly asks for JSON
    if request.headers.get("Accept") == "application/json":
        return jsonify(stored_feedback)

    # Otherwise return nice HTML
    return render_template_string(HTML_TEMPLATE, data=stored_feedback)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


