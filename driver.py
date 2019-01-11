from app import create_app, db, cli
from app.models import User, FileContents



app = create_app()
print("app is being created")
cli.register(app)


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'FuleContents': FileContents}
