import logging

PREFIX = "SPCHARGER"

# the TreeRoots logger (pat. pending).
#
# there are three "fixes":
# - the "prefix";
# - the "fix";
# - and the "suffix".

class TreeRoots(logging.Formatter):
    def __init__(self):
        super().__init__()
        self.last_mod = "this_string_will_never_be_used"
        self.last_fnc = "this_string_will_never_be_used"

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
                tooth = "???"
            case "DEBUG":
                tooth = "DBG"
            case "INFO":
                tooth = "INF"
            case "WARNING":
                tooth = "WRN"
            case "ERROR":
                tooth = "ERR"
            case "CRITICAL":
                tooth = "CRT"
            case _:
                tooth = "???"
        tooth = tooth + "{:>11}".format("┠╼" if new_fnc else "┃ ")
        # tooth is the "suffix".
        # fnc_adorn is...another suffix. goes before, though.

        output = []
        if new_mod or fst_mod:
            if not fst_mod:
                output.append("{:^12}".format("fzz...") + "┷")
            output.append(f"{mod_adorn:>12}┒")
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
