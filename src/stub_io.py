class StubIO:
    """Module for simulating user input."""

    def __init__(self, inputs = None):
        self.inputs = inputs or []
        self.outputs = []

    def print(self, output):
        self.outputs.append(output)

    def get_command(self):
        if len(self.inputs) > 0:
            return self.command.pop(0)
        else:
            return ""

    def give_command(self, input):
        self.inputs.append(input)