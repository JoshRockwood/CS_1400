import argparse


def main():
    validated_args = validate_command_line_arguments()

    formatted_lines = []

    xn = validated_args.initial_population
    for iteration_number in range(0, validated_args.iterations + 1):
        formatted_lines.append(f"{iteration_number} {xn:.3f}\n")
        xn = logistics_equation(validated_args.growth_rate, xn)

    write_file_lines(formatted_lines, validated_args.output_file_name)


def validate_command_line_arguments():
    parser = argparse.ArgumentParser(description="Monitors the population of Archmaedea IV's magical creatures.")

    # Add arguments
    parser.add_argument("initial_population", type=float,
                        help="initial population as a percentage of the total population 0 < x0 < 1")
    parser.add_argument("growth_rate", type=float, help="growth rate is a number in the range 0 < r < 4")
    parser.add_argument("iterations", type=int, help="number of iterations is a positive integer")
    parser.add_argument("output_file_name", type=str, help="name of output_file")

    args = parser.parse_args()

    if not (0 < args.initial_population < 1):
        parser.error("Initial population must be between 0 and 1")

    if not (0 < args.growth_rate < 4):
        parser.error("Growth rate must be between 0 and 4")

    if not (0 < args.iterations):
        parser.error("Iterations must be a positive integer")

    return args


def logistics_equation(r, xn):
    # r is growth rate, xn is population at time
    xn_plus_1 = r * xn * (1 - xn)
    return xn_plus_1


def write_file_lines(lines, output_file_name):
    with open(output_file_name, "w") as file:
        file.writelines(lines)


if __name__ == "__main__":
    main()
