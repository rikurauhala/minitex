#from pathlib import Path

from stub_io import StubIO
#from utils.commands import COMMANDS
from services.reference_service import ReferenceService
#from file_writer import FileWriter
from app import Application
from database import initialize_database


class AppLibrary:
    def __init__(self, ):
        """Creates class for Robot Framework to test the main App from with fake IO"""
        self._io = StubIO()
        self._reference_service = ReferenceService()
        self._app = Application(self._io, False)

    def input(self, value):
        """Test commands given in reference.robot (that are translated further with
            resource.robot keywords) in form "Input  x" are added here to app's
            pre-start input list"""
        self._io.give_command(value)

    def output_should_contain(self, value):
        """This Test command checks if the given value with command "Output Should Contain x"
        from reference.robot has same value as output list that was filled while app was running"""
        outputs = self._io.outputs

        if not value in outputs:
            raise AssertionError(
                f"Output \"{value}\" is not in {str(outputs)}"
            )

    def output_should_not_contain(self, value):
        outputs = self._io.outputs

        if value in outputs:
            raise AssertionError(
                f"Output \"{value}\" is in {str(outputs)}"
            )

    def export_message_should_contain(self, value):
        #folder_path = Path("./data")
        #file_name = "references.bib"

        #message = value.split("*")
        #part = message[0] + str(self._folder_path.joinpath(self._file_name).resolve())

        outputs = self._io.outputs

        if value in outputs:
            raise AssertionError(
                f"Output \"{value}\" is in {str(outputs)}"
            )

    def input_integer(self, integer):
        self._io.input_integer(integer)

    def run_application(self):
        self._app.start()

    def format_database(self):
        initialize_database()
