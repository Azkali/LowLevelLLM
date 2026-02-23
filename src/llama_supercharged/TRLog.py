import logging

PREFIX = "SPCHARGER"
BO_FMT = "\x1b[1m"                      # bold.
BO_BLN = "\x1b[5m"                      # blink.
NS_FMT = BO_FMT + "\x1b[95m"            # not set.      magenta.
DE_FMT = BO_FMT + "\x1b[34m"            # debug.        darkblue.
IN_FMT = BO_FMT + "\x1b[32m"            # info.         darkgreen.
WA_FMT = BO_FMT + "\x1b[33m"            # warning.      darkyellow.
ER_FMT = BO_FMT + "\x1b[91m"            # error.        red.
CR_FMT = BO_FMT + "\x1b[31m" + BO_BLN   # critical.     darkred.
NO_FMT = "\x1b[0m"                      # reset.        nothing.

# the TreeRoots logger (pat. pending).
#
# there are three "fixes":
# - the "prefix";
# - the "fix";
# - and the "suffix".

class TreeRoots(logging.Formatter):
    def __init__(self, ansi = True):
        super().__init__()
        self.last_mod = "this_string_will_never_be_used"
        self.last_fnc = "this_string_will_never_be_used"

        if not ansi:
            BO_FMT = ""
            BO_BLN = ""
            NS_FMT = "" # there has to be a better way...
            DE_FMT = ""
            IN_FMT = ""
            WA_FMT = ""
            ER_FMT = ""
            CR_FMT = ""
            NO_FMT = "" # this one isn't needed, but still. so aren't the first two.

    def format(self, record):
        parts = record.name.split(".")

        mod = parts[1] if len(parts) > 1 else "???"  # mod is the "fix".
        fnc = record.funcName

        new_mod = True if self.last_mod != mod else False
        new_fnc = True if self.last_fnc != fnc else False
        fst_mod = True if self.last_mod == "this_string_will_never_be_used" else False
        if new_mod:
            self.last_mod = mod
        if new_fnc:
            self.last_fnc = fnc

        mod_adorn = "[" + mod + "]"
        fnc_adorn = ("[" + fnc + "]") if new_fnc else ""
        pre_tooth = "╾┒" if new_fnc else " ╏"

        # "╘╗".

        #print(new_mod, end=""); print("   ", end="")
        #print(new_fnc, end=""); print("   ", end="")
        #print(fst_mod, end=""); print("   ", end="")
        #print("", flush=True)

        match record.levelname:
            case "NOTSET":
                tooth = NS_FMT + "???"
            case "DEBUG":
                tooth = DE_FMT + "DBG"
            case "INFO":
                tooth = IN_FMT + "INF"
            case "WARNING":
                tooth = WA_FMT + "WRN"
            case "ERROR":
                tooth = ER_FMT + "ERR"
            case "CRITICAL":
                tooth = CR_FMT + "CRT"
            case _:
                tooth = NS_FMT + "???"
        tooth = tooth + NO_FMT + "{:>11}".format("┠╼" if new_fnc else "┃ ")
        # tooth is the "suffix".
        # fnc_adorn is...another suffix. goes before, though.

        output = []
        if new_mod or fst_mod:
            if not fst_mod:
                output.append("{:^12}".format("fzz...") + "┷")
            output.append(f"{BO_FMT}{mod_adorn:>12}{NO_FMT}┒") # effects cannot be applied before formatting.
        output.append(f"{tooth} {fnc_adorn:^12}{pre_tooth} {record.getMessage()}")

        # to those reading this, please trust that this is more efficient.
        return f"[{PREFIX}] " + f"\n[{PREFIX}] ".join(output)

def setup(level = logging.DEBUG):
    handler = logging.StreamHandler()
    handler.setFormatter(TreeRoots())

    variable = logging.getLogger("lib")
    variable.setLevel(level)
    variable.addHandler(handler)
    variable.propagate = False
