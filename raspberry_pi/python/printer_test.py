from escpos.printer import Serial


def main() -> None:
    printer = Serial(
        devfile="/dev/serial0",
        baudrate=9600,
        bytesize=8,
        parity="N",
        stopbits=1,
        xonxoff=False,
        dsrdtr=False,
    )
    try:
        printer.set(align="center", bold=True, width=2, height=2)
        printer.text("Testing 123\n")

        printer.set(align="center", bold=False, width=1, height=1)
        printer.text("\n")
        printer.qr("https://simonprickett.dev", size=5, center=True)
        printer.text("\n\n")

        printer.barcode(
            "12345678",
            "CODE39",
            height=80,
            width=2,
            pos="BELOW",
            align_ct=True,
        )
        printer.text("\n\n")
        printer.text("Hello, world!\n\n\n\n")
    finally:
        printer.close()


if __name__ == "__main__":
    main()
