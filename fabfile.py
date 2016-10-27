from fabric.api import local

def serve():
    local("python app.py")

def build():
    local("pip install -r requirements.txt")
    local("python app.py")

def test():
    local("python sample_tests.py")
