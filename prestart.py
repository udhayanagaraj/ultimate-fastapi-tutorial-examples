import subprocess
import sys

from alembic.config import Config
from alembic import command

from app.main import ROOT

def main():
    alembic_cfg = Config(ROOT / "alembic.ini")
    subprocess.run([sys.executable,"-m","app.backend_pre_start"],check=True)
    command.revision(
        alembic_cfg,
        message="initial migration",
        autogenerate=True,
    )
    command.upgrade(alembic_cfg,"head")
    subprocess.run([sys.executable,"-m","app.initial_data"],check=True)

if __name__ == "__main__":
    main()