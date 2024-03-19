import os
from pathlib import Path


def get_file_from_working_dir(folder_name: str, file_name: str = "") -> Path:
    if os.name == 'nt':  # Windows
        save_dir = Path(f'{Path.home()}/PlayerSetting/{folder_name}')
    else:  # Linux
        save_dir = Path(f'~/.playerSetting/{folder_name}').expanduser()

    save_dir.mkdir(parents=True, exist_ok=True)
    output = Path(f"{save_dir}/{file_name}") if file_name != "" else save_dir

    return output
