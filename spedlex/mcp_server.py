"""SPEDLex as an MCP server, so any MCP-capable assistant (Claude, ChatGPT
agents, IDE agents, local models behind an MCP client) can look up U.S.
special-education terms and check its own wording.

    pip install "spedlex[mcp] @ git+https://github.com/SiskinSkai/spedlex"
    python -m spedlex.mcp_server            # stdio transport

Then register the command with your MCP client (docs/USING-WITH-AI.md shows
a client config). Needs Python 3.10+ and the `mcp` package; the rest of
SPEDLex has no dependencies.

The server runs locally on the bundled data. Text sent to its tools is
processed in memory and never stored or sent anywhere.
"""

from functools import lru_cache

try:  # mcp 2.x
    from mcp.server.mcpserver import MCPServer as _Server
except ImportError:  # mcp 1.x
    from mcp.server.fastmcp import FastMCP as _Server

from . import __version__
from .lexicon import Lexicon

INSTRUCTIONS = f"""SPEDLex v{__version__}: an open, cited vocabulary of U.S. special-education terms
(IDEA Part B plus state layers). Use it to name special-education concepts the way the reader's
state does, to expand acronyms correctly, and to avoid disfavored terms. Pass the reader's state as a
postal code ('TX') when you know it. Results record how official documents name each concept, with a
citation and a review status; they are not legal definitions. Most records are not yet
expert-reviewed, so say so if a user relies on one for a decision."""

server = _Server(name="spedlex", instructions=INSTRUCTIONS)


@lru_cache(maxsize=64)
def _lex(state):
    return Lexicon.from_default(jurisdiction=state or None)


@server.tool()
def lookup_term(term: str, state: str = "") -> list:
    """What a special-education term or acronym names (e.g. 'ARD committee', 'PLAAFP', 'CSE'), the
    national preferred term, what each covered state's documents call it, the term to use for the
    reader's state, whether the form is disfavored, a citation and the review status. Returns an
    empty list if the term is not in SPEDLex."""
    return _lex(state).lookup(term)


@server.tool()
def terms_in_text(text: str, state: str = "") -> list:
    """Every special-education term found in a text, with its concept, category, citation, review
    status and the reader's state's own name for it. Ambiguous acronyms list their candidates."""
    return [a.to_dict() for a in _lex(state).annotate(text)]


@server.tool()
def check_text(text: str, state: str = "") -> list:
    """Check a draft for special-education wording to reconsider: disfavored terms (e.g. 'mental
    retardation'), older names, terms recorded only in other states' documents (e.g. 'ARD committee'
    written for a New York reader) and acronyms that mean different things in different states.
    Each issue has a message and, where possible, a suggested replacement."""
    return [i.to_dict() for i in _lex(state).check(text)]


@server.tool()
def glossary_for_text(text: str, state: str = "") -> str:
    """A short, cited Markdown glossary of the special-education terms in a text, suitable for
    grounding an answer about that text."""
    return _lex(state).glossary(text)


def main():
    server.run()


if __name__ == "__main__":
    main()
