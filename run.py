from my_project import create_app  # Assurez-vous que ce module existe
import os

app = create_app()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # Render attribue un port dynamique
    app.run(host="0.0.0.0", port=port, debug=False)
