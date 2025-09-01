Enter your action: d - 1 2 4
Traceback (most recent call last):
  File "C:\U...\TwitchProjects\balatrocli\main.py", line 10, in <module>
    main()
    ~~~~^^
  File "C:\U...\TwitchProjects\balatrocli\main.py", line 6, in main
    BalatroCLI().run()
    ~~~~~~~~~~~~~~~~^^
  File "C:\U...\TwitchProjects\balatrocli\balatro\cli.py", line 109, in run
    if not self._handle_action(action, additional_input):
           ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\U...\TwitchProjects\balatrocli\balatro\cli.py", line 52, in _handle_action
    card_indices = [int(idx) for idx in additional_input.split()]
                    ~~~^^^^^
ValueError: invalid literal for int() with base 10: '-'