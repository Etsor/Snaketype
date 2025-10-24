class Color:
    # Reset all styles
    RESET: str = '\033[0m'

    # Text styles
    BOLD: str          = '\033[1m'
    DIM: str           = '\033[2m'
    ITALIC: str        = '\033[3m'         # !!! May not work everywhere !!!
    UNDERLINE: str     = '\033[4m'
    BLINK: str         = '\033[5m'         # !!! May not work everywhere !!!
    INVERT: str        = '\033[7m'
    STRIKETHROUGH: str = '\033[9m'
    HIDDEN: str        = '\033[8m'

    # Foreground colors
    FG_BLACK: str   = '\033[30m'
    FG_RED: str     = '\033[31m'
    FG_GREEN: str   = '\033[32m'
    FG_YELLOW: str  = '\033[33m'
    FG_BLUE: str    = '\033[34m'
    FG_MAGENTA: str = '\033[35m'
    FG_CYAN: str    = '\033[36m'
    FG_WHITE: str   = '\033[37m'

    # Bright foreground colors
    FG_BRIGHT_BLACK: str   = '\033[90m'
    FG_BRIGHT_RED: str     = '\033[91m'
    FG_BRIGHT_GREEN: str   = '\033[92m'
    FG_BRIGHT_YELLOW: str  = '\033[93m'
    FG_BRIGHT_BLUE: str    = '\033[94m'
    FG_BRIGHT_MAGENTA: str = '\033[95m'
    FG_BRIGHT_CYAN: str    = '\033[96m'
    FG_BRIGHT_WHITE: str   = '\033[97m'

    # Background colors
    BG_BLACK: str   = '\033[40m'
    BG_RED: str     = '\033[41m'
    BG_GREEN: str   = '\033[42m'
    BG_YELLOW: str  = '\033[43m'
    BG_BLUE: str    = '\033[44m'
    BG_MAGENTA: str = '\033[45m'
    BG_CYAN: str    = '\033[46m'
    BG_WHITE: str   = '\033[47m'

    # Bright background colors
    BG_BRIGHT_BLACK: str   = '\033[100m'
    BG_BRIGHT_RED: str     = '\033[101m'
    BG_BRIGHT_GREEN: str   = '\033[102m'
    BG_BRIGHT_YELLOW: str  = '\033[103m'
    BG_BRIGHT_BLUE: str    = '\033[104m'
    BG_BRIGHT_MAGENTA: str = '\033[105m'
    BG_BRIGHT_CYAN: str    = '\033[106m'
    BG_BRIGHT_WHITE: str   = '\033[107m'
    

def colorize(
    text: str,
    fg: str         = "",
    bg: str         = "",
    bold: bool      = False,
    dim: bool       = False,
    italic: bool    = False,
    underline: bool = False,
    blink: bool     = False,
    invert: bool    = False,
    strike: bool    = False,
    hidden: bool    = False
) -> str:
    """
    Parameters:
        text (str): Text to style
        fg (str): Foreground color
        bg (str): Background color
        bold (bool): Bold
        underline (bool): Underlined
        italic (bool): Italic
        strike (bool): Strikethrough
        invert (bool): Inverted colors
        dim (bool): Dim
        hidden (bool): Hidden

    Returns:
        str: Styled string ready to print
    """
    
    styles = []

    if bold:      styles.append(Color.BOLD)
    if dim:       styles.append(Color.DIM)
    if italic:    styles.append(Color.ITALIC)
    if underline: styles.append(Color.UNDERLINE)
    if strike:    styles.append(Color.STRIKETHROUGH)
    if invert:    styles.append(Color.INVERT)
    if blink:     styles.append(Color.BLINK)
    if hidden:    styles.append(Color.HIDDEN)

    if fg:        styles.append(fg)
    if bg:        styles.append(bg)

    return f"{''.join(styles)}{text}{Color.RESET}"
