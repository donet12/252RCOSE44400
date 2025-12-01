from flask import Flask, render_template, request, redirect
import requests
import os
from datetime import datetime

app = Flask(__name__)

# URL of the backend container inside Docker network
BACKEND_URL = "http://backend:5001"


@app.route("/", methods=["GET"])
def index():
    """
    TODO:
    - Send a GET request to BACKEND_URL + "/api/message"
    - Extract the message from the JSON response
    - Render index.html and pass the message as "current_message"
    """
    current_message = ""
    timestamp_display = "N/A"

    try:
        response = requests.get(BACKEND_URL + "/api/message", timeout=5)
        if response.status_code == 200:
            data = response.json()
            raw_message = data.get("message", "")

            if " (updated at " in raw_message:
                message_part, ts_part = raw_message.rsplit(" (updated at ", 1)
                current_message = message_part
                ts_text = ts_part.rstrip(")")
                try:
                    timestamp_display = datetime.strptime(ts_text, "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d %H:%M:%S")
                except ValueError:
                    timestamp_display = ts_text
            else:
                current_message = raw_message
        else:
            current_message = f"Error: {response.status_code}"
    except Exception as e:
        current_message = f"Error: {str(e)}"

    return render_template("index.html", current_message=current_message, last_updated=timestamp_display)


@app.route("/update", methods=["POST"])
def update():
    """
    TODO:
    - Get the value from the form field named "new_message"
    - Send a POST request to BACKEND_URL + "/api/message"
      with JSON body { "message": new_message }
    - Redirect back to "/"
    """
    new_message = request.form.get("new_message", "")
    timestamp_display = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        requests.post(BACKEND_URL + "/api/message", json={"message": new_message}, timeout=5)
        return render_template("index.html", current_message=new_message, last_updated=timestamp_display)
    except Exception as e:
        return render_template("index.html", current_message=f"Error: {str(e)}", last_updated=timestamp_display)


# v2 TODO:
# - Change page title (in HTML)
# - Parse timestamp from backend message
# - Show "Last updated at: <timestamp>" in the template


if __name__ == "__main__":
    # Do not change the host or port
    app.run(host="0.0.0.0", port=5000)

