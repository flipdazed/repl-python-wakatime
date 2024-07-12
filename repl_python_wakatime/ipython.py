"""ipython
==========
"""

from typing import Any, Dict, Tuple, List, Optional, Callable

from IPython.terminal.prompts import ClassicPrompts, Prompts
from IPython.terminal.interactiveshell import TerminalInteractiveShell
from pygments.token import Token, _TokenType
from traitlets.config.loader import Config, LazyConfigValue

from repl_python_wakatime.hooks.wakatime import wakatime_hook


def get_new_prompts_class(
    hook: Callable = wakatime_hook,
    args: Tuple = (),
    kwargs: Optional[Dict[str, Any]] = None,
) -> Any:
    """Get new prompts class.

    :param prompts_class:
    :type prompts_class: type
    :param hook:
    :type hook: Callable
    :param args:
    :type args: tuple
    :param kwargs:
    :type kwargs: dict[str, Any] | None
    :rtype: type
    """
    if kwargs is None:
        kwargs = {}

    class Ps(Prompts):
        """Ps."""

        def in_prompt_tokens(self) -> List[Tuple[_TokenType, str]]:
            """In prompt tokens.

            :rtype: list[tuple[_TokenType, str]]
            """
            return [
                (Token.Prompt, self.vi_mode() ),
                (Token.Prompt, 'In ['),
                (Token.PromptNum, str(self.shell.execution_count)),
                (Token.Prompt, ']: '),
            ]

        def continuation_prompt_tokens(
            self, width: Optional[int] = None
        ) -> List[Tuple[_TokenType, str]]:
            """Continuation prompt tokens.

            :param width:
            :type width: int | None
            :rtype: list[tuple[_TokenType, str]]
            """
            if width is None:
                width = self._width()
            return [
                (Token.Prompt, (' ' * (width - 5)) + '...: '),
            ]

        def rewrite_prompt_tokens(self) -> List[Tuple[_TokenType, str]]:
            """Rewrite prompt tokens.

            :rtype: list[tuple[_TokenType, str]]
            """
            width = self._width()
            return [
                (Token.Prompt, ('-' * (width - 2)) + '> '),
            ]

        def out_prompt_tokens(self) -> List[Tuple[_TokenType, str]]:
            """Out prompt tokens.

            :rtype: list[tuple[_TokenType, str]]
            """
            hook(*args, **kwargs)
            return [
                (Token.OutPrompt, 'Out['),
                (Token.OutPromptNum, str(self.shell.execution_count)),
                (Token.OutPrompt, ']: '),
            ]

    return Ps


def install_hook(
    c: Config,
    hook: Callable = wakatime_hook,
    args: Tuple = (),
    kwargs: Optional[Dict[str, Any]] = None,
) -> Config:
    """Install hook.

    :param c:
    :type c: Config
    :param hook:
    :type hook: Callable
    :param args:
    :type args: tuple
    :param kwargs:
    :type kwargs: dict[str, Any] | None
    :rtype: Config
    """
    if kwargs is None:
        kwargs = {"plugin": "repl-ipython-wakatime"}
    c.TerminalInteractiveShell.prompts_class = get_new_prompts_class(  # type: ignore
        hook,
        args,
        kwargs,  # type: ignore
    )
    return c
