import argparse

def read_user_cli_args():

    parser = argparse.ArgumentParser(
        prog="sitechecker", description="Checks for target URLs availability"
    )

    parser.add_argument(
        "-u",
        "--urls",
        metavar="URLs",
        nargs="+",
        type=str,
        default=[],
        help="Input one or more URLs"
    )

# added argument for reading URLs from files
    parser.add_argument(
        "-f",
        "--input-file",
        metavar="FILE",
        type=str,
        default="",
        help="Read URLs from file",
    )
    return parser.parse_args()

def display_check_result(result, url, error=""):
    print(f'URL "{url}" is:', end =" ")
    if result:
        print('"Online!👍"')
    else:
        print(f'"Offline?" 👎 \n  Erro: "{error}"')