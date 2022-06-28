#!/bin/sh

logo="%{T3}  %{T-}"
updates=$(zypper lu | wc -l)
total=$((updates-4))

if [ "$total" -gt 0 ]; then
    echo "$logo$total "
else
    echo "$logo"
fi
