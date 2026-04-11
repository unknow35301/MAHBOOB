import MAHBOOB

while True:
    try:
        MAHBOOB.main()
        try:
            input("\n\033[38;5;228m══► Press Enter to return to menu (Ctrl+C to exit)... ◄══\033[0m")
        except KeyboardInterrupt:
            print("\nExiting...")
            break
    except KeyboardInterrupt:
        print("\nExiting...")
        break
    except SystemExit:
        break
    except Exception:
        pass