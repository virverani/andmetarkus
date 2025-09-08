# Create a function to add a line to file
class FileFunctions:

    def add_line_to_file(self, file_path: str, line: str) -> None:
        """Add row to end of file."""
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write(line + '\n')

    def read_file(self, file_path: str) -> list[str]:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.readlines()