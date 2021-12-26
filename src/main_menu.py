import sys

class MainMenu:
    """Class that defines main menu and how to change and select options inside.
    """
    def __init__(self):
        self.options = {0: "start", 1: "change_level", 2: "change_color",  3: "quit"}
        self.colors = {1: "white", 2: "red", 3: "green", 4: "blue", 5: "yellow", 6: "cyan"}
        self.actions = {"DOWN_DOWN": self._menu_move_down,
                   "UP_DOWN": self._menu_move_up,
                   "RETURN_DOWN": self._menu_select,
                   "LEFT_DOWN": self._menu_move_left,
                   "RIGHT_DOWN": self._menu_move_right}

    def check_main_menu_events(self, events, selected, level, selected_color):
        """Defines how menu options change with different keypress events as input.

        Args:
            events: List of keypress events as list of strings
            selected: Integer that defines currently selected menu option
            level: Current level number
            selected_color Integer that defines currently selected color

        Returns:
            selected: Currently selected menu option as number
            level: Currently selected level number
            selected_color: Currently selected color as number
            start: Boolean, True if start button has been pressed, False otherwise
            color: Selected color as string
            option: Selected menu option as string
        """
        start = False
        option = self.options[selected]
        for event in events:
            if event == "QUIT":
                sys.exit()
            if event in self.actions:
                selected, level, selected_color, start = self.actions[event](
                    selected, level, selected_color, option
                    )
                if start:
                    break
        option = self.options[selected]
        color = self.colors[selected_color]
        return selected, level, selected_color, start, color, option

    def _menu_move_down(self, selected, level, selected_color, option):
        return min(3, selected + 1), level, selected_color, False

    def _menu_move_up(self, selected, level, selected_color, option):
        return max(0, selected - 1), level, selected_color, False

    def _menu_move_left(self, selected, level, selected_color, option):
        if option == "change_level":
            level = max(1, level - 1)
        if option == "change_color":
            selected_color = max(1, selected_color - 1)
        return selected, level, selected_color, False

    def _menu_move_right(self, selected, level, selected_color, option):
        if option == "change_level":
            level = min(10, level + 1)
        if option == "change_color":
            selected_color = min(6, selected_color + 1)
        return selected, level, selected_color, False

    def _menu_select(self, selected, level, selected_color, option):
        chosen = False
        if option == "start":
            chosen = True
        elif option == "quit":
            sys.exit()
        return selected, level, selected_color, chosen
