/*
 * DroidXNU host menu mock-up.
 *
 * This is NOT an EFI application and cannot boot or reboot anything.
 * It only demonstrates menu labels and input handling on the host.
 */

#include <stdio.h>

static void show_menu(void)
{
    puts("\nDroidXNU — experimental boot menu concept");
    puts("------------------------------------------");
    puts("1. Boot experimental DroidXNU [NOT IMPLEMENTED]");
    puts("2. Reboot to original Android [NOT IMPLEMENTED]");
    puts("0. Exit");
    printf("Choose an option: ");
}

int main(void)
{
    char input[32];

    for (;;) {
        show_menu();

        if (fgets(input, sizeof input, stdin) == NULL) {
            puts("\nInput closed. Exiting mock-up.");
            return 0;
        }

        switch (input[0]) {
        case '1':
            puts("Unavailable: no compatible DroidXNU image or loader exists.");
            break;
        case '2':
            puts("Unavailable: this host mock-up cannot reboot a phone.");
            break;
        case '0':
            puts("Exiting mock-up. No device state was changed.");
            return 0;
        default:
            puts("Unknown choice. Enter 1, 2, or 0.");
            break;
        }
    }
}
