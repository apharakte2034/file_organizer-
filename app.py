from flask import Flask, render_template, request
from file_organizer import organize_files
import webbrowser

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    messages = []
    if request.method == "POST":
        folder_path = request.form.get("folder_path")
        if folder_path:
            messages = organize_files(folder_path.strip('"'))
        else:
            messages = ["❌ Please enter a valid folder path."]
    return render_template("index.html", messages=messages)

if __name__ == "__main__":
    url = "http://127.0.0.1:5000/"
    print("\n==============================================")
    print(f"🚀 File Organizer Web App is running!")
    print(f"🌐 Open this link in your browser: {url}")
    print("==============================================\n")
    
    # Optional: Automatically open in browser
    try:
        webbrowser.open(url)
    except:
        pass

    app.run(debug=False)
