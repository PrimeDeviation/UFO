# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

import argparse
from datetime import datetime

from .module.state import SessionFinishState, ErrorState, MaxStepReachedState, NoneState
from .module.session import Session
from .config.config import Config
from .utils import print_with_color


configs = Config.get_instance().config_data


args = argparse.ArgumentParser()
args.add_argument("--task", help="The name of current task.",
                  type=str, default=datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))

parsed_args = args.parse_args()



def main():
    """
    Main function.
    """

    session = Session(parsed_args.task)

    while not isinstance(session.get_state(), (SessionFinishState, ErrorState, MaxStepReachedState, NoneState)):

        session.handle()

    if isinstance(session.get_state(), SessionFinishState):
        session.handle()
  
    session.print_cost()
  


if __name__ == "__main__":
    main()
