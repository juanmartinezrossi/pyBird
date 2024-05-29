Steps to use:
1. (if in raspberry py): Open a Terminal and execute: pip install -r requirements.txt
2. execute: cp settings_repo.py settings.py
3. Configure parameters in settings.py
4. Execute main_bird.py


Troubleshooting:
1. externally-managed-environment × This environment is externally managed
    solution: excecute 'sudo rm /usr/lib/python3.11/EXTERNALLY-MANAGED'

2. MutableMapping error: Dronekit is not compatible with python versions after 3.10.
    solution: find the directory where the dronekit library is installed in your raspberry pi with:
        pip show dronekit
    e.g.: /usr/local/lib/python3.11/dist-packages/dronekit
    do:
        sudo nano dronekit
    press Alt+R to replace texx:
        Replace: collections
        With:   collections.abc
    do not further update all libraries after this. If you do, repeat this process.

