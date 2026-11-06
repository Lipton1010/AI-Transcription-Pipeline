"""Session-aware character names for a player who changed characters."""


def roster_for_session(config, session):
    roster = list(config["active_roster"])
    if session is None:
        return roster
    number = int(session)
    for change in config.get("character_transitions", []):
        old, new, transition = change["old_character"], change["new_character"], change["session"]
        if number < transition:
            roster[roster.index(new)] = old
        elif number == transition:
            roster.insert(roster.index(new), old)
    return roster


def handles_for_session(config, session):
    handles = dict(config["handle_map"])
    number = int(session)
    for change in config.get("character_transitions", []):
        if number > change["session"]:
            handles[change["handle"]] = change["new_character"]
    return handles
