import tic_tac_toe

class writer:
    def __init__(self, *writers):
        self.writers = writers
        self.written = ""

    def __str__(self):
        return str(self.written)

    def write(self, text):
        self.written += text.rstrip(' ')

    def get_written(self):
        return self.written

    def clear_written(self):
        self.written = ""

import sys
def gather_printed_output(module=None, function=None, *args):
    gathered = ""
    if module and function:
        saved = sys.stdout
        sys.stdout = writer(sys.stdout)
        function_call = getattr(sys.modules[module],function)
        function_call(*args)
        old_writer = sys.stdout
        sys.stdout = saved
        gathered = old_writer.get_written()
    return gathered

# make more dynamic. Once kids know about throwing exceptions I'll be able to do more actual testing!
test_output = gather_printed_output('tic_tac_toe', 'draw_tic_tac_toe', 3)
tic_tac_toe_3 = "   |   |\n---+---+---\n   |   |\n---+---+---\n   |   |\n"

if test_output != tic_tac_toe_3:
    print("Test Fails")
else:
    print("Test Succeeds!")

print(tic_tac_toe_3)
print(test_output)