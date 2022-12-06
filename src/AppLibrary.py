"""
To be built very soon

from stub_io import StubIO
from utils.commands import COMMANDS
from services.reference_service import ReferenceService
from file_writer import FileWriter
from app import App


class AppLibrary:
    def __init__(self):
        self._io = StubIO()
        self._reference_service = ReferenceService()
        self._user_service = UserService(self._user_repository)

        self._app = App(
            self._user_service,
            self._io
        )

    def input(self, value):
        self._io.add_input(value)

    def output_should_contain(self, value):
        outputs = self._io.outputs

        if not value in outputs:
            raise AssertionError(
                f"Output \"{value}\" is not in {str(outputs)}"
            )

    def run_application(self):
        self._app.run()

    def create_user(self, username, password):
        self._user_service.create_user(username, password)
"""