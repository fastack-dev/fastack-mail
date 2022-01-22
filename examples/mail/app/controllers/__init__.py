from app.controllers.mailer import MailerController
from fastack import Fastack


def init_controllers(app: Fastack):
    app.include_controller(MailerController())
