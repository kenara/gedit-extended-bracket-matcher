from gi.repository import GObject, Gedit, Gtk, Gdk

class BracketLinePlugin(GObject.Object, Gedit.ViewActivatable):
    __gtype_name__ = "BracketLinePlugin"
    view = GObject.Property(type=Gedit.View)

    SEARCH_LIMIT = 100000  # 100k characters

    def do_activate(self):
        self.buffer = self.view.get_buffer()
        self.statusbar = self.view.get_toplevel().get_statusbar()
        self.handler = self.view.connect("key-release-event", self.on_key_release)
        self.motion_handler = self.view.connect("motion-notify-event", self.on_cursor_moved)

    def do_deactivate(self):
        self.view.disconnect(self.handler)
        self.view.disconnect(self.motion_handler)

    def on_key_release(self, view, event):
        self.check_bracket_match()
        return False

    def on_cursor_moved(self, view, event):
        self.check_bracket_match()
        return False

    def check_bracket_match(self):
        buf = self.buffer
        cursor = buf.get_iter_at_mark(buf.get_insert())

        brackets = {'(': ')', '[': ']', '{': '}', ')': '(', ']': '[', '}': '{'}
        char_under = cursor.get_char()
        prev_iter = cursor.copy()
        prev_iter.backward_char()
        char_before = prev_iter.get_char()

        if char_under in brackets:
            match_pos = self.find_match(cursor.copy(), char_under, brackets[char_under], char_under in "({[")
        elif char_before in brackets:
            match_pos = self.find_match(prev_iter.copy(), char_before, brackets[char_before], char_before in "({[")
        else:
            return

        if match_pos:
            line = match_pos.get_line() + 1  # lines are 0-indexed
            self.statusbar.push(0, f"Matching bracket found at line {line}")
        else:
            self.statusbar.push(0, "No matching bracket found (even with extended range)")

    def find_match(self, start_iter, open_char, close_char, forward=True):
        depth = 1
        steps = 0

        while steps < self.SEARCH_LIMIT:
            if forward:
                if not start_iter.forward_char():
                    break
            else:
                if not start_iter.backward_char():
                    break

            c = start_iter.get_char()
            if c == open_char:
                depth += 1
            elif c == close_char:
                depth -= 1
                if depth == 0:
                    return start_iter.copy()

            steps += 1

        return None
