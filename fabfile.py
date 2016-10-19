from fabric.api import local

def serve():
    local("pip install -r requirements.txt")
    local("python app.py")
