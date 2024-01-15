!!! info "Username and Password character restrictions"

    Username must match the following regular expression:
    `/^[A-Za-z0-9_][A-Za-z0-9_-]*\$?$/`

    - it must start with one of these characters: `A-Z` `a-z` `0-9` `_`
    - it may contain any of these characters: `A-Z` `a-z` `0-9` `_-`
    - `$` is only allowed once at the very end

    Password must match the following regular expression:
    `/^[A-Za-z0-9.,\/_@%^:=+ -]*$/`

    - it must contain only these characters: `A-Z` `a-z` `0-9` `.,/_@%^:=+ -`
