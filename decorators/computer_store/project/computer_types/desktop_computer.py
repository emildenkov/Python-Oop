from project.computer_types.computer import Computer


class DesktopComputer(Computer):

    def __init__(self, manufacturer: str, model: str):
        super().__init__(manufacturer, model)

    @property
    def get_processor(self):
        return {
            "AMD Ryzen 7 5700G": 500,
            "Intel Core i5-12600K": 600,
            "Apple M1 Max": 1800,
        }

    @property
    def get_max_ram(self):
        return 128

    @property
    def get_type(self):
        return "desktop computer"
