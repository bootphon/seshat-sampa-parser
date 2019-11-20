from seshat.parsers.base import BaseCustomParser


class Myclass(BaseCustomParser):
    """This extension should be imported in the init file,
    and inherit from the `BaseCustomParser` class"""
    NAME = "Parser-name"  # this name should be unique, and will be displayed in Seshat's interface

    def check_annotation(self, annot: str) -> None:
        """Checks the input annotation. Doesn't return anything.
        If the annotation is, raises an `AnnotationError` """
        pass # write annotation-checking code here.