workdir() {
  if [[ $# -gt 0 ]]; then
    handler_workdir "$@"
    return 0
  fi

  local target
  target=$(handler_workdir)

  if [[ "$target" =~ ^/.* && -d "$target" ]]; then
    cd "$target" || return 1
    echo -e "\033[1;32m[+] Directory changed to \033[0m$(pwd)"
    return 0
  fi

  echo -e "$target"
}