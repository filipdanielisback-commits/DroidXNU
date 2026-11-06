# Boot menu prototype

The current prototype is a harmless host-side terminal mock-up.

It demonstrates the two labels requested for the future graphical menu:

1. Boot experimental DroidXNU.
2. Reboot to original Android.

Both options are deliberately informational only. Selecting either option prints that the feature is not implemented and returns to the menu. No reboot, kernel loading, EFI call, disk access, or device operation occurs.

## Build on a host with a C compiler

```sh
cc -std=c11 -Wall -Wextra -Werror host-menu.c -o droidxnu-menu
./droidxnu-menu
```

This prototype is not the future EFI GUI. A real loader requires separate platform research, code review, and QEMU testing first.
