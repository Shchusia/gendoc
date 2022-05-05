from typing import Optional

from gen_doc.models import ParsedDocString

from .parser_python_google_docstring import GoogleDocStringPyParser
from .parser_python_sphinx_docstring import SphinxDocStringPyParser


class DocStingPyParser:
    @staticmethod
    def parse(doc_string: Optional[str]) -> Optional[ParsedDocString]:
        if not doc_string:
            return None
        return max(
            [
                GoogleDocStringPyParser.parse(doc_string=doc_string),
                SphinxDocStringPyParser.parse(doc_string=doc_string),
            ]
        )
