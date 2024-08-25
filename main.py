import argparse
import json

import module_factory
import cli_args

def read_options_file():
    with open('options.json') as f:
        options = json.load(f)
        
    return options

def write_options_file(options):
    with open('options.json', 'w') as f:
        json.dump(options, f, indent=4)

def update_options_with_args(parser, args_for_config, options):
    # Apply incoming args to update options.json
    for group in parser._action_groups:
        # Skip default Argparser groups
        if group.title == "positional arguments" or group.title == "options":
            continue

        # Select args pertaining to group
        print(f'ARG GROUP: {group.title}')
        group_arg_keys = [a.dest for a in group._group_actions]
        options_to_update = {k: v for k, v in args_for_config.items() if k in group_arg_keys}

        # Apply new settings to JSON options of relevant module
        options[group.title.value].update(options_to_update)

    return options

def read_cli(options):
    parser = argparse.ArgumentParser(description='Run FLOMPS Simulation Suite')

    # Add args to respective parser groups for each module, such that group titles match JSON module keys for configuration
    cli_args.add_sat_sim_args(parser)
    cli_args.add_algorithm_args(parser)
    cli_args.add_fl_args(parser)

    # Only get arg keys with specified values
    args = parser.parse_args()
    args_for_config = {k: v for k, v in args.__dict__.items() if v is not None}
    print(args_for_config)

    updated_options = update_options_with_args(parser, args_for_config, options)
    write_options_file(updated_options)

if __name__ == "__main__":
    options = read_options_file()
    read_cli(options)

    # Argparse

    # 1) End-to-End Simulation

    # 2) SatSim only (can execute either from this file or run independent sat_sim.py file)

    # 3) Algorithm only (requires adjacency matrices file)

    # 4) FL only (requires parametric matrices file)

    # 5) Model only (for testing purposes, 
    #                run either MNIST or ResNet
    #                on its own without FL overhead)

    # Create Modules
    # sat_sim_module = module_factory.create_sat_sim_module()
    # sat_sim_module.config.read_options(options["sat_sim"])

    # algorithm_module = module_factory.create_algorithm_module()
    # algorithm_module.config.read_options(options["algorithm"])

    # fl_module = module_factory.create_fl_module()
    # fl_module.config.read_options(options["federated_learning"])

    # # Simulation Process
    # sat_sim_module.input.parse_input('TLEs/leoSatelliteConstellation4.tle')
    # matrices = sat_sim_module.input.run_module()
    # print(matrices)

    # algorithm_module.input.parse_input(matrices)

    # Algorithm Output -> FL Input
    # algorithm_output.set_fl_input(fl_input)

    # fl_input.federated_learning.start_server()

    # Run Sat Sim
    

    # Pass input to Algorithm

   

