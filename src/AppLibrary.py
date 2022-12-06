from stub_io import StubIO
from utils.commands import COMMANDS
from services.reference_service import ReferenceService
from file_writer import FileWriter
from app import Application


class AppLibrary:
    def __init__(self, ):
        self._io = StubIO()
        self._reference_service = ReferenceService()
        self._app = Application(self._io, False)

    def input(self, value):
        self._io.give_command(value)

    def output_should_contain(self, value):
        outputs = self._io.outputs

        if not value in outputs:
            raise AssertionError(
                f"Output \"{value}\" is not in {str(outputs)}"
            )

    def run_application(self):
        self._app.start()